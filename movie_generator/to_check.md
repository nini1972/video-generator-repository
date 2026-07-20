--- CineRepo Console Stdin Ready ---
Click 'Initiate Pipeline Movie' to start.
[08:29:07] Initiating pipeline...
[08:29:07] RepoInvestigator launched. Scanning target path...
[08:36:01] Initializing CineRepo Agent Pipeline...
[08:36:01] Gemini API Key detected. Running live multi-agent cognitive pipeline on: 'C:\Users\ninic\project\ai_detective_story'
[08:36:01] Creative mode: free-form.
[08:36:01] [STAGE 1] Launching RepoInvestigator Agent...
[08:36:01] RepoInvestigator completed in 14.53s. Project identified: 'dual-ai-detective'
[08:36:01] [STAGE 2] Launching PromptArchitect Agent...
[08:36:01] PromptArchitect completed in 10.32s. Brief: 'The Double-Scribed Ledger' (3 symbols mapped, 4 scenes).
[08:36:01] [STAGE 3] Launching StoryboardDirector Agent...
[08:36:01] StoryboardDirector completed in 174.48s. Storyboard populated with 4 scenes (using namespace cache: 'dual-ai-detective').
[08:36:01] [STAGE 3.5] Launching AudioMixer...
[08:36:01] AudioMixer completed in 12.27s.
[08:36:01] Master audio: mixed_audio_79f6aa3ec0f1742e.wav
[08:36:01] [STAGE 4] Launching ProductionStitcher & FFmpeg Engine...
[08:36:01] ProductionStitcher completed in 199.02s.
[08:36:01] > Starting compilation for movie: 'The Double-Scribed Ledger'
[08:36:01] > Verifying FFmpeg executable: FOUND
[08:36:01] > Audio Direction received: [soundtrack_mode=instrumental_only], [speech_mode=full_narration]
[08:36:01] > Soundtrack style instructions: Downtempo darkjazz with a melancholic, reverberating analog tenor saxophone floating over a heavy, pulsing modular synth bass. Driven by slow, mechanical clockwork ticks and brushed snare drums, building to a tense, electric-violin climax.
[08:36:01] > Caching master video reels: https://r2-bucket.flowith.net/concat_1779012993538996307.mp4
[08:36:01] > Master video reels download status: SUCCESS
[08:36:01] > Building personalised Ken Burns video from 4 generated images...
[08:36:01] > Rendering scene 1 clip...
[08:36:01] > Scene 1 clip failed — falling back to cached video.
[08:36:01] > Using pre-mixed master audio track: mixed_audio_79f6aa3ec0f1742e.wav
[08:36:01] > Generated FFmpeg Command: `C:\Users\ninic\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.EXE -y -i C:\Users\ninic\project\hermes agent\movie_generator\assets\target_repos\dual-ai-detective\concat_visuals.mp4 -i C:\Users\ninic\project\hermes agent\movie_generator\assets\target_repos\dual-ai-detective\mixed_audio_79f6aa3ec0f1742e.wav -c:v copy -c:a aac -shortest C:\Users\ninic\project\hermes agent\movie_generator\assets\target_repos\dual-ai-detective\final_movie.mp4`
[08:36:01] > Executing program assembly in sub-process...
[08:36:01] > FFmpeg process completed successfully!
[08:36:05] Pipeline successfully completed! Rendering outputs...



INFO:     127.0.0.1:51555 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:51555 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:51555 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:51555 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:51555 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:51555 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:59334 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:59334 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:59334 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:59334 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:59334 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:59334 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:59334 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:59334 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:59334 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:59334 - "GET /api/status HTTP/1.1" 200 OK
Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
INFO:     127.0.0.1:55396 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:55396 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:55396 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:55396 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:55396 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:55396 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:58093 - "GET /api/status HTTP/1.1" 200 OK
[StoryboardDirector] Launching parallel asset generation (images + speech)...
[ImageGen] Scene 1: generating image...
[ImageGen] Scene 2: generating image...
[ImageGen] Scene 3: generating image...
[TTS] Scene 1: generating narration (119 chars)...
[ImageGen] Scene 4: generating image...
[TTS] Scene 2: generating narration (116 chars)...
[TTS] Scene 3: generating narration (116 chars)...
[TTS] Scene 4: generating narration (107 chars)...
INFO:     127.0.0.1:58093 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:58093 - "GET /api/status HTTP/1.1" 200 OK
[ImageGen] Scene 4: saved successfully (1722KB).
[ImageGen] Scene 1: saved successfully (1599KB).
[ImageGen] Scene 2: saved successfully (1932KB).
[ImageGen] Scene 3: saved successfully (1790KB).
[TTS] Scene 3: saved successfully (651KB).
[TTS] Scene 1: saved successfully (656KB).
INFO:     127.0.0.1:58093 - "GET /api/status HTTP/1.1" 200 OK
[TTS] Scene 2: saved successfully (941KB).
INFO:     127.0.0.1:58093 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:58093 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:58093 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:58093 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:58093 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:58093 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:58093 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:58093 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
[TTS] Scene 4: gemini-2.5-flash-preview-tts produced implausibly long audio. Retrying...
[TTS] Scene 4: gemini-2.5-flash-preview-tts returned no audio part.
[TTS] Scene 4: gemini-3.1-flash-tts failed — 404 NOT_FOUND. {'error': {'code': 404, 'message': 'models/gemini-3.1-flash-tts is not found for API version v1beta, or i
[TTS] Scene 4: all models failed, skipping speech.
[TTS] Scene 1: extended visual from 10.00s to 14.76s to fit narration.
[TTS] Scene 2: extended visual from 10.00s to 20.84s to fit narration.
[TTS] Scene 3: extended visual from 10.00s to 14.64s to fit narration.
[MusicGen] Generating 60s soundtrack: Downtempo darkjazz with a melancholic, reverberating analog tenor saxophone floating over a heavy, pulsing modular synth bass. Driven by slow, mechanical clockwork ticks and brushed snare drums, building to a tense, electric-violin climax....
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
[MusicGen] Soundtrack saved successfully (727KB, model=lyria-3-clip-preview).
[AudioMixer] Mixing master audio track...
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
[AudioMixer] Master audio saved (10377KB, 60.2s).
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:50623 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:62500 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:62500 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:62500 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:62500 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:62500 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:62500 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:62500 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:62500 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:62500 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:62500 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:62500 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:62500 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:51931 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:51931 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:53352 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:53352 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:53352 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:53352 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:53352 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:53352 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:53352 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:53352 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:53352 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:53352 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:53352 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:53352 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:59334 - "POST /api/pipeline/run HTTP/1.1" 200 OK
INFO:     127.0.0.1:59334 - "GET /api/assets/image?path=C%3A%5CUsers%5Cninic%5Cproject%5Chermes%20agent%5Cmovie_generator%5Cassets%5Ctarget_repos%5Cdual-ai-detective%5Cscene_1_a686ea2d8165be70.png HTTP/1.1" 200 OK
INFO:     127.0.0.1:57150 - "GET /api/assets/image?path=C%3A%5CUsers%5Cninic%5Cproject%5Chermes%20agent%5Cmovie_generator%5Cassets%5Ctarget_repos%5Cdual-ai-detective%5Cscene_3_914dbf8caebd7839.png HTTP/1.1" 200 OK
INFO:     127.0.0.1:55364 - "GET /api/assets/image?path=C%3A%5CUsers%5Cninic%5Cproject%5Chermes%20agent%5Cmovie_generator%5Cassets%5Ctarget_repos%5Cdual-ai-detective%5Cscene_2_d79e773440930e02.png HTTP/1.1" 200 OK
INFO:     127.0.0.1:52332 - "GET /api/assets/video?t=1784529365922&repo_name=dual-ai-detective HTTP/1.1" 206 Partial Content
INFO:     127.0.0.1:60008 - "GET /api/assets/video?t=1784529365922&repo_name=dual-ai-detective HTTP/1.1" 206 Partial Content
INFO:     127.0.0.1:59334 - "GET /api/assets/image?path=C%3A%5CUsers%5Cninic%5Cproject%5Chermes%20agent%5Cmovie_generator%5Cassets%5Ctarget_repos%5Cdual-ai-detective%5Cscene_4_5c07fb8292e5438d.png HTTP/1.1" 200 OK
INFO:     127.0.0.1:57150 - "GET /api/assets/video?t=1784529365922&repo_name=dual-ai-detective HTTP/1.1" 206 Partial Content
INFO:     127.0.0.1:60008 - "GET /api/assets/video?t=1784529365922&repo_name=dual-ai-detective HTTP/1.1" 206 Partial Content
Exception in callback _ProactorBasePipeTransport._call_connection_lost()
handle: <Handle _ProactorBasePipeTransport._call_connection_lost()>
Traceback (most recent call last):
  File "C:\Users\ninic\AppData\Local\Python\pythoncore-3.14-64\Lib\asyncio\events.py", line 94, in _run
    self._context.run(self._callback, *self._args)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\ninic\AppData\Local\Python\pythoncore-3.14-64\Lib\asyncio\proactor_events.py", line 165, in _call_connection_lost
    self._sock.shutdown(socket.SHUT_RDWR)
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
ConnectionResetError: [WinError 10054] An existing connection was forcibly closed by the remote host
INFO:     127.0.0.1:59334 - "GET /favicon.ico HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:59334 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:59334 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:59334 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:60008 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:60008 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:60008 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:60008 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:60008 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:60008 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:60008 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:60008 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:60008 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:60008 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:60008 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:60008 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:60008 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:54810 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:54810 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:54810 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:54810 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:54810 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:54810 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:54810 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:54810 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:54810 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:54810 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:54810 - "GET /api/status HTTP/1.1" 200 OK
INFO:     127.0.0.1:54810 - "GET /api/status HTTP/1.1" 200 OK
