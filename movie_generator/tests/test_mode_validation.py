import os
import sys
import tempfile
import unittest

from pydub import AudioSegment
from pydub.generators import Sine

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PARENT = os.path.dirname(PROJECT_ROOT)
if PROJECT_PARENT not in sys.path:
    sys.path.insert(0, PROJECT_PARENT)

from movie_generator.agents.storyboard_director import StoryboardDirector
from movie_generator.agents.prompt_architect import CreativeBriefSchema, PromptArchitect
from movie_generator.audio.mixer import AudioMixer
from movie_generator.audio.speech_synthesiser import SpeechSynthesiser


class ModeValidationTests(unittest.TestCase):
    def test_mock_storyboard_honors_audio_preferences(self):
        director = StoryboardDirector(client=None)
        storyboard = director._get_mock_storyboard(
            soundtrack_pref="no_music",
            speech_pref="no_speech",
        )

        self.assertEqual(storyboard["audio_direction"]["soundtrack_mode"], "no_music")
        self.assertEqual(storyboard["audio_direction"]["speech_mode"], "no_speech")

    def test_mock_creative_brief_exposes_authoritative_directions(self):
        brief = PromptArchitect(client=None)._get_mock_brief()

        self.assertIn("visual_direction", brief)
        self.assertIn("music_prompt", brief)
        self.assertNotIn("visual_anchors", brief)
        self.assertNotIn("music_direction", brief)

    def test_creative_brief_schema_accepts_two_scene_arc(self):
        brief = CreativeBriefSchema.model_validate({
            "title": "Two Scenes",
            "logline": "A compact creative test.",
            "symbol_map": [],
            "scene_arc": [
                {"scene_number": 1, "visual_seed": "An opening image."},
                {"scene_number": 2, "visual_seed": "A closing image."},
            ],
            "tone": "Quietly complete",
            "visual_direction": "Ink on paper",
            "music_prompt": "Sparse acoustic guitar, instrumental only",
            "narration_voice": "Warm and restrained",
        })

        self.assertEqual(len(brief.scene_arc), 2)

    def test_storyboard_rejects_scene_arcs_outside_supported_range(self):
        director = StoryboardDirector(client=object())
        brief = {"scene_arc": [{"scene_number": 1, "visual_seed": "Too short"}]}

        with self.assertRaisesRegex(RuntimeError, "Expected 2-8 scene seeds"):
            director.direct(brief)

    def test_no_speech_mode_skips_scene_synthesis(self):
        scenes = [
            {"scene_number": 1, "narration_text": "First scene."},
            {"scene_number": 2, "narration_text": "Second scene."},
        ]
        synthesiser = SpeechSynthesiser(client=None)

        with tempfile.TemporaryDirectory() as output_dir:
            result = synthesiser.synthesise_all_scenes(
                scenes,
                output_dir,
                speech_mode="no_speech",
            )

        self.assertTrue(all(scene["local_speech_path"] is None for scene in result))

    def test_narration_duration_extends_its_visual_scene(self):
        synthesiser = SpeechSynthesiser(client=None)
        scenes = [{"scene_number": 1, "duration_seconds": 1.0}]

        with tempfile.TemporaryDirectory() as output_dir:
            speech_path = os.path.join(output_dir, "scene_1_speech.wav")
            exported_audio = AudioSegment.silent(duration=2250).export(
                speech_path,
                format="wav",
            )
            exported_audio.close()
            scenes[0]["local_speech_path"] = speech_path

            aligned_scenes = synthesiser.align_scene_durations_to_speech(scenes)

        self.assertEqual(aligned_scenes[0]["speech_duration_seconds"], 2.25)
        self.assertEqual(aligned_scenes[0]["duration_seconds"], 3.0)

    def test_abnormally_long_narration_is_not_used_for_scene_timing(self):
        synthesiser = SpeechSynthesiser(client=None)
        scenes = [{"scene_number": 1, "duration_seconds": 8.0}]

        with tempfile.TemporaryDirectory() as output_dir:
            speech_path = os.path.join(output_dir, "scene_1_speech.wav")
            exported_audio = AudioSegment.silent(duration=91_000).export(
                speech_path,
                format="wav",
            )
            exported_audio.close()
            scenes[0]["local_speech_path"] = speech_path

            aligned_scenes = synthesiser.align_scene_durations_to_speech(scenes)

        self.assertIsNone(aligned_scenes[0]["local_speech_path"])
        self.assertEqual(aligned_scenes[0]["duration_seconds"], 8.0)

    def test_music_is_ducked_only_during_audible_narration(self):
        mixer = AudioMixer()
        music = Sine(220).to_audio_segment(duration=3000).apply_gain(-12)
        speech = (
            AudioSegment.silent(duration=1000)
            + Sine(440).to_audio_segment(duration=1000).apply_gain(-6)
            + AudioSegment.silent(duration=1000)
        )

        ducked = mixer._duck_music_for_speech(music, speech)

        self.assertAlmostEqual(ducked[100:900].dBFS, music[100:900].dBFS, delta=0.1)
        self.assertLess(ducked[1100:1900].dBFS, music[1100:1900].dBFS - 10)
        self.assertAlmostEqual(ducked[2100:2900].dBFS, music[2100:2900].dBFS, delta=0.1)


if __name__ == "__main__":
    unittest.main()