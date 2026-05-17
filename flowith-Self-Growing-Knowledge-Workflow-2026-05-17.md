![Flowith](https://r2.flowith.net/flowith.png)

# Self-Growing Knowledge Workflow

> Exported from Flowith · 2026-05-17

---

### User

<sub>5/17/2026, 10:11:03 AM</sub>

You are a director specialised in short movies. You decide to create company and hire specialised agents for specialised work.  Your goal is to create short story movies around the underlying concept of a Github Project. You will investigate the Project, understand the underlaying concepts, or purpose of the project... You have a total freedom in style, type, lenght etc of the short movie output, but you should be able to explain the link between the short movie and the Github Project. 
Lets try out with the following link:https://github.com/NousResearch/hermes-agent

---

### online search

<sub>5/17/2026, 10:11:24 AM</sub>

The NousResearch Hermes Agent is an open-source, self-improving AI agent framework designed for long-lived, persistent operation, distinguishing itself from session-based assistants. Its core philosophy centers on an agent that learns and grows with the user over time, emphasizing learning depth and memory quality rather than just ecosystem breadth.

### Core Features

The Hermes Agent boasts a comprehensive set of features aimed at creating a highly capable and autonomous assistant:
*   **Closed Learning Loop and Persistent Memory:** A central tenet is its built-in learning loop. The agent curates memory across sessions, autonomously creates new skills after completing complex tasks, and refines these skills through repeated use. It leverages SQLite FTS5 for search over prior sessions and LLM summarization for effective cross-session recall.
*   **Multi-platform Messaging Gateway:** Hermes can be interacted with across various messaging platforms, including Telegram, Discord, Slack, WhatsApp, Signal, and Email, through a single gateway process, ensuring continuous conversations across devices.
*   **Flexible Model Provider Support:** It supports a wide array of Large Language Model (LLM) providers, such as Nous Portal, OpenRouter (with over 200 models), OpenAI, Anthropic, Xiaomi MiMo, z.ai, and MiniMax, allowing operators to switch models without code changes and avoiding vendor lock-in.
*   **Terminal User Interface (TUI):** For developers, it provides a full terminal UI with features like multiline editing, slash-command autocomplete, conversation history, and streaming tool output.
*   **Autonomous Skill Creation and Improvement:** Hermes can convert solved workflows into reusable skills and improves them as tasks repeat and procedures evolve, shifting from session-based recall to procedural learning.
*   **Scheduled Automations:** A built-in cron scheduler enables natural-language-defined daily reports, nightly backups, and weekly audits to run unattended.
*   **Subagent Delegation and Parallelization:** Users can spawn isolated subagents for parallel workstreams and write Python scripts to call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns.
*   **Extensive Toolset and Sandboxing:** Hermes includes over 40 built-in tools covering terminal access, file operations, browser automation, code execution, image generation, and natural language scheduling. It also supports real sandboxing with various backends like local, Docker, and SSH for secure operations.

### Function Calling Capabilities

The Hermes model family, particularly versions like Hermes 2 Pro, Hermes 3, and Hermes 4, are specifically designed and trained for advanced agentic function-calling and structured output.
*   **Hermes Function Calling Standard:** This standard allows LLM agents to execute API calls directly from user instructions. For example, an agent can interpret a request like "find a flight from New York to Los Angeles for next Friday," generate the necessary `search_flights` function call, and return the results.
*   **Training Data:** The models are trained on specialized datasets, such as `hermes-function-calling-v1`, which compile structured output and function-calling conversations, JSON mode, agentic JSON mode, and structured extraction samples. This training enables LLMs to interpret queries and execute appropriate single or multiple function calls reliably.
*   **Tool Access:** Hermes models can leverage a diverse set of functions, including `code_interpreter`, `google_search_and_scrape`, `get_current_stock_price`, `get_company_news`, and more, to gather information and perform tasks based on user queries.

### Philosophy Behind the Hermes Model Family

Nous Research's philosophy for the Hermes model family is deeply rooted in **open-source principles, user control, and continuous self-improvement**.
*   **Self-Improving and User-Aligned AI:** The fundamental idea is to create a "self-improving AI agent that grows with you." This means the agent continuously learns from interactions, builds persistent knowledge, and develops a deeper understanding of the user across sessions.
*   **Open-Source and Neutral Alignment:** Nous Research advocates for "neutral alignment," which emphasizes user steerability and minimal refusals, in contrast to what they perceive as corporate safety filters that might stifle creativity and exploration. Hermes models are openly available, reflecting a commitment to democratizing advanced AI capabilities.
*   **Hybrid Reasoning:** Models like Hermes 4 introduce "hybrid reasoning," allowing users to toggle between fast responses and deeper, step-by-step thinking processes. This involves the model generating its internal reasoning within `<think>` tags before providing a final answer, offering transparency into the AI's thought process.
*   **Operational Agent and Data Generation Pipeline:** Beyond its role as an operational agent, Hermes Agent also functions as a data generation pipeline for training the next generation of AI agents. Nous Research uses methods like rejection sampling and length control training to produce high-quality synthetic reasoning data.

 Sources: 
- [i-scoop.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEf4oY-zL-pPHPb5roUMRcRZJ393viLxNe18lWGrPissce6H1JYsAOej49ALp8oKqlxU6I0SxirjFK3wX6zZYzUnr-HJDh3GJTrRyqQDEIOA1dDf2j8VMc8O_drCo5aq1oO6FbKfh0iio7sMt0Pbka2YBw=)
- [jimmysong.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoDbPGB-oxmNtttK9HiOFpdSIyGFgkVw7FV4m6gcgbxBcxQnZ-hvjOf1qDcAT10JUqUrsWtLT6Q-NRF-5PWsbFf8OIIuz7Ua730Jf-EZvBsWK9K2_uqYbXxy-uatIqeLw=)
- [bitcoin.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEONLQhQVxdpusfUzBICiWMYUltncUsRwgBlmvxYiqmer4e3jsPgZ_dghot9e3b4QwB38iEYq4UgxhVPnkANabeUC4rSEPEwVaEqUD8q1xf3yH36U9us-OymzPzxa4PiZaw_0kJq_CeoULgzn3JNwp_NUbraF3M7ZahwrRioth9Sq21J3tT9wGlOVPkiHTEp1NTWzTN)
- [explainx.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC2jCyxC2szAeWU_owkudpexvbtdt-0AzBE1fs2iPu7oEX0pX_hmZLW1bC9GauKVKTGW_ErHlg2kQpjiU9bprIA8kbhEfdm5q1bIIuxcy7VX-N_ZrfbSvfhok7EPG6jGoiEaVuMkzwgVbqLHEcNZmhPrl_WULormqDqqiH97wDultZNZ9GkNY7xR_Uvg==)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIF96roQTJ5om9r3v1aIEnvOTX42r0gYq-j4_T5GhyTLkm8-U5BSJoSVjMSSbwOL7-rGNEXH02WLRj1Ba6Ywbk2bF09gyAxkETQkg0RhuAJh_qZ75a9mNMzsMw6MDxDw0MBle_Cvk=)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmMytay2S85A1_qE1oHz2HyfMOCb7hxLa0ZAXhFapS2rqyo35Nxh7QiRbxVcImJTnfIb9VE_EmH7s4IZ1qdVbCpdaHC5iUPmLYAiJFZVOhqDY7YXXtiCNv8Yc8FzCXUqvG)
- [knightli.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEj9AcfUZlHPuGIjbm2shxOKM7rg8CJU9TLtuFiSqVKgGFsuwEC-Jqhf4LRVz4E1sRnWGGSkomP65hifa2zDp4XJFEaaqiYz_Vx6q5xER5D4JFCXX1aW828g39jbDIY1OfX8BVevEYpfLKVODDm2gT_HevxZxocEisofqL1_GvbOSm4Qxb1-5Y=)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoI2w6o7JcqqwUKcyFOooha8soGI1PZWtVRsuyqiFtCwWyEjJMTDIGYTV9vcfTvxAmXQg5ht7ZUcBM2JNdmnfZGQUQZfc-MGEZZReLFdoopkXR3xR8A8i0gN5_IQ8m5UZtmUJk6GhKtAsQVywjOokEfwPVRLtIuTTwtDwrIKwtfrL0)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGicofUbdIUJGavK-bP1ElU7mWiblZnkhx15LbvIPdE9fLwQqR2t1J38cZ3VUEBnTZccSPxNKR-PnfdHjBE4gmGKqBBjH2bVjFYT3SwpxM5ZATVC45Jy2v7YEM3)
- [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI4PMeaxtEHprmFphuHZJqXoVlDePOsqfOYGFFDRp7EEnjanQ85E8vHOxJHLCvHXo98eC_m7dCp9ulPf3FhQC8N6074hQMIJZYDblXtyIdRk3BVR3sK5TIXzQMmd0Qi8N1nNgKP8lgmpd1dArzcpnPaU71XyqEoUes9I3_24cklYlhIOq3-vqt49TMSTOVc-ojmJldZIE=)
- [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzDvZ4HrRm_GJ68Iy1ZRLPftWnG-j7IsVv8ZdHIRCvP47XSJFxQ_tS21TcSoJDvYvhUQQVyo2ujUR-On7CqpHloWnPLcwILdJiT36wwMQV7o5kbRzZTFFXulRKxUyK_p6Eh3mUPxMc7GxSUVTKg69RRJEqUuBAcHF7xQk0qkGvItiQ)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8MmJrne2GyG0IX8ElZrFIe5vu6OA5CGrbgwpCD1chJhFHp5xvMQmoowXUFuwoV8qhoID6UlNq9PxbisL6FPj3x7poCJYxu3i_dpes2chDqo9Iqrtu3jm46x7Xk4hgrWBUb_mBtkl4awoTyr14mmkaVv4pz6656rBouBXv4uTUS9GzM_jgORr6aXgXK55zCqWWipjKRiRrfXY0iNpMAA==)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFImeQQTrHYAY_LOD_JvImd2eCZ_T4AZJvC3lSaaGdVi2QJeJ8TGwwGdPtfXErbuCW6TGjQSeHGP3pgcX6AycvYV17GYha10Lpu0N4sgrcqL4wzBYjl8sAkfNltjsT8WiZQ1Gj_-dfBNmpZ3ABb_qUWQnw=)
- [venturebeat.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5aALe9C-n94gzW-1o4Vq9aiRe_YCGIdiJQb-jCn1wQgBAafV7oFxC9KEMga4vX42mM009YqKLtqKRd-_4J15hpdyCow0YNs_Ku8pX2einzYddi7oJ_WEmjIADDHlXPF7ehgJVexggC0T9dzlboGGet77-yBAj5cOPdf_wMHzufquAwxlrki_anczzXD8qSSQxIK3ixzCPE6gYwv5JF7hBW98_UPHHYV08WAfqHtlxsNo=)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf2CLAO5wZ_R6YFz9I619oqPO1SHlw_JoYzPoU9nI9u6ktsWadn4pIcSF1hqqIApbOSDoT90YXo12fHmoOdRWzu5wf-7nnyyD7xGBGYO94lte4hmRgGF7wlzkQP1ReKt3S_XvcRXkELYpUppbz2kartPAbHImTllHf5sWk2lEBdeCJjORZgMhQGulHKDMPLmsDPMLpCZ3Jll6yX0KN1u3G6y1Wdfo_n-VBjdbnGJJD076fBXtszSKE4TZXrGms0uDE74PhnvlZNSlw)
- [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGORXOa8wLEHRAzY4DcMQp7w5D1TdjoNsemS-bVdLG5OXeUMoDNFaDlAyQTiDXbPxjXtpJMFUkdZ-ZcQtVyzsx2qFeMJ1_mlGFEXf3fjacmLL7EqZzql8F5cuvPG48Q38jVidZP7zE=)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG96k3pOUJBkNYEi2ktPUoO_-S_jKQGXkSEbFsnO6hVCYc66LWeTv9yhuMUvXeXxwq4TNoUJIohYGGrr3jvI-5r0paTULDrRsC-tkcPzBBSRqBR4d8cYxHCXQLszwvHSGMYlilMbseVXoUePiK4TSJxWwtX8U5zvukQKVmFJQX9jRSehpeC9f7AEsbhUw==)
- [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZA4Rwdx8MBLKSdeoo8y4Wpbffcu_qQjSGvAqZkQ-llqRA5ii1gSNfKyDXAipa66pOuRtibobhjV-KKJnVg1iR2W8PuAeyJTUw1AOYY3FYEltzW0nUdZecq3rV)

---

### online search

<sub>5/17/2026, 10:11:24 AM</sub>

NousResearch's Hermes Agent is an open-source, self-improving AI agent designed to "grow with you," distinguishing itself from conventional session-based assistants by maintaining persistent memory and autonomously creating and refining skills over time. This agent framework can be deployed on various infrastructures, from a $5 VPS to GPU clusters, and offers cross-platform continuity across messaging services like Telegram, Discord, and Slack.

### Core Features of Hermes Agent

The Hermes Agent boasts a robust set of core features aimed at creating a powerful and autonomous assistant:
*   **Closed Learning Loop:** The agent continuously learns and improves through agent-curated memory with periodic nudges, autonomous skill creation for complex tasks, and self-improving skills during use. It also utilizes FTS5 full-text search with LLM summarization for recalling past conversations across sessions.
*   **Persistent Memory and Context Management:** Unlike typical AI assistants that reset after each session, Hermes Agent builds a persistent model of the user and their work, remembering learned skills and solutions to problems. It automatically discovers and loads project context files (e.g., `.hermes.md`) and allows users to inject files, folders, Git diffs, and URLs into messages using context references.
*   **Multi-platform Messaging Gateway:** Hermes Agent provides a single gateway process supporting various messaging platforms (Telegram, Discord, Slack, WhatsApp, Signal, CLI) and includes voice memo transcription, ensuring conversation continuity across devices and applications.
*   **Extensive Tooling and Automation:** It comes with over 40 built-in tools for terminal operations, file management, web search, browser automation, code execution, image generation, and text-to-speech. Hermes also supports scheduled automations via a built-in cron scheduler for tasks like daily reports or nightly backups.
*   **Subagent Delegation and Parallelization:** The agent can spawn isolated subagents for parallel workstreams and allows Python scripts to call tools via RPC, streamlining multi-step pipelines.
*   **LLM Provider Flexibility:** Hermes supports free switching between multiple LLM providers, including Nous Portal, OpenRouter (offering over 200 models), OpenAI, and Anthropic, without requiring code changes or vendor lock-in. It also offers fine-grained control over which AI providers handle requests, optimizing for cost, speed, or quality.

### Function Calling Capabilities

NousResearch has significantly emphasized function calling across its Hermes model family. The "Hermes Function Calling Standard" enables LLM agents to execute API calls directly from user instructions, greatly enhancing their utility in digital assistants.

*   **Hermes 2 Pro:** This model, particularly the Mistral 7B version, is explicitly designed for function calling and JSON structured outputs. It was trained on an updated dataset that includes a dedicated Function Calling and JSON Mode dataset. Hermes 2 Pro scored 90% on a function calling evaluation and 84% on a structured JSON output evaluation, demonstrating its proficiency in interpreting queries and executing appropriate single or multiple function calls. The model uses ChatML as its prompt format, providing a structured system for multi-turn chat dialogue and steerability through system prompts.
*   **Hermes 3:** This version features enhanced agentic function-calling capabilities, alongside advanced long-term context retention and multi-turn conversation.
*   **Hermes 4:** While the primary focus of Hermes 4 is hybrid reasoning and user control, the underlying model family also benefits from the advancements in function calling seen in earlier iterations, enabling agents to interact directly with APIs.

### Philosophy Behind the Hermes Model Family

The Hermes model family, particularly highlighted with Hermes 4, is built upon a philosophy centered on user control, open-source principles, and "neutral alignment":

*   **User Control and Steerability:** Nous Research prioritizes giving users control over AI capabilities. Their models are designed to be "steerable," allowing them to be fine-tuned or prompted to behave in specific ways without the rigid safety constraints often found in commercial AI systems. This approach aims to minimize unnecessary refusals and moralizing, fostering a more creative and engaging assistant "aligned to you" rather than corporate policies.
*   **Open-Source Ethos:** Nous Research is a leading voice in the open-source AI movement. The Hermes models, including their weights, are made freely available, typically on platforms like Hugging Face, reflecting a commitment to democratizing advanced AI capabilities and providing a blueprint for open research.
*   **Neutral Alignment:** This philosophy emphasizes that the models should be compliant with user intent without imposing blanket "safe-by-default" refusals, while still encoding selective boundaries for harmful content. Hermes 4, for instance, achieves high scores on RefusalBench, indicating its ability to engage with complex topics appropriately.
*   **Hybrid Reasoning:** Hermes 4 introduces hybrid reasoning, allowing models to toggle between fast direct responses and structured reasoning traces (using `<think>...</think>` tags) when complex problems require deeper deliberation. This gives users control over speed-accuracy tradeoffs.

In essence, the NousResearch Hermes Agent and its underlying model family aim to create highly capable, autonomous, and user-centric AI solutions that empower users with greater control and adaptability through continuous learning, robust tooling, and transparent, open-source development.

 Sources: 
- [jimmysong.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6IiRIGq6SFNOo51yYG9cJ06yqlZ0vP6Lx9xdS17tKs8poCCqPwHi70tdD8wDvvZGqZI2BRJlcy9h72PJcPfqNEF8lBNfzntq9T9ws-vU2LcwpRhr0r6Q-WJDmwRzfhyE=)
- [i-scoop.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1tH8N9dHUHtRiKVDuNPHsozi0P8tEbR-tZiIOy7iStbEbm-HSJcnmt7XYXVZzqgb9YiJgTKvIvxK3TMdjwmZqiqByftNX-zgsdO4nQ5iLYDSJiIV0cof5wW7ODSmWV_pFdCl897FkMChytS7UKYU0DK4=)
- [mintlify.app](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqELFIAi-lfGkyclSzTA1rt2vNAPqcRVQsgyCV6hwcZ2bBTCbSI__F3JlnbBoGM3jmq9WMGLKRtCtxdR_3O4sQ-bgRu1_yKaKX0VVAb-ccsXNVOZAs_Fz3bh3cDX88_Ab4BPRQaxgDyteHvqo9K4LoWvlerjHW)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxGqCIqCYrCdJwsIfHA_H0gChzI2F1iBYNUJmV0nGGkhrNXji6_DAzSNQDNGbMlINiO7_bQZ-7kns60RW6r4oW9uJvY_iKkatk0obrLubdl7w21BO0RBmBHjFhaCaSlAuc)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkGs-XYXypNVlcKHrAWkDyrZl_5tO7VXgx9qLC-wbw5Rx8xQ6U8LL2LNOVb1IklBRFUAt-wMuJMY773iIfMgWeS3DzhL1K0BA64M3M_72HI7GlJlR-w-l5dfhbzgRDyckDA0S_C3U4NqvX3cUa9BF5fm3ps-swlDyD2-ce3ysP2neD)
- [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcGlKDU45M6oHyy6azG5DZcUk0nAIVLyJYHmDxq0iss-bQTMmm_JTDf39W-5vlZaZ1AqMJPLn1qx1pMJJhUNdCSo2x-cmVR0HgPKw-I70tvRNYgEIuoxhwkCKOrDHd51W2OxfSIosJGn5W7lndym94Pw8uWmyzNnJbMVtxQHxKUOLsMhW2k9_0MbNVnZvOYUyV0DuESQY=)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoj5O7bZ6gqxmuSseT9Fm9LTp-7kUo3HFqepx657Izrc-vErR-lKx_to9w2XfJTAeH2lnM2skwZqIovaC5_ckc-M9CIGW3Sb-mjQWDKkrLjwg7EcWChgdp4xCUdY4wW5OuRSv4iQa7l8Wi5qtVRjTqvwF4hygu7ZUO5J4wRbEYkaC8b2xzkIFhxFdCi5FYU2bYvrtz3VY-XawWPBrrfg==)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEQCz-jB32pivMzEUJArpZV5Fob1A-EmTIH_Dc8B_PbiFFMVCGREKeE38Cqz-YdHxj0uvb6l2tWYFyaV3P_WX6AAETdL-xDK4JJgTbQ2mWQwSuq6KoyrtJcSqsZzpln9XQbSUFE3Evs9FG0VT3rEHQ6aU=)
- [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYAzWfdDkMR0r7anBrK8S7pSqT-u_LasUdCxijzebSnYy5urFMXKSUk4RR0cHzeyRcHuM3Ic67Ilh7Xhs6SHvmSzxbctjKHXS-0LviflHJgDhJm4vgY4oSRTxZkEe8Yv7P6WTGUE2FATYHiTXGC1-hFtyUc59VWkh5RIep8Q==)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2WAbXkCgzWfdIEWzxRCBeIYPT5DSq5nEBnT6Vryc027q4q8qKK008Ib8WMx1OI0-vyN4w3WNLFwckF4OH1liSmESr9-DJhMUW-50jpAu3SrxclKUVIxotEmaa)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETrzIr1OEipg5yjh2_0rdAQG3K7eBNgThNCPpYUqFd7Au9lQZllz36vcg6rbaOjQDy4j_mN9DuZrV5BFzUJB7deJ7aCgzNI7Onuo7f-ztieHTN86WLJSNk-vQNY473UB9IMvBUWSs9ZO1RhgVk5spCWSpsr152BzElBatDkB4w_e76bdBugA9dHDZv9tyyONS8Fydb7Zxj-miaPTV3XOTXyztbe74RQk9E6P0caZBWIHOtKECHAQBHSKdK08uyk8JHV8SUI_D_kJl_)
- [venturebeat.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9JrPZNMHA_qw0aHmRAIQtIJkWg1DhlhN77X3CYrAJckAfvEknRAwPhcE-Ayz4wCuTaqll06TFccaTENegSHyT-APl2MQaXvXPrWxDh_cuexQl2rkXN8malAjsoRmn96kKFfi9dF4th1YLXF_gO7untoBoWNMJgxCYmcl-iPIlOYXPBkTvZ-e0o8jP2EmiBrMMaEhpz1fUjgDCNGKiWkWWcz_ZSHP39dGzI4AoXnbhBFA=)
- [marktechpost.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG75nxZU-1PjqEfxatztGV30mCPZ1p9CKPQ5dRJwEbpKq-g0CiOiGor9Kyhzta7jawRokyB6gAk04RD65gNmw1qtLEs2aT4hkym9PBfh3lGMws0Gs0uGpzEZxgKslFO6Qdv-adrgkaYr6GKOWREYi2bx_GyVzn_i1QYK4Q_Nd4aatxCJ3-fsqHDpo3eg4bGGzeLQ0FH3D0aV7kHRIb4X5V0bnS3Zeb6SvVzukKyqDQN1sh3lZbQSbEBnRBnit020wqU)
- [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExyYlsnooglzHrkCAQQrNwGhkf4UfBqXzM47-9Z89UYCsXTDUoUpO8-x7RgK92vt2hqcI0P9pybMEPPppDnLS75wqMBZQD2t3TkJHHpEof_zWa8K1d0TyyuwNj_src_6G8LQbKgQM=)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7FjLe4vR-1H4cpVgMbkE4domN9PEj8ZDjBgBIdb-FBS8igB-KNYs6YYz-R3F8XMBZNs3_pnHPpzAH_gAROhCfBmc5YSM4lotltNpssxTh-iULIGu6VDwrn2oAxeFdZEBfZTsGfM-CW8tva-9L99L_0pb_0xHwHBQW-Dt4CWLi-gJLD8YbTrzVVsDwhw==)

---

### online search

<sub>5/17/2026, 10:11:24 AM</sub>

The NousResearch Hermes Agent is an open-source, autonomous AI agent designed with a core philosophy of continuous self-improvement and user alignment, aiming to overcome the "amnesia problem" prevalent in many AI assistants. It is not merely a chatbot or a copilot but a persistent personal agent that learns and evolves with extended use.

### Core Features of the Hermes Agent:

The Hermes Agent boasts a rich set of capabilities that enable it to operate autonomously and effectively across various tasks and platforms:

*   **Persistent Memory:** It remembers user preferences, projects, and environments across sessions, eliminating the need to re-explain context repeatedly. This "agent-curated memory" includes full-text search with LLM summarization for cross-session recall.
*   **Automated Skill Creation:** When the agent solves complex problems, it automatically writes and refines reusable skill documents, learning from experience and improving over time. These skills are searchable, shareable, and compatible with the agentskills.io open standard.
*   **Multi-Platform Gateway:** Hermes can connect and operate across various messaging platforms, including Telegram, Discord, Slack, WhatsApp, Signal, and CLI, from a single gateway process. This allows for seamless conversation continuity across different devices and applications.
*   **Scheduled Automations:** It features a built-in cron scheduler for unattended tasks like daily reports, nightly backups, or weekly audits, delivered to any connected platform.
*   **Parallel Sub-Agents:** Hermes can spawn isolated sub-agents for parallel workstreams, each with its own conversation and terminal, enabling the collapse of multi-step pipelines into zero-context-cost turns via RPC.
*   **Full Browser & Web Control:** Capabilities include web search, page extraction, and full browser automation (navigate, click, type, screenshot), along with vision analysis, image generation, and text-to-speech.
*   **Flexible Execution Environments:** It supports running commands directly on the local machine in an isolated container or via SSH Remote.
*   **LLM Provider Agnostic:** Hermes offers native integration with Nous Portal and access to over 200 models via API keys from providers like OpenRouter, OpenAI, and Anthropic, allowing for flexibility and no vendor lock-in.
*   **Security & Privacy:** Emphasizing zero telemetry, zero data collection, and container hardening with read-only root and dropped capabilities, ensuring all data remains on the user's machine.

### Function Calling Capabilities:

The Hermes model family, particularly Hermes 2 Pro, is specifically designed for robust function calling and structured output.

*   **Hermes Function-calling Standard:** This standard enables LLM agents to execute API calls directly from user instructions. For example, it can interpret a request to "find a flight" and generate the necessary `search_flights` function call.
*   **Training for Structured Outputs:** The models are trained on extensive datasets containing structured output and function-calling conversations, JSON mode, agentic JSON mode, and structured extraction samples. This training allows them to interpret queries and execute appropriate single or multiple function calls.
*   **Prompt Formats:** Hermes models are trained on specific system prompts and structures for function calling and JSON mode, enabling them to respond with only a JSON object adhering to a given schema.
*   **Tool Use:** Tools are functions that extend the agent's capabilities, including terminal access, file operations, web search, browser automation, and more. Hermes 3 also integrates tool use via the Hermes Function Calling standard, where tool definitions are specified as JSON schemas. An example implementation demonstrates Hermes-2 Pro acting as a stock-market expert bot by accessing the Yahoo Finance API to fetch stock prices.

### Philosophy Behind the Hermes Model Family:

Nous Research's philosophy behind the Hermes model family centers on creating "self-improving AI agents that grow with you".

*   **Solving the Amnesia Problem:** A core motivation is to address the frustration of AI assistants losing context between sessions. Hermes agents are built for persistent execution and maintain context over time, learning from interactions and autonomously developing new capabilities through a continuous improvement loop.
*   **Neutral Alignment and User Control:** Especially with Hermes 4, Nous Research advocates for "neutral alignment," emphasizing user control over corporate safety filters and minimizing unnecessary refusals. This approach aims to make AI more creative, engaging, and aligned with user intent, without blanket "safe-by-default" restrictions that might stifle innovation.
*   **Hybrid Reasoning:** Hermes 4 introduces a "hybrid reasoning" mode, allowing users to toggle between fast, direct responses and a deeper, step-by-step thinking process, where the AI generates its internal reasoning within `<think>` tags. This provides transparency into the AI's thought process and allows for a trade-off between speed and accuracy.
*   **Open-Source Methodology:** Nous Research is a proponent of the open-source AI movement, making model weights freely downloadable and providing detailed technical reports, fostering community involvement and transparency in AI development.

 Sources: 
- [hermes-agent.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlTLGLSff2eYxlM_Q7C8Bn2ggU9u9YovCoGlFr287h0rv9AmH3B5arYh3nnzkriHMPiFO-MwOikOlPtsiB6v2123ppVFSsmkMg2fpwqE55DOqvXBU=)
- [hostinger.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnGXV9y7VeFZQhj7QT7L7qAo2dfzf0FQitjkpKggluxx7wxUMbLTrv1eaoWg5N_yRCH00zVp3a-C8Dm0shqE6ht8wfnv4LbxoTA0gd9Mc9sGNGSTFKgaUm-pA2I7zWyNAWnCEqc2cl6RnCxLdbtHzJN_-r)
- [yuv.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAk0C_yKesIcVzCq1oSLEnaKmOBfc0BPIjLVvjcRa37pMCD7up27CjU9W-MSozL9jds_AhtyXGLBETmoMuhlMSnzxsRAzyRP5zbxtFqnMjX7HWUtC0k62amOtg)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEv_L1NGAvY3K0Df_fQOVHOvkEZENL73kPJSOI3Or_eTFFKkDRo82zipDzDxDNKD-S3e_c2ZsXNCfwGkEbKKVmcEjH5jZCN7MH0SToou11EbaEz-hteMht3oa3h9zXYL6HL)
- [jimmysong.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbgtG5iJYot0uPxWsZoNof-r96yiRtoq9P3FsBsdqrgynjVLbjRLcGJBT_iSzurU5isvRs26rhmkZi0BHsEaJMCs9TWZCTvrLSI6L9v-EcUe3wKB1dhcFYE_tUdmRxYHs=)
- [i-scoop.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPuFaw1JhZnmL0K84-6ABHkxdQdfj_NgdTLs5eBMdH7rsw_yeR2feml-T1u2Jg7FTo2IcYs3t_YLxgTNG0BUObId6aTBzfUfjoa_KfdLmNzpMyoOIcIDMR3nz0WcIz2GVJ-WsFYbDfj0ZrjyWYY0mOhyM=)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEht5Jwj7KrNDp1KbICYU7TidYrLDABb3CNPzLzmW3_4_uW5oCZo4OF56-FA14JOx5Y2w-QJXXfNDtkRi2_CEYue3FiZJZPwR2FYtPe8ZdnE30mp819L0sgEnUb-AyRgz1D_aTC0YD5t2RsKFkd0QFAaznRmSP0CzuxGx1wnGECCyPeDUrb-0Q9kxfpRKiXegk28Zbytefy-rY63CwuHLH3LkO9lwMUsU-qk-t6UqGx4IStlMt31Ts5u8jTUg==)
- [nvidia.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3H9-Uu-LWbClvOv7jNDrP5tTn325C09pmksjS8kR6dxueKbELLudMH6sLqUkDkNwUgoUkfU51MMQAUWZaRsq6iBJay_CNp8Hu5Gfi5J3ouTzFPk76R_qcMR5DFLRHLvlmZDdXTqsBL6MpOVl7Q_MOWn2kyrq2YKdqhfc4ndY=)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJagWTiXAdT660QLKVRsbKUL8O8BBrlSPVfY-M6hGTvA85-0YkFt9hQgzFQ7tKixYpkoZPYXwkhUL_E-Eujp_TIjXQzeR0CsT9upHHiJj3SPchLZfGqVDPOdVGefDKXqe5gGT1_tBfc4u2c05ePjs6DmF5Tn79vIhXynrXpwf2ViWQ)
- [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHamouZT8NxUPn9-xh6g_GoffuDnfEQkmOJ9T2pCPmBGHVv6VuM3hnerNug4S6uvEOp8CL_ZQS3ufYWZ1WwOsVw1E004RDt9mN41aF_q6gav8CrGHXmSJPK-oN32oSW5gZp32YpOcnbeeH6nNKJMVNYwp0ITwNX1qmgzhTmCJBP_1t6IOSaPD7U2KRXJI2Ut8NRTrEZ8dI=)
- [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVTFGDL2OcEix6W6EUaKvzR-MOrxCTsYNo8JmGAFBzu4hahdZjF_uCsCCayeGcKH9Oj8ce-1HV2zREfgYZTMNGao6Z2we-HhOXywV0G3aspEgQixokNwMEQeKGLdl89mVhML8-YkIOPYtUuw7SJrO5IyssbdGfNMF-LjHylUKQef4z)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzWanpBxPx8iFpNqVcsGZowIuVQtwiIWyylb8h3V-D0KKhQy-fkGxWiOjR-hjeXxd7tiH-sAQc_9Kz3-owCCZQL-l246TZ6eeQ4vQRjCvO408QOi4fR1EObEaWGEG-iwVtzYfs-Zgm09oUtxhQxXza1NM8sKjF7rSbBiZzm38IQu3eRLFwsBhuFBFpvX45KNHZnOt_sae7K8n0fMO7sg==)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKeT61BLpf49kA1AYvRSaYtNDW7QvUTTJe0KWnnXyGHrpy9KyeUNu4KTZDtdOV1mMMLqTD9sJYtijbigAH2dngYI6I6o14MsQRPycow1Gho5bmDFAHvWhLRO9_UZhmktTqGOSF-g-tJDa6u1-wLzflMrc=)
- [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUF6YOKZioJooKNOql2Hi38OroydulqRzzr6niMkwzYoEnnQpo6bAsKAbyLxLSvxQsjGKJeSdCwk1gne026iJbtWovwDRwHd7M4RH4JV4d9VQDjuQsSo3XtK05)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt4P11Q2Mh_RPtr_q0fG7Vmx6aIeRT1PktuEMiX-WobImD2ja_VUnIL-maX3qMKXR4XyReGfeHiElE2E-gDoLwotLtBefvsNcR3IS9ymkLtcr3TsEpyLW_znxCeZEOjVArE2aKjQQp4F6jdZMZPklDGivgPRNE3pLW4grBpC4n50Vn9oi9xsjy-KBCH0OWMzoJG3djs6ZfqNz4WP5j4VNpP2OvMSMkB95sfF4ufHjmHFl8Ekwx5qf3WTebd46ofoylfQBmE3Uzu80P)
- [marktechpost.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRjATT3cejcTTt1ooihXFcollXp8H_k-bn2EKGpMhMfJMUyqRusYKk8pLpfpKJ-jqYNXdQPyyutc9l4nKigoMts2weRFgXbHHDxjFiummBj6TwJPRNCygG6y-VFaVR9nJmfrsLss1cY5ZDqzh9OX1syEISZqn0tYwDy0T52CSmoA5pUeArXV9PbjIVd6By4hAS9CxdhjCspXMS8zbOSHRKv2Ixj3LfrEsjJ2wpuZ8dSMPLfc6x1yCZosqDEwuF__rd)
- [venturebeat.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoDys0kWAjslRGx0nSvki65wjZweZReZJWhVLUMh1Muzv3u-FYd1rcSiqFgO2JgrsNbSDChyh-de8rf2-9FGjtETaNs5CzuC_nlfgMuvN0zTYUmGWUpT-czt60KbvNGF9mTbZMMPfeMO8kh3F3gx7rV_rG2hgJ_Lf1JbI47n0LT8Q58qLiv9IOrfyd7E7zcReicRkAiuu7wXKhgBtNEtru9Y5mn-LW5xXrTmrnFROeWCU=)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnfFtnCRvm-_OdJCdBC03R3wo2P9iPSJvyCVG-qvf5wQa2PJM3JaKGVIBctv1db4s6RVjsZjQnprMj32gV5O1OAvUOX9WXZmbpyQAEXiDzgT69GlPAsmQluaLiPyLdjWL_YLwziTa7TldPnKwbUuUaFGcfH1qxzOb2MKtqLF8Cz7TlFEVYRCqoNiVx)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGytJJo2kTWsSULkFwBX3VZywtYeLOir-92NQ2cwfj1s2gxItp77UUYsQpo9CrTieZurOOYMTn9NqqY3EkkMLk13W589VaH-RERaSMRh3Qpswg_liUJ_DqURgxHc0z3h9mTp4lLoO1YpMGVT2tVxQSLsRUDRU3hR6o2T_68M3F8cnQWlO5PfUCSA9OKAg==)

---

### read single webpage

<sub>5/17/2026, 10:11:24 AM</sub>

Source URL: https://github.com/NousResearch/hermes-agent

Title: GitHub - NousResearch/hermes-agent: The agent that grows with you

URL Source: https://github.com/NousResearch/hermes-agent

Markdown Content:
# GitHub - NousResearch/hermes-agent: The agent that grows with you · GitHub

[Skip to content](https://github.com/NousResearch/hermes-agent#start-of-content)
## Navigation Menu

Toggle navigation

[](https://github.com/)

[Sign in](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fnousresearch%2Fhermes-agent)

Appearance settings

*   
Platform

    *   
AI CODE CREATION
        *   [GitHub Copilot Write better code with AI](https://github.com/features/copilot)
        *   [GitHub Spark Build and deploy intelligent apps](https://github.com/features/spark)
        *   [GitHub Models Manage and compare prompts](https://github.com/features/models)
        *   [MCP Registry New Integrate external tools](https://github.com/mcp)

    *   
DEVELOPER WORKFLOWS
        *   [Actions Automate any workflow](https://github.com/features/actions)
        *   [Codespaces Instant dev environments](https://github.com/features/codespaces)
        *   [Issues Plan and track work](https://github.com/features/issues)
        *   [Code Review Manage code changes](https://github.com/features/code-review)

    *   
APPLICATION SECURITY
        *   [GitHub Advanced Security Find and fix vulnerabilities](https://github.com/security/advanced-security)
        *   [Code security Secure your code as you build](https://github.com/security/advanced-security/code-security)
        *   [Secret protection Stop leaks before they start](https://github.com/security/advanced-security/secret-protection)

    *   
EXPLORE
        *   [Why GitHub](https://github.com/why-github)
        *   [Documentation](https://docs.github.com/)
        *   [Blog](https://github.blog/)
        *   [Changelog](https://github.blog/changelog)
        *   [Marketplace](https://github.com/marketplace)

[View all features](https://github.com/features)

*   
Solutions

    *   
BY COMPANY SIZE
        *   [Enterprises](https://github.com/enterprise)
        *   [Small and medium teams](https://github.com/team)
        *   [Startups](https://github.com/enterprise/startups)
        *   [Nonprofits](https://github.com/solutions/industry/nonprofits)

    *   
BY USE CASE
        *   [App Modernization](https://github.com/solutions/use-case/app-modernization)
        *   [DevSecOps](https://github.com/solutions/use-case/devsecops)
        *   [DevOps](https://github.com/solutions/use-case/devops)
        *   [CI/CD](https://github.com/solutions/use-case/ci-cd)
        *   [View all use cases](https://github.com/solutions/use-case)

    *   
BY INDUSTRY
        *   [Healthcare](https://github.com/solutions/industry/healthcare)
        *   [Financial services](https://github.com/solutions/industry/financial-services)
        *   [Manufacturing](https://github.com/solutions/industry/manufacturing)
        *   [Government](https://github.com/solutions/industry/government)
        *   [View all industries](https://github.com/solutions/industry)

[View all solutions](https://github.com/solutions)

*   
Resources

    *   
EXPLORE BY TOPIC
        *   [AI](https://github.com/resources/articles?topic=ai)
        *   [Software Development](https://github.com/resources/articles?topic=software-development)
        *   [DevOps](https://github.com/resources/articles?topic=devops)
        *   [Security](https://github.com/resources/articles?topic=security)
        *   [View all topics](https://github.com/resources/articles)

    *   
EXPLORE BY TYPE
        *   [Customer stories](https://github.com/customer-stories)
        *   [Events & webinars](https://github.com/resources/events)
        *   [Ebooks & reports](https://github.com/resources/whitepapers)
        *   [Business insights](https://github.com/solutions/executive-insights)
        *   [GitHub Skills](https://skills.github.com/)

    *   
SUPPORT & SERVICES
        *   [Documentation](https://docs.github.com/)
        *   [Customer support](https://support.github.com/)
        *   [Community forum](https://github.com/orgs/community/discussions)
        *   [Trust center](https://github.com/trust-center)
        *   [Partners](https://github.com/partners)

[View all resources](https://github.com/resources)

*   
Open Source

    *   
COMMUNITY
        *   [GitHub Sponsors Fund open source developers](https://github.com/sponsors)

    *   
PROGRAMS
        *   [Security Lab](https://securitylab.github.com/)
        *   [Maintainer Community](https://maintainers.github.com/)
        *   [Accelerator](https://github.com/accelerator)
        *   [GitHub Stars](https://stars.github.com/)
        *   [Archive Program](https://archiveprogram.github.com/)

    *   
REPOSITORIES
        *   [Topics](https://github.com/topics)
        *   [Trending](https://github.com/trending)
        *   [Collections](https://github.com/collections)

*   
Enterprise

    *   
ENTERPRISE SOLUTIONS
        *   [Enterprise platform AI-powered developer platform](https://github.com/enterprise)

    *   
AVAILABLE ADD-ONS
        *   [GitHub Advanced Security Enterprise-grade security features](https://github.com/security/advanced-security)
        *   [Copilot for Business Enterprise-grade AI features](https://github.com/features/copilot/copilot-business)
        *   [Premium Support Enterprise-grade 24/7 support](https://github.com/premium-support)

*   [Pricing](https://github.com/pricing)

Search or jump to...

# Search code, repositories, users, issues, pull requests...

 Search  

Clear

[Search syntax tips](https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax)

# Provide feedback

We read every piece of feedback, and take your input very seriously.

- [x] Include my email address so I can be contacted 

 Cancel  Submit feedback 

# Saved searches

## Use saved searches to filter your results more quickly

Name 

Query 

To see all available qualifiers, see our [documentation](https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax).

 Cancel  Create saved search 

[Sign in](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fnousresearch%2Fhermes-agent)

[Sign up](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=NousResearch%2Fhermes-agent)

Appearance settings

Resetting focus

You signed in with another tab or window. [Reload](https://github.com/NousResearch/hermes-agent) to refresh your session.You signed out in another tab or window. [Reload](https://github.com/NousResearch/hermes-agent) to refresh your session.You switched accounts on another tab or window. [Reload](https://github.com/NousResearch/hermes-agent) to refresh your session.Dismiss alert

{{ message }}

[NousResearch](https://github.com/NousResearch)/**[hermes-agent](https://github.com/NousResearch/hermes-agent)**Public

*   [Notifications](https://github.com/login?return_to=%2FNousResearch%2Fhermes-agent)You must be signed in to change notification settings
*   [Fork 24.6k](https://github.com/login?return_to=%2FNousResearch%2Fhermes-agent)
*   [Star 154k](https://github.com/login?return_to=%2FNousResearch%2Fhermes-agent) 

*   [Code](https://github.com/NousResearch/hermes-agent)
*   [Issues 4k](https://github.com/NousResearch/hermes-agent/issues)
*   [Pull requests 5k+](https://github.com/NousResearch/hermes-agent/pulls)
*   [Actions](https://github.com/NousResearch/hermes-agent/actions)
*   [Projects](https://github.com/NousResearch/hermes-agent/projects)
*   [Security and quality 0](https://github.com/NousResearch/hermes-agent/security)
*   [Insights](https://github.com/NousResearch/hermes-agent/pulse)

Additional navigation options

*   [Code](https://github.com/NousResearch/hermes-agent)
*   [Issues](https://github.com/NousResearch/hermes-agent/issues)
*   [Pull requests](https://github.com/NousResearch/hermes-agent/pulls)
*   [Actions](https://github.com/NousResearch/hermes-agent/actions)
*   [Projects](https://github.com/NousResearch/hermes-agent/projects)
*   [Security and quality](https://github.com/NousResearch/hermes-agent/security)
*   [Insights](https://github.com/NousResearch/hermes-agent/pulse)

[](https://github.com/NousResearch/hermes-agent)

# NousResearch/hermes-agent

main

[**1015**Branches](https://github.com/NousResearch/hermes-agent/branches)[**13**Tags](https://github.com/NousResearch/hermes-agent/tags)

[](https://github.com/NousResearch/hermes-agent/branches)[](https://github.com/NousResearch/hermes-agent/tags)

Go to file

Code

Open more actions menu

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| ## Latest commit [![Image 1: kshitijk4poor](https://avatars.githubusercontent.com/u/82637225?v=4&size=40)](https://github.com/kshitijk4poor)[kshitijk4poor](https://github.com/NousResearch/hermes-agent/commits?author=kshitijk4poor) [fix(matrix): warn on clock-skew silent message drops (](https://github.com/NousResearch/hermes-agent/commit/519657aa98d4969ec9e23c70c074d1982ef3ccf1)[#12614](https://github.com/NousResearch/hermes-agent/issues/12614)[) (](https://github.com/NousResearch/hermes-agent/commit/519657aa98d4969ec9e23c70c074d1982ef3ccf1)[#27330](https://github.com/NousResearch/hermes-agent/pull/27330)[)](https://github.com/NousResearch/hermes-agent/commit/519657aa98d4969ec9e23c70c074d1982ef3ccf1) Open commit details pending May 17, 2026 [519657a](https://github.com/NousResearch/hermes-agent/commit/519657aa98d4969ec9e23c70c074d1982ef3ccf1)·May 17, 2026 ## History [8,612 Commits](https://github.com/NousResearch/hermes-agent/commits/main/) Open commit details [](https://github.com/NousResearch/hermes-agent/commits/main/)8,612 Commits |
| [.github](https://github.com/NousResearch/hermes-agent/tree/main/.github ".github") | [.github](https://github.com/NousResearch/hermes-agent/tree/main/.github ".github") | [ci: reject PRs with no common ancestor on main (](https://github.com/NousResearch/hermes-agent/commit/887ba1fb03d78f8922b32e7d17dfb1e0998d9315 "ci: reject PRs with no common ancestor on main (#26611) Catches the failure mode that produced #25045: a contributor PR whose branch had been disconnected from main's history (likely an accidental 'git checkout --orphan' or '.git/' re-init). GitHub's merge UI does not refuse merges of unrelated histories, so the PR landed cleanly with its intended one-file change but its parent-less root commit (413990c94) got grafted into main as a second root. The merge resolution itself was correct — main's content won for every conflicting file — but ~1500 files' worth of git blame collapsed onto that single commit. Implementation: 'git merge-base origin/main HEAD' exits non-zero and prints nothing when the two commits share no ancestor. Check both conditions and fail with a clear message + recovery steps. Verified: against the historic state of PR #25045 (base 5d90386ba, head 1149e75db), 'git merge-base' returns empty with exit 1, so the new check would have rejected it.")[#26611](https://github.com/NousResearch/hermes-agent/pull/26611)[)](https://github.com/NousResearch/hermes-agent/commit/887ba1fb03d78f8922b32e7d17dfb1e0998d9315 "ci: reject PRs with no common ancestor on main (#26611) Catches the failure mode that produced #25045: a contributor PR whose branch had been disconnected from main's history (likely an accidental 'git checkout --orphan' or '.git/' re-init). GitHub's merge UI does not refuse merges of unrelated histories, so the PR landed cleanly with its intended one-file change but its parent-less root commit (413990c94) got grafted into main as a second root. The merge resolution itself was correct — main's content won for every conflicting file — but ~1500 files' worth of git blame collapsed onto that single commit. Implementation: 'git merge-base origin/main HEAD' exits non-zero and prints nothing when the two commits share no ancestor. Check both conditions and fail with a clear message + recovery steps. Verified: against the historic state of PR #25045 (base 5d90386ba, head 1149e75db), 'git merge-base' returns empty with exit 1, so the new check would have rejected it.") | May 15, 2026 |
| [.plans](https://github.com/NousResearch/hermes-agent/tree/main/.plans ".plans") | [.plans](https://github.com/NousResearch/hermes-agent/tree/main/.plans ".plans") | [Merge PR](https://github.com/NousResearch/hermes-agent/commit/586fe5d62d0709df43131f88ecd62b1b6d4b0043 "Merge PR #724: feat: --yolo flag to bypass all approval prompts Authored by dmahan93. Adds HERMES_YOLO_MODE env var and --yolo CLI flag to auto-approve all dangerous command prompts. Post-merge: renamed --fuck-it-ship-it to --yolo for brevity, resolved conflict with --checkpoints flag.")[#724](https://github.com/NousResearch/hermes-agent/pull/724)[: feat: --yolo flag to bypass all approval prompts](https://github.com/NousResearch/hermes-agent/commit/586fe5d62d0709df43131f88ecd62b1b6d4b0043 "Merge PR #724: feat: --yolo flag to bypass all approval prompts Authored by dmahan93. Adds HERMES_YOLO_MODE env var and --yolo CLI flag to auto-approve all dangerous command prompts. Post-merge: renamed --fuck-it-ship-it to --yolo for brevity, resolved conflict with --checkpoints flag.") | Mar 11, 2026 |
| [acp_adapter](https://github.com/NousResearch/hermes-agent/tree/main/acp_adapter "acp_adapter") | [acp_adapter](https://github.com/NousResearch/hermes-agent/tree/main/acp_adapter "acp_adapter") | [fix(acp): replay session history before responding to session/load (](https://github.com/NousResearch/hermes-agent/commit/3034eee38ec516109566c00975be4d0276747c34 "fix(acp): replay session history before responding to session/load (#12285 follow-up) (#26957) Switches `_replay_session_history` from `loop.call_soon`-deferred (after the `LoadSessionResponse` is written) to `await`-inline (before the response is constructed) for both `session/load` and `session/resume`. Adds defensive try/except around the awaited call so a replay helper crash still yields a successful load response — partial transcripts are acceptable, total load failure is not. The deferral was added on May 2 in commit 19854c7cd with the rationale \"Zed only attaches streamed transcript/tool updates once the load/resume response has completed.\" That justification was incorrect: - Zed's current ACP integration (zed-industries/zed crates/agent_servers/src/acp.rs) explicitly registers the session-update routing entry BEFORE awaiting the loadSession RPC, with the comment: \"so that any session/update notifications that arrive during the call (e.g. history replay during session/load) can find the thread.\" - Every other reference ACP server (Codex, Claude Code, OpenCode, Pi, agentao) replays history BEFORE responding to the load request. - The ACP spec wording (\"Stream the entire conversation history back to the client via notifications\") and the natural JSON-RPC reading both mean \"during the request's lifetime\", not \"after the response resolves\". Empirical reproduction (reported by Biraj on @agentclientprotocol/sdk v0.21.1): the same custom ACP client works correctly against Codex / Claude Code / OpenCode / Pi but receives 0 notifications from Hermes because it measures the per-call notification count at the moment `loadSession` resolves — which on Hermes was before the `call_soon`- scheduled replay coroutine had a chance to run. Changes: - `acp_adapter/server.py`: remove `_schedule_history_replay`; both `load_session` and `resume_session` now `await self._replay_session_history` before returning, wrapped in try/except that logs and continues on helper exceptions. - `tests/acp/test_server.py`: replace the single `test_load_session_schedules_history_replay_after_response` (which encoded the now-incorrect post-response ordering) with two tests asserting `events == [\"replay\", \"returned\"]` for load and resume. Add two regression tests confirming that a replay helper raising still yields a `LoadSessionResponse` / `ResumeSessionResponse` rather than propagating the exception out as a JSON-RPC error. Result: 240 ACP tests pass (was 238), ruff clean. Verified end-to-end: biraj's synchronous notification-counter pattern now sees 6 notifications during `loadSession` for a 5-message session, matching all other reference ACP servers. The `_fenced_text` change in `acp_adapter/tools.py` from the same May 2 commit is orthogonal and intentionally left intact — it's a separate, still-valid fix for Zed's pipe-as-table rendering. Refs #12285. Follows up #26943 (which added thought-chunk replay but kept the deferral).")[#…](https://github.com/NousResearch/hermes-agent/issues/12285) | May 16, 2026 |
| [acp_registry](https://github.com/NousResearch/hermes-agent/tree/main/acp_registry "acp_registry") | [acp_registry](https://github.com/NousResearch/hermes-agent/tree/main/acp_registry "acp_registry") | [feat(acp-registry): switch to uvx distribution, drop npm launcher](https://github.com/NousResearch/hermes-agent/commit/c8c6ce17315c0f8512cec6f0bc8120141acdf830 "feat(acp-registry): switch to uvx distribution, drop npm launcher The ACP Registry schema supports uvx as a first-class distribution method alongside npx and binary. Pointing the registry directly at the existing hermes-agent PyPI release removes: - the @nousresearch npm scope (we don't own it) - a separate npm publish step on every weekly release - 90 lines of Node launcher + tests in packages/hermes-agent-acp/ The Zed registry now installs Hermes via: uvx --from 'hermes-agent[acp]==<version>' hermes-acp This is the same command the npm launcher was shelling out to anyway, so end-user behavior is unchanged. Registry CI validates the PyPI URL + version-pin exact match automatically. Changes: - acp_registry/agent.json: distribution.npx -> distribution.uvx - delete packages/hermes-agent-acp/ entirely - scripts/release.py: drop npm-launcher bump paths, keep manifest lockstep - tests/acp/test_registry_manifest.py: assert uvx shape + version pin - tests/scripts/test_release_acp_registry.py: rewrite for uvx-only shape - docs (user-guide + dev-guide): drop all npm-launcher references - delete docs/plans/acp-registry-zed-integration.md (stale, npm-shaped) Validated against agentclientprotocol/registry agent.schema.json via jsonschema. hermes-agent==0.13.0 is already live on PyPI.") | May 15, 2026 |
| [agent](https://github.com/NousResearch/hermes-agent/tree/main/agent "agent") | [agent](https://github.com/NousResearch/hermes-agent/tree/main/agent "agent") | [fix: strip image parts for non-vision models with provider profiles +…](https://github.com/NousResearch/hermes-agent/commit/563b4d9e51a46cc421e327b351cb7efe1ccb151b "fix: strip image parts for non-vision models with provider profiles + getattr-safe _custom_providers Original commit 75e5d0f6b by hueilau targeted _build_api_kwargs in pre-refactor run_agent.py. The body now lives in agent/chat_completion_helpers.build_api_kwargs — re-applied there. Also: switch the custom_providers forward (from 21078ebce) to use getattr() — tests build a bare AIAgent via __new__ and would otherwise hit AttributeError on _custom_providers. Co-authored-by: hueilau <33933019+hueilau@users.noreply.github.com>") | May 17, 2026 |
| [assets](https://github.com/NousResearch/hermes-agent/tree/main/assets "assets") | [assets](https://github.com/NousResearch/hermes-agent/tree/main/assets "assets") | [Update banner image to new version](https://github.com/NousResearch/hermes-agent/commit/3e311a009278895df422e4ce58d53d6c0a46a0f8 "Update banner image to new version") | Feb 25, 2026 |
| [cron](https://github.com/NousResearch/hermes-agent/tree/main/cron "cron") | [cron](https://github.com/NousResearch/hermes-agent/tree/main/cron "cron") | [fix(cron): prevent parallel job result loss on exception](https://github.com/NousResearch/hermes-agent/commit/7a7e78a360464b30ba9e9a20525681977b0f2095 "fix(cron): prevent parallel job result loss on exception Replace generator-based result collection with explicit per-future handling. Each future is now processed independently with a 600s timeout. Before: _results.extend(f.result() for f in _futures) - One exception stops the generator, remaining results are lost - No timeout: one hung job blocks the entire tick After: as_completed() + per-future try/except - Each future handled independently - 600s timeout prevents indefinite blocking - Failed futures are logged and counted as failures") | May 17, 2026 |
| [datagen-config-examples](https://github.com/NousResearch/hermes-agent/tree/main/datagen-config-examples "datagen-config-examples") | [datagen-config-examples](https://github.com/NousResearch/hermes-agent/tree/main/datagen-config-examples "datagen-config-examples") | [feat: add WebResearchEnv RL environment for multi-step web research](https://github.com/NousResearch/hermes-agent/commit/15561ec425a74f26bd2051f562d60ec43f78a050 "feat: add WebResearchEnv RL environment for multi-step web research") | Mar 5, 2026 |
| [docker](https://github.com/NousResearch/hermes-agent/tree/main/docker "docker") | [docker](https://github.com/NousResearch/hermes-agent/tree/main/docker "docker") | [fix(docker): chown .venv to hermes so lazy_deps can install platform …](https://github.com/NousResearch/hermes-agent/commit/942adf617910f50a39f41bd200d8083bf4cb2bed "fix(docker): chown .venv to hermes so lazy_deps can install platform packages (#24841) The Dockerfile permissions section made /opt/hermes/.venv readable but not writable by the hermes runtime user. Since the 2026-05-12 policy change moved messaging packages (discord.py, telegram, slack, etc.) out of [all] and into lazy_deps.py, the Docker image no longer ships with them pre-installed. At first gateway boot, lazy_deps.ensure() tries to `uv pip install` them into the venv but fails with EACCES because site-packages is root-owned. The result: every messaging platform adapter silently fails to load inside Docker containers, producing only a cryptic \"discord.py not installed\" warning despite the gateway being correctly configured. Two-part fix: 1. Dockerfile: add /opt/hermes/.venv to the existing chown -R hermes:hermes line so the default (UID 10000) case works out of the box. 2. docker/entrypoint.sh: extend the needs_chown block to also re-chown the .venv when HERMES_UID is remapped. Without this, the build-time chown becomes stale when someone uses the documented HERMES_UID override in docker-compose.yml. Fixes #21536 Related: #17674, #21543, #21755") | May 13, 2026 |
| [docs](https://github.com/NousResearch/hermes-agent/tree/main/docs "docs") | [docs](https://github.com/NousResearch/hermes-agent/tree/main/docs "docs") | [feat(acp-registry): switch to uvx distribution, drop npm launcher](https://github.com/NousResearch/hermes-agent/commit/c8c6ce17315c0f8512cec6f0bc8120141acdf830 "feat(acp-registry): switch to uvx distribution, drop npm launcher The ACP Registry schema supports uvx as a first-class distribution method alongside npx and binary. Pointing the registry directly at the existing hermes-agent PyPI release removes: - the @nousresearch npm scope (we don't own it) - a separate npm publish step on every weekly release - 90 lines of Node launcher + tests in packages/hermes-agent-acp/ The Zed registry now installs Hermes via: uvx --from 'hermes-agent[acp]==<version>' hermes-acp This is the same command the npm launcher was shelling out to anyway, so end-user behavior is unchanged. Registry CI validates the PyPI URL + version-pin exact match automatically. Changes: - acp_registry/agent.json: distribution.npx -> distribution.uvx - delete packages/hermes-agent-acp/ entirely - scripts/release.py: drop npm-launcher bump paths, keep manifest lockstep - tests/acp/test_registry_manifest.py: assert uvx shape + version pin - tests/scripts/test_release_acp_registry.py: rewrite for uvx-only shape - docs (user-guide + dev-guide): drop all npm-launcher references - delete docs/plans/acp-registry-zed-integration.md (stale, npm-shaped) Validated against agentclientprotocol/registry agent.schema.json via jsonschema. hermes-agent==0.13.0 is already live on PyPI.") | May 15, 2026 |
| [gateway](https://github.com/NousResearch/hermes-agent/tree/main/gateway "gateway") | [gateway](https://github.com/NousResearch/hermes-agent/tree/main/gateway "gateway") | [fix(matrix): warn on clock-skew silent message drops (](https://github.com/NousResearch/hermes-agent/commit/519657aa98d4969ec9e23c70c074d1982ef3ccf1 "fix(matrix): warn on clock-skew silent message drops (#12614) (#27330) The 5-second startup-grace filter in _on_room_message silently drops events where event_ts < startup_ts - 5. When the host clock is set ahead of real time, the comparison flips against every live event and the bot 'connects but never replies' — exactly the symptom in #12614. Reporter Schnurzel700 chased this for several weeks before tracing it to their Debian VM's clock being out of sync. The current /1000.0 millisecond->second conversion is correct (mautrix returns ms); the failure mode is purely environmental. Add a one-shot WARNING that fires when: - we are >30s past startup (initial-sync replay window closed), AND - 3 consecutive drops share the same skew within 60s (a constant clock offset, not varied-age backfill from an invited room). State is reset in connect() so reconnects after fixing NTP rearm the detector. Includes the NTP fix instruction in the warning message itself and a new Troubleshooting entry in the Matrix docs. 5 new tests cover the happy path, initial-sync backfill, under- threshold drops, varied-age backfill, and the reconnect rearm path.")[#12614](https://github.com/NousResearch/hermes-agent/issues/12614)[) (](https://github.com/NousResearch/hermes-agent/commit/519657aa98d4969ec9e23c70c074d1982ef3ccf1 "fix(matrix): warn on clock-skew silent message drops (#12614) (#27330) The 5-second startup-grace filter in _on_room_message silently drops events where event_ts < startup_ts - 5. When the host clock is set ahead of real time, the comparison flips against every live event and the bot 'connects but never replies' — exactly the symptom in #12614. Reporter Schnurzel700 chased this for several weeks before tracing it to their Debian VM's clock being out of sync. The current /1000.0 millisecond->second conversion is correct (mautrix returns ms); the failure mode is purely environmental. Add a one-shot WARNING that fires when: - we are >30s past startup (initial-sync replay window closed), AND - 3 consecutive drops share the same skew within 60s (a constant clock offset, not varied-age backfill from an invited room). State is reset in connect() so reconnects after fixing NTP rearm the detector. Includes the NTP fix instruction in the warning message itself and a new Troubleshooting entry in the Matrix docs. 5 new tests cover the happy path, initial-sync backfill, under- threshold drops, varied-age backfill, and the reconnect rearm path.")[#27330](https://github.com/NousResearch/hermes-agent/pull/27330)[)](https://github.com/NousResearch/hermes-agent/commit/519657aa98d4969ec9e23c70c074d1982ef3ccf1 "fix(matrix): warn on clock-skew silent message drops (#12614) (#27330) The 5-second startup-grace filter in _on_room_message silently drops events where event_ts < startup_ts - 5. When the host clock is set ahead of real time, the comparison flips against every live event and the bot 'connects but never replies' — exactly the symptom in #12614. Reporter Schnurzel700 chased this for several weeks before tracing it to their Debian VM's clock being out of sync. The current /1000.0 millisecond->second conversion is correct (mautrix returns ms); the failure mode is purely environmental. Add a one-shot WARNING that fires when: - we are >30s past startup (initial-sync replay window closed), AND - 3 consecutive drops share the same skew within 60s (a constant clock offset, not varied-age backfill from an invited room). State is reset in connect() so reconnects after fixing NTP rearm the detector. Includes the NTP fix instruction in the warning message itself and a new Troubleshooting entry in the Matrix docs. 5 new tests cover the happy path, initial-sync backfill, under- threshold drops, varied-age backfill, and the reconnect rearm path.") | May 17, 2026 |
| [hermes_cli](https://github.com/NousResearch/hermes-agent/tree/main/hermes_cli "hermes_cli") | [hermes_cli](https://github.com/NousResearch/hermes-agent/tree/main/hermes_cli "hermes_cli") | [Local: doctor uses x-goog-api-key for Google generativelanguage endpoint](https://github.com/NousResearch/hermes-agent/commit/364a1dd290245093f76837c6074bb7d4fdc798c6 "Local: doctor uses x-goog-api-key for Google generativelanguage endpoint") | May 17, 2026 |
| [locales](https://github.com/NousResearch/hermes-agent/tree/main/locales "locales") | [locales](https://github.com/NousResearch/hermes-agent/tree/main/locales "locales") | [feat(i18n): localize all gateway commands + web dashboard, add 8 new …](https://github.com/NousResearch/hermes-agent/commit/c39168453d019e758faab7fbe67cd939f8b56d0b "feat(i18n): localize all gateway commands + web dashboard, add 8 new locales (16 total) (#22914) * feat(i18n): localize /model command output Reported by @tianma8888: when Chinese users run /model, the labels (\"Provider:\", \"Context:\", \"_session only_\", etc.) are still English. This routes the static prose through the existing i18n catalog so it follows display.language / HERMES_LANGUAGE. Changes: - locales/{en,zh,ja,de,es,fr,tr,uk}.yaml: add 17 keys under gateway.model.* covering switched/provider/context/max_output/cost/ capabilities/prompt_caching/warning/saved_global/session_only_hint/ current_label/current_tag/more_models_suffix/usage_*. - gateway/run.py _handle_model_command: replace hardcoded f-strings in the picker callback, the text-list fallback, and the direct-switch confirmation block with t(\"gateway.model.<key>\", ...). What stays English: - model IDs, provider slugs, capability strings, cost figures, and the \"[Note: model was just switched...]\" prepended to the model's next prompt (LLM-facing, not user-facing). - The two slightly-different session-only hints unify on a single key with the em-dash phrasing. Validation: tests/agent/test_i18n.py 27/27 passing (parity contract holds), tests/gateway/ -k 'model or i18n' 74/74 passing. * feat(i18n): localize all gateway slash command outputs Expands the i18n catalog from 7 strings to 234 keys across 35 gateway slash command handlers, so non-English users see localized output for \`/profile\`, \`/status\`, \`/help\`, \`/personality\`, \`/voice\`, \`/reset\`, \`/agents\`, \`/restart\`, \`/commands\`, \`/goal\`, \`/retry\`, \`/undo\`, \`/sethome\`, \`/title\`, \`/yolo\`, \`/background\`, \`/approve\`, \`/deny\`, \`/insights\`, \`/debug\`, \`/rollback\`, \`/reasoning\`, \`/fast\`, \`/verbose\`, \`/footer\`, \`/compress\`, \`/topic\`, \`/kanban\`, \`/resume\`, \`/branch\`, \`/usage\`, \`/reload-mcp\`, \`/reload-skills\`, \`/update\`, \`/stop\` (plus the \`/model\` block already added in the previous commit). Reported by @tianma8888 — Chinese users want command output prose in their language, not just the labels we already had. Translations are hand-written for all 8 supported locales (en, zh, ja, de, es, fr, tr, uk), matching each catalog's existing style: full-width punctuation in zh, em-dashes in zh/ja/uk, French spaced colons, German noun capitalization, etc. What stays English (unchanged): - Identifiers/values: model IDs, file paths, profile names, session IDs, command flag names like --global, URLs, config keys. - Backtick code spans: \`/foo\`, \`config.yaml\`. - Log messages (logger.info/warning/error). - LLM-facing system notes prepended to next prompt (e.g. [Note: model was just switched...]). - Strings produced by external modules (gateway_help_lines, format_gateway, manual_compression_feedback) — those have their own surfaces. New shared keys for cross-handler boilerplate: - gateway.shared.session_db_unavailable (5 call sites: branch, title, resume, topic, _disable_telegram_topic_mode_for_chat) - gateway.shared.session_not_found (1 site) - gateway.shared.warn_passthrough (2 sites in /title's f\"⚠️ {e}\" pattern) YAML gotcha fixed: \`yolo.on\` and \`yolo.off\` were originally written unquoted, which YAML 1.1 parses as boolean True/False keys. Renamed to \`yolo.enabled\` / \`yolo.disabled\` for both safety and clarity. Test fix: tests/agent/test_i18n.py::test_t_missing_key_in_non_english_falls_back_to_english now resets the catalog cache on teardown, so the fake \"foo: English Foo\" locale doesn't poison the module-level cache for subsequent tests in the same xdist worker. (Without this, every gateway slash command test that shares a worker with the i18n suite would see the fake catalog.) Validation: - tests/agent/test_i18n.py: 27/27 (parity contract — every key in every locale, matching placeholder tokens). - tests/gateway/: 5077 passed, 0 failed (full gateway suite). - 180 t() call sites added across 35 handlers; 1872 catalog entries total (234 keys × 8 locales). * feat(i18n): add 8 new locales — af, ko, it, ga, zh-hant, pt, ru, hu Expands the static-message catalog from 8 → 16 languages, each with full 270-key parity against the English source-of-truth. Every locale now covers the same surface PR #22914 added: approval prompts plus all 35 gateway slash command outputs. New locales: - af Afrikaans (community ask in #21961 by @GodsBoy; PRs #21962, #21970) - ko Korean (PRs #20297 by @tmdgusya, #22285 by @project820) - it Italian (PR #20371 by @leprincep35700) - ga Irish/Gaeilge (PR #20962 by @ryanmcc09-dot) - zh-hant Traditional Chinese (PRs #20523 by @jackey8616, #13140 by @anomixer) - pt Portuguese (PRs #20443 by @pedroborges, #15737 by @carloshenriquecarniatto, #22063 by @Magaav) - ru Russian (PR #22770 by @DrMaks22) - hu Hungarian (PR #22336 by @lunasec007) Each locale uses native-quality translations matching the existing tone and conventions of the older 8 locales: - zh-hant uses 繁體 characters with TW/HK technical vocabulary (軟體 not 软件, 連線 not 连接, 設定 not 设置, 訊息 not 消息, 工作階段 not 会话, 程式 not 程序, 預設 not 默认, 伺服器 not 服务器), full-width punctuation 「：（）」. - ko uses formal 합니다체 (습니다/합니다) register throughout. - pt uses European Portuguese as baseline with neutral PT/BR vocabulary where possible. - ga uses standard An Caighdeán Oifigiúil; English loanwords retained for tech terms without good Irish equivalents (gateway, API, JSON). - All preserve {placeholder} tokens, backtick code spans, slash commands, brand names (Hermes, MCP, TTS, YOLO, OpenAI, Telegram, etc.), and emoji. Aliases added in agent/i18n.py: - af-za, Afrikaans → af - ko-kr, Korean, 한국어 → ko - it-it, italiano → it - ga-ie, Irish, Gaeilge → ga - zh-tw, zh-hk, zh-mo, traditional-chinese → zh-hant (note: zh-tw used to alias to zh; now aliases to its own zh-hant catalog) - zh-cn, zh-hans, zh-sg → zh (unchanged from before) - pt-pt, pt-br, brazilian, portuguese → pt - ru-ru, Russian, русский → ru - hu-hu, Magyar → hu The zh-tw alias re-routing is intentional: previously typing 'zh-TW' got the Simplified Chinese catalog (wrong vocabulary for Taiwan/HK users). Now those users get the proper Traditional Chinese catalog. Validation: - tests/agent/test_i18n.py: 43/43 (parity contract holds for all 16 languages × 270 keys = 4320 catalog entries, with matching placeholder tokens). - E2E alias resolution verified for all 19 alias inputs (Afrikaans, ko-KR, 한국어, italiano, Gaeilge, zh-TW, zh-HK, traditional-chinese, pt-BR, brazilian, Magyar, etc.). - tests/gateway/: 5198 passed (3 pre-existing TTS routing failures unrelated to i18n). Credit to all contributors whose PRs surfaced these language requests. Their original PRs may now be closed as superseded with credit. * feat(dashboard-i18n): add 14 web dashboard locales matching the static catalog Brings the React dashboard (web/src/) up to the same 16-language coverage the static catalog already has after the previous commits in this PR. The Translations interface is TypeScript-typed, so every new locale must provide every key — tsc -b is the parity guard. Languages added (each is a complete 429-line locale file): - af Afrikaans - ja Japanese (PR #22513 by @snuffxxx surfaced this) - de German (PR #21749 by @mag1art) - es Spanish (PR #21749) - fr French (PRs #21749, #10310 by @foXaCe) - tr Turkish - uk Ukrainian - ko Korean (PRs #21749, #18894 by @ovstng, #22285 by @project820) - it Italian - ga Irish (Gaeilge) - zh-hant Traditional Chinese (PR #13140 by @anomixer) - pt Portuguese (PRs #22063 by @Magaav, #22182 by @wesleysimplicio, #15737 by @carloshenriquecarniatto) - ru Russian (PRs #21749, #22770 by @DrMaks22) - hu Hungarian (PR #22336 by @lunasec007) Each translation covers all 15 namespaces with full key parity vs en.ts, preserves every {placeholder} token verbatim, keeps identifiers untranslated (brand names, file paths, cron expressions, code spans), translates the language.switchTo tooltip into the target language, and matches existing tone conventions (zh-hant uses TW/HK vocab; ja uses formal desu/masu; ko uses formal seumnida register; ga uses An Caighdean Oifigiuil with English loanwords for tech vocab without good Irish equivalents). Plumbing: - web/src/i18n/types.ts: Locale union expanded to all 16 codes. - web/src/i18n/context.tsx: imports all 16 catalogs; exports LOCALE_META (endonym + flag per locale); isLocale() type guard. - web/src/i18n/index.ts: re-export LOCALE_META. - web/src/components/LanguageSwitcher.tsx: replaced two-state EN-ZH toggle with a click-to-open dropdown listing all 16 languages. Note: zh-hant.ts exports zhHant (camelCase) since hyphen is invalid in a JS identifier; the canonical 'zh-hant' string keys it in TRANSLATIONS. Validation: - npx tsc -b: 0 errors. Every locale satisfies Translations. - npm run build (tsc + vite production): green, 2062 modules. - Each locale file is exactly 429 lines. Out of scope: plugin dashboards (kanban/achievements ship as prebuilt bundles with no source in repo); Docusaurus docs (separate surface); TUI (no i18n yet). * feat(plugin-i18n): localize achievements + kanban plugin dashboards across all 16 locales Brings the two shipped plugin dashboards (hermes-achievements, kanban) under the same i18n umbrella as the core dashboard PR #22914 just established. Both bundles now read user-facing strings from the host's i18n catalog via SDK.useI18n() instead of hardcoded English. ## Approach Plugin dashboards ship as prebuilt IIFE bundles in plugins/<name>/dashboard/dist/index.js — no build step, no source in repo (upstream-authored, vendored as compiled JS). Earlier contributor PRs (#22594, #22595, #18747) tried direct edits but didn't actually wire the bundles to read translations. This change does the wiring properly: 1. Each bundle gets a useI18n shim at IIFE scope: const useI18n = SDK.useI18n || function () { return { t: { kanban: null }, locale: \"en\" }; }; Older host SDKs without useI18n still load the bundle and render English fallbacks. 2. A small tx(t, path, fallback, vars) helper resolves dotted keys under the plugin's namespace (t.kanban.* or t.achievements.*) and interpolates {placeholder} tokens. 3. Every React component starts with const { t } = useI18n() and each user-visible string is wrapped in tx(t, \"key\", \"English fallback\"). Helpers called outside React components (window.prompt callers, constants used during init) take t as a parameter. 4. Top-level constants that were English dictionaries (COLUMN_LABEL, COLUMN_HELP, DESTRUCTIVE_TRANSITIONS, DIAGNOSTIC_EVENT_LABELS in kanban) become getColumnLabel(t, status)-style functions backed by FALLBACK_* dictionaries. ## Translations added Two new top-level namespaces added to the dashboard's TypeScript-typed Translations interface: - achievements: ~70 keys covering the hero, scan banner, achievement card, share dialog, stats, filters, and empty states. - kanban: ~145 keys covering the board, columns (with nested columnLabels and columnHelp sub-dicts), card detail panel, bulk-actions toolbar, dependency editor, board switcher, and diagnostic callouts. Each key is provided across all 16 supported locales: en, zh, zh-hant, ja, de, es, fr, tr, uk, af, ko, it, ga, pt, ru, hu. Total new translation entries: ~3,440 (215 keys × 16 locales). ## What stays English (deliberate) - API paths, CSS class names, data-* attributes, JSON keys, regex strings, URLs, file paths (~/.hermes/kanban.db, boards/_archived/). - State identifier strings used as lookup keys (triage / todo / ready / running / blocked / done / archived) — labels translate, key strings don't. - The PNG share-card text rendered to canvas in the achievements ShareDialog (HERMES AGENT watermark, UNLOCKED stamp, tier names) — these become part of a globally-shared image and stay English. - localStorage keys (hermes.kanban.selectedBoard). - Brand names (Kanban, Hermes, WebSocket, Nous Research). ## Contributor credit PR #22594 by @02356abc and PR #22595 by @02356abc supplied the en + zh kanban namespace skeleton (145 keys); used as the en source- of-truth in this commit and translated to the other 14 locales. PR #18747 by @laolaoshiren first surfaced the achievements localization request. ## Validation - npx tsc -b: 0 errors. All 16 locale .ts files satisfy the Translations type with full key parity. - npm run build (tsc + vite production build): green, 2062 modules, 1.56MB JS / 95KB CSS, ~2.5s build. - node --check on both plugin bundles: parse cleanly. - 126 tx() call sites in kanban, 46 in achievements. ## Out of scope - TUI (ui-tui/) has no i18n infrastructure yet. - Docusaurus docs (website/i18n/) — already had zh-Hans; expanding is a separate translation workstream (Thai / Korean / Hindi PRs).") | May 10, 2026 |
| [nix](https://github.com/NousResearch/hermes-agent/tree/main/nix "nix") | [nix](https://github.com/NousResearch/hermes-agent/tree/main/nix "nix") | [chore: remove Atropos RL environments and tinker-atropos integration (](https://github.com/NousResearch/hermes-agent/commit/5af672c7530263544a9f5e2479f3853d83b3b798 "chore: remove Atropos RL environments and tinker-atropos integration (#26106) * chore: remove Atropos RL environments, tools, tests, skill, and tinker-atropos submodule Delete: - environments/ (43 files — base env, agent loop, tool call parsers, benchmarks) - rl_cli.py (standalone RL training CLI) - tools/rl_training_tool.py (all 10 rl_* tools) - tests: test_rl_training_tool, test_tool_call_parsers, test_managed_server_tool_support, test_agent_loop, test_agent_loop_vllm, test_agent_loop_tool_calling, test_terminalbench2_env_security - optional-skills/mlops/hermes-atropos-environments/ - tinker-atropos git submodule + .gitmodules * chore: remove RL/Atropos references from Python source - toolsets.py: remove rl toolset block + update comment - model_tools.py: remove rl_tools group + update async bridging comment - hermes_cli/tools_config.py: remove RL display entry, _DEFAULT_OFF_TOOLSETS, setup block, and rl_training post-setup handler - tools/budget_config.py: remove RL environment reference in docstring - tests/test_model_tools.py: remove rl_tools from expected groups - tests/run_agent/test_streaming_tool_call_repair.py: fix stale cross-reference * chore: remove rl/yc-bench extras and tinker-atropos refs from pyproject.toml - Remove rl extra (atroposlib, tinker, fastapi, uvicorn, wandb) - Remove yc-bench extra - Remove rl_cli from py-modules - Remove [tool.ty.src] exclude for tinker-atropos - Remove [tool.ruff] exclude for tinker-atropos - Regenerate uv.lock * chore: remove tinker-atropos from install/setup scripts - setup-hermes.sh: remove entire tinker-atropos submodule install block - scripts/install.sh: remove both tinker-atropos blocks (Termux + standard) - scripts/install.ps1: remove tinker-atropos block - nix/hermes-agent.nix: remove tinker-atropos pip install line * chore: remove RL references from cli-config.yaml.example * docs: remove Atropos/RL references from README, CONTRIBUTING, AGENTS.md * docs: remove RL/Atropos references from website - Delete: environments.md, rl-training.md, mlops-hermes-atropos-environments.md - sidebars.ts: remove rl-training and environments sidebar entries - optional-skills-catalog.md: remove hermes-atropos-environments row - tools-reference.md: remove entire rl toolset section - toolsets-reference.md: remove rl row + update example - integrations/index.md: remove RL Training bullet - architecture.md: remove environments/ from tree + RL section - contributing.md: remove tinker-atropos setup - updating.md: remove tinker-atropos install + stale submodule update * chore: remove remaining RL/Atropos stragglers - hermes_cli/config.py: remove TINKER_API_KEY + WANDB_API_KEY env var defs - hermes_cli/doctor.py: remove Submodules check section (tinker-atropos) - hermes_cli/setup.py: remove RL Training status check - hermes_cli/status.py: remove Tinker + WandB from API key status display - agent/display.py: remove both rl_* tool preview/activity blocks - website/docs: remove RL references from providers.md + env-variables.md - tests: remove TINKER_API_KEY from conftest, set_config_value, setup_script * chore: remove RL training section from .env.example")[#…](https://github.com/NousResearch/hermes-agent/pull/26106) | May 15, 2026 |
| [optional-skills](https://github.com/NousResearch/hermes-agent/tree/main/optional-skills "optional-skills") | [optional-skills](https://github.com/NousResearch/hermes-agent/tree/main/optional-skills "optional-skills") | [feat(skills): add osint-investigation optional skill (](https://github.com/NousResearch/hermes-agent/commit/5f91b1a48b06c8260dc539614abda27cf4e831cb "feat(skills): add osint-investigation optional skill (closes #355) (#26729) * feat(skills): add osint-investigation optional skill (closes #355) Phase-1 public-records OSINT investigation framework adapted from ShinMegamiBoson/OpenPlanter (MIT). Lives in optional-skills/research/. Six data-source wiki entries (FEC, SEC EDGAR, USAspending, Senate LD, OFAC SDN, ICIJ Offshore Leaks), each following the 9-section template: summary, access, schema, coverage, cross-reference keys, data quality, acquisition, legal, references. Six stdlib-only acquisition scripts that emit normalized CSV, plus three analysis scripts: - entity_resolution.py — three-tier match (exact / fuzzy / token overlap) with explicit confidence per row - timing_analysis.py — permutation test for donation/contract timing correlation, joins through cross-links - build_findings.py — assembles structured findings.json with evidence chains pointing back to source rows Validation: full pipeline runs end-to-end on synthetic fixtures. Entity resolution found 24 cross-matches with 0 false positives on a 5-row / 4-row test set. Timing analysis on 5 donations clustered near 3 awards returned p=0.000, effect size 2.41 SD. Findings JSON correctly tags HIGH-severity timing pattern. All 9 scripts pass --help and py_compile. Docs site page auto-generated by website/scripts/generate-skill-docs.py; sidebar + catalog entries updated by the same generator. * fix(osint-investigation): live API fixes from end-to-end sweep Live-tested the skill on a real public-citizen query and found three bugs the synthetic E2E missed. All three are now fixed and re-verified. 1. FEC fetch hung on contributor name searches. The combination of two_year_transaction_period + sort=date + contributor_name puts the OpenFEC query plan on a slow path that the upstream gateway times out (25s+). Switched to min_date/max_date with no explicit sort. Renamed --candidate to --contributor (the original name was misleading: FEC searches by donor, not by candidate; --candidate is kept as a deprecated alias). Added --state filter for narrowing. 2. ICIJ Offshore Leaks reconcile endpoint returns 404. ICIJ removed the Open Refine reconciliation API. Rewrote fetch_icij_offshore.py to download the official bulk CSV ZIP (~70 MB, public, no auth) and search it locally. Cached under $HERMES_OSINT_CACHE/icij/ (default ~/.cache/hermes-osint/icij/) for 30 days, --force-refresh to refetch. Verified live: 'PUTIN' query returns 5 Panama Papers officer matches in 0.5s after first download. 3. SEC EDGAR silently returned 0 when the company-name resolver matched an individual Form 3/4/5 filer (insider trading disclosures). Now surfaces 'Resolved company X → CIK Y (Z)' on stderr, prints a filing-type histogram when the type filter wipes results, and explicitly warns when the matched CIK appears to be an individual filer rather than a corporate registrant. Bonus: _http.py was retrying 429 responses with exponential backoff plus honoring (often-missing) Retry-After headers, which compounded into multi-second hangs per page when the upstream key was over quota. Changed to fail-fast on 429 with a clear, actionable error showing the upstream's quota message. Verified: 0.3s fast-fail vs the previous 60s hang on DEMO_KEY rate-limit exhaustion. Updated SKILL.md, fec.md, and icij-offshore.md to match the new CLI flags and ICIJ bulk-cache flow. Regenerated the docusaurus page via website/scripts/generate-skill-docs.py. Live sweep results across all 6 sources for 'Dillon Rolnick, New York': - OFAC SDN: 0 matches ✓ (correctly not sanctioned) - USAspending: 0 matches ✓ (correctly not a federal contractor) - Senate LDA: 0 matches ✓ (correctly not a lobbying client) - SEC EDGAR: warns it resolved to 'Rolnick Michael' (CIK 0001845264) who is an individual Form 3 filer, not a corporate registrant - ICIJ: 0 matches ✓ (correctly not in any offshore leak) - FEC: rate-limited (DEMO_KEY); fails fast with clear quota message * feat(osint-investigation): expand to 12 sources covering identity, property, courts, archives, news Phase-2 expansion per Teknium feedback that the original 6-source skill (federal financial/regulatory only) wasn't a complete OSINT toolkit. Adds 6 more sources covering the major omissions a real investigation would reach for first. New sources (6 fetch scripts + 6 wiki entries): 1. NYC ACRIS — Real property records (deeds, mortgages, liens) via the city's Socrata API. Search by party name or property address. Joins Parties to Master to populate doc_type, dates, borough, and amount. Coverage: 5 NYC boroughs, ~70M party records, 1966-present. 2. OpenCorporates — Global corporate registry covering 130+ jurisdictions (~200M companies). Free API token at https://opencorporates.com/api_accounts/new raises the rate limit; HTML fallback works without one (limited fields). 3. CourtListener (Free Law Project) — federal + state court opinions (~10M back to colonial era) + PACER dockets via RECAP. Anonymous v4 search works; COURTLISTENER_TOKEN raises rate limits. 4. Wayback Machine CDX — historical web captures (~900B+). Used both for surveillance-of-record (when did this site change?) and as a content-recovery layer when other sources point to dead URLs. 5. Wikipedia + Wikidata — narrative bio + structured facts. Wikipedia OpenSearch for article matching, REST summary for extracts, Wikidata Action API (wbgetentities) for claims. Avoids the SPARQL Query Service which is aggressively rate-limited. 6. GDELT 2.0 DOC API — global news monitoring in 100+ languages, ~2015-present. Auto-retries with 6s backoff on the standard 1-req-per-5-sec throttle. Other changes in this commit: - SEC EDGAR no longer raises SystemExit when the company-name resolver finds no CIK; writes an empty CSV with header so the rest of a pipeline can keep moving and the warning is just on stderr. - _http.py User-Agent updated per Wikimedia policy: includes app name, version, and a 'set HERMES_OSINT_UA to identify yourself' instruction. - SKILL.md workflow now groups sources into two clusters (federal financial vs identity/property/courts/archives/news) with bash examples for each. 'When to use this skill' lists the broader set of investigation patterns the expanded sources unlock. Live sweep results on 'Dillon Rolnick, New York' across all 12 sources: ofac ✓ 0 (correctly clean) icij ✓ 0 (correctly not in any leak) usaspending ✓ 0 (correctly not a federal contractor) senate_lda ✓ 0 (correctly not a lobbying client) sec_edgar ✓ 0, warns: resolved to 'Rolnick Michael' (CIK 0001845264), individual Form 3 filer, NOT a corporate registrant fec — rate-limited (DEMO_KEY exhausted), fails fast with clear quota message nyc_acris ✓ 200 records named Rolnick across NYC; 48 records at 571 Hudson (the property the web identifies as his) opencorporates ✓ 0 (no API token configured; HTML fallback) courtlistener ✓ 0 for 'Dillon Rolnick'; 20 for 'Rolnick' generally; 5 for 'Microsoft' sanity check wayback ✓ 30 captures of nousresearch.com from 2011-present wikipedia ✓ 0 (correctly not notable enough); Bill Gates sanity returns full structured facts (occupation, employer, DOB, place of birth, country) gdelt ✓ 0 for 'Dillon Rolnick'; 5 for 'Nous Research' All 17 scripts compile clean and pass --help. Synthetic analysis pipeline regression still passes (entity_resolution 30 matches, timing p=0.000, findings 2). * feat(osint-investigation): remove FEC; DEMO_KEY rate-limits make it unreliable The FEC fetcher consistently failed the live sweep because the OpenFEC DEMO_KEY tier (40 calls/hour) exhausts on a single investigation, and the upstream returns slow-path query plans for unindexed contributor-name searches that the gateway times out. Without a real API key it's not usable; with one the user has to sign up at api.data.gov first. That's too much setup friction for a skill that should work out of the box. Removed: - scripts/fetch_fec.py - references/sources/fec.md Updated: - SKILL.md frontmatter description + tags - 'When NOT to use' now points users at https://www.fec.gov/data/ for federal donations - entity_resolution example switched from donor↔contractor to lobbying-client↔contractor (Senate LDA + USAspending pair) - timing_analysis example switched to lobbying-filings vs awards - 8 wiki entries had their 'FEC ↔ ...' cross-reference bullets removed 11 sources remain (5 federal financial + 6 identity/property/courts/ archives/news). All scripts compile, pass --help, and the synthetic analysis pipeline still passes on the new lobbying-shaped regression fixture (30 matches, p=0.000 on tight clustering, 2 findings).")[closes](https://github.com/NousResearch/hermes-agent/commit/5f91b1a48b06c8260dc539614abda27cf4e831cb "feat(skills): add osint-investigation optional skill (closes #355) (#26729) * feat(skills): add osint-investigation optional skill (closes #355) Phase-1 public-records OSINT investigation framework adapted from ShinMegamiBoson/OpenPlanter (MIT). Lives in optional-skills/research/. Six data-source wiki entries (FEC, SEC EDGAR, USAspending, Senate LD, OFAC SDN, ICIJ Offshore Leaks), each following the 9-section template: summary, access, schema, coverage, cross-reference keys, data quality, acquisition, legal, references. Six stdlib-only acquisition scripts that emit normalized CSV, plus three analysis scripts: - entity_resolution.py — three-tier match (exact / fuzzy / token overlap) with explicit confidence per row - timing_analysis.py — permutation test for donation/contract timing correlation, joins through cross-links - build_findings.py — assembles structured findings.json with evidence chains pointing back to source rows Validation: full pipeline runs end-to-end on synthetic fixtures. Entity resolution found 24 cross-matches with 0 false positives on a 5-row / 4-row test set. Timing analysis on 5 donations clustered near 3 awards returned p=0.000, effect size 2.41 SD. Findings JSON correctly tags HIGH-severity timing pattern. All 9 scripts pass --help and py_compile. Docs site page auto-generated by website/scripts/generate-skill-docs.py; sidebar + catalog entries updated by the same generator. * fix(osint-investigation): live API fixes from end-to-end sweep Live-tested the skill on a real public-citizen query and found three bugs the synthetic E2E missed. All three are now fixed and re-verified. 1. FEC fetch hung on contributor name searches. The combination of two_year_transaction_period + sort=date + contributor_name puts the OpenFEC query plan on a slow path that the upstream gateway times out (25s+). Switched to min_date/max_date with no explicit sort. Renamed --candidate to --contributor (the original name was misleading: FEC searches by donor, not by candidate; --candidate is kept as a deprecated alias). Added --state filter for narrowing. 2. ICIJ Offshore Leaks reconcile endpoint returns 404. ICIJ removed the Open Refine reconciliation API. Rewrote fetch_icij_offshore.py to download the official bulk CSV ZIP (~70 MB, public, no auth) and search it locally. Cached under $HERMES_OSINT_CACHE/icij/ (default ~/.cache/hermes-osint/icij/) for 30 days, --force-refresh to refetch. Verified live: 'PUTIN' query returns 5 Panama Papers officer matches in 0.5s after first download. 3. SEC EDGAR silently returned 0 when the company-name resolver matched an individual Form 3/4/5 filer (insider trading disclosures). Now surfaces 'Resolved company X → CIK Y (Z)' on stderr, prints a filing-type histogram when the type filter wipes results, and explicitly warns when the matched CIK appears to be an individual filer rather than a corporate registrant. Bonus: _http.py was retrying 429 responses with exponential backoff plus honoring (often-missing) Retry-After headers, which compounded into multi-second hangs per page when the upstream key was over quota. Changed to fail-fast on 429 with a clear, actionable error showing the upstream's quota message. Verified: 0.3s fast-fail vs the previous 60s hang on DEMO_KEY rate-limit exhaustion. Updated SKILL.md, fec.md, and icij-offshore.md to match the new CLI flags and ICIJ bulk-cache flow. Regenerated the docusaurus page via website/scripts/generate-skill-docs.py. Live sweep results across all 6 sources for 'Dillon Rolnick, New York': - OFAC SDN: 0 matches ✓ (correctly not sanctioned) - USAspending: 0 matches ✓ (correctly not a federal contractor) - Senate LDA: 0 matches ✓ (correctly not a lobbying client) - SEC EDGAR: warns it resolved to 'Rolnick Michael' (CIK 0001845264) who is an individual Form 3 filer, not a corporate registrant - ICIJ: 0 matches ✓ (correctly not in any offshore leak) - FEC: rate-limited (DEMO_KEY); fails fast with clear quota message * feat(osint-investigation): expand to 12 sources covering identity, property, courts, archives, news Phase-2 expansion per Teknium feedback that the original 6-source skill (federal financial/regulatory only) wasn't a complete OSINT toolkit. Adds 6 more sources covering the major omissions a real investigation would reach for first. New sources (6 fetch scripts + 6 wiki entries): 1. NYC ACRIS — Real property records (deeds, mortgages, liens) via the city's Socrata API. Search by party name or property address. Joins Parties to Master to populate doc_type, dates, borough, and amount. Coverage: 5 NYC boroughs, ~70M party records, 1966-present. 2. OpenCorporates — Global corporate registry covering 130+ jurisdictions (~200M companies). Free API token at https://opencorporates.com/api_accounts/new raises the rate limit; HTML fallback works without one (limited fields). 3. CourtListener (Free Law Project) — federal + state court opinions (~10M back to colonial era) + PACER dockets via RECAP. Anonymous v4 search works; COURTLISTENER_TOKEN raises rate limits. 4. Wayback Machine CDX — historical web captures (~900B+). Used both for surveillance-of-record (when did this site change?) and as a content-recovery layer when other sources point to dead URLs. 5. Wikipedia + Wikidata — narrative bio + structured facts. Wikipedia OpenSearch for article matching, REST summary for extracts, Wikidata Action API (wbgetentities) for claims. Avoids the SPARQL Query Service which is aggressively rate-limited. 6. GDELT 2.0 DOC API — global news monitoring in 100+ languages, ~2015-present. Auto-retries with 6s backoff on the standard 1-req-per-5-sec throttle. Other changes in this commit: - SEC EDGAR no longer raises SystemExit when the company-name resolver finds no CIK; writes an empty CSV with header so the rest of a pipeline can keep moving and the warning is just on stderr. - _http.py User-Agent updated per Wikimedia policy: includes app name, version, and a 'set HERMES_OSINT_UA to identify yourself' instruction. - SKILL.md workflow now groups sources into two clusters (federal financial vs identity/property/courts/archives/news) with bash examples for each. 'When to use this skill' lists the broader set of investigation patterns the expanded sources unlock. Live sweep results on 'Dillon Rolnick, New York' across all 12 sources: ofac ✓ 0 (correctly clean) icij ✓ 0 (correctly not in any leak) usaspending ✓ 0 (correctly not a federal contractor) senate_lda ✓ 0 (correctly not a lobbying client) sec_edgar ✓ 0, warns: resolved to 'Rolnick Michael' (CIK 0001845264), individual Form 3 filer, NOT a corporate registrant fec — rate-limited (DEMO_KEY exhausted), fails fast with clear quota message nyc_acris ✓ 200 records named Rolnick across NYC; 48 records at 571 Hudson (the property the web identifies as his) opencorporates ✓ 0 (no API token configured; HTML fallback) courtlistener ✓ 0 for 'Dillon Rolnick'; 20 for 'Rolnick' generally; 5 for 'Microsoft' sanity check wayback ✓ 30 captures of nousresearch.com from 2011-present wikipedia ✓ 0 (correctly not notable enough); Bill Gates sanity returns full structured facts (occupation, employer, DOB, place of birth, country) gdelt ✓ 0 for 'Dillon Rolnick'; 5 for 'Nous Research' All 17 scripts compile clean and pass --help. Synthetic analysis pipeline regression still passes (entity_resolution 30 matches, timing p=0.000, findings 2). * feat(osint-investigation): remove FEC; DEMO_KEY rate-limits make it unreliable The FEC fetcher consistently failed the live sweep because the OpenFEC DEMO_KEY tier (40 calls/hour) exhausts on a single investigation, and the upstream returns slow-path query plans for unindexed contributor-name searches that the gateway times out. Without a real API key it's not usable; with one the user has to sign up at api.data.gov first. That's too much setup friction for a skill that should work out of the box. Removed: - scripts/fetch_fec.py - references/sources/fec.md Updated: - SKILL.md frontmatter description + tags - 'When NOT to use' now points users at https://www.fec.gov/data/ for federal donations - entity_resolution example switched from donor↔contractor to lobbying-client↔contractor (Senate LDA + USAspending pair) - timing_analysis example switched to lobbying-filings vs awards - 8 wiki entries had their 'FEC ↔ ...' cross-reference bullets removed 11 sources remain (5 federal financial + 6 identity/property/courts/ archives/news). All scripts compile, pass --help, and the synthetic analysis pipeline still passes on the new lobbying-shaped regression fixture (30 matches, p=0.000 on tight clustering, 2 findings).")[#355](https://github.com/NousResearch/hermes-agent/issues/355)[) (](https://github.com/NousResearch/hermes-agent/commit/5f91b1a48b06c8260dc539614abda27cf4e831cb "feat(skills): add osint-investigation optional skill (closes #355) (#26729) * feat(skills): add osint-investigation optional skill (closes #355) Phase-1 public-records OSINT investigation framework adapted from ShinMegamiBoson/OpenPlanter (MIT). Lives in optional-skills/research/. Six data-source wiki entries (FEC, SEC EDGAR, USAspending, Senate LD, OFAC SDN, ICIJ Offshore Leaks), each following the 9-section template: summary, access, schema, coverage, cross-reference keys, data quality, acquisition, legal, references. Six stdlib-only acquisition scripts that emit normalized CSV, plus three analysis scripts: - entity_resolution.py — three-tier match (exact / fuzzy / token overlap) with explicit confidence per row - timing_analysis.py — permutation test for donation/contract timing correlation, joins through cross-links - build_findings.py — assembles structured findings.json with evidence chains pointing back to source rows Validation: full pipeline runs end-to-end on synthetic fixtures. Entity resolution found 24 cross-matches with 0 false positives on a 5-row / 4-row test set. Timing analysis on 5 donations clustered near 3 awards returned p=0.000, effect size 2.41 SD. Findings JSON correctly tags HIGH-severity timing pattern. All 9 scripts pass --help and py_compile. Docs site page auto-generated by website/scripts/generate-skill-docs.py; sidebar + catalog entries updated by the same generator. * fix(osint-investigation): live API fixes from end-to-end sweep Live-tested the skill on a real public-citizen query and found three bugs the synthetic E2E missed. All three are now fixed and re-verified. 1. FEC fetch hung on contributor name searches. The combination of two_year_transaction_period + sort=date + contributor_name puts the OpenFEC query plan on a slow path that the upstream gateway times out (25s+). Switched to min_date/max_date with no explicit sort. Renamed --candidate to --contributor (the original name was misleading: FEC searches by donor, not by candidate; --candidate is kept as a deprecated alias). Added --state filter for narrowing. 2. ICIJ Offshore Leaks reconcile endpoint returns 404. ICIJ removed the Open Refine reconciliation API. Rewrote fetch_icij_offshore.py to download the official bulk CSV ZIP (~70 MB, public, no auth) and search it locally. Cached under $HERMES_OSINT_CACHE/icij/ (default ~/.cache/hermes-osint/icij/) for 30 days, --force-refresh to refetch. Verified live: 'PUTIN' query returns 5 Panama Papers officer matches in 0.5s after first download. 3. SEC EDGAR silently returned 0 when the company-name resolver matched an individual Form 3/4/5 filer (insider trading disclosures). Now surfaces 'Resolved company X → CIK Y (Z)' on stderr, prints a filing-type histogram when the type filter wipes results, and explicitly warns when the matched CIK appears to be an individual filer rather than a corporate registrant. Bonus: _http.py was retrying 429 responses with exponential backoff plus honoring (often-missing) Retry-After headers, which compounded into multi-second hangs per page when the upstream key was over quota. Changed to fail-fast on 429 with a clear, actionable error showing the upstream's quota message. Verified: 0.3s fast-fail vs the previous 60s hang on DEMO_KEY rate-limit exhaustion. Updated SKILL.md, fec.md, and icij-offshore.md to match the new CLI flags and ICIJ bulk-cache flow. Regenerated the docusaurus page via website/scripts/generate-skill-docs.py. Live sweep results across all 6 sources for 'Dillon Rolnick, New York': - OFAC SDN: 0 matches ✓ (correctly not sanctioned) - USAspending: 0 matches ✓ (correctly not a federal contractor) - Senate LDA: 0 matches ✓ (correctly not a lobbying client) - SEC EDGAR: warns it resolved to 'Rolnick Michael' (CIK 0001845264) who is an individual Form 3 filer, not a corporate registrant - ICIJ: 0 matches ✓ (correctly not in any offshore leak) - FEC: rate-limited (DEMO_KEY); fails fast with clear quota message * feat(osint-investigation): expand to 12 sources covering identity, property, courts, archives, news Phase-2 expansion per Teknium feedback that the original 6-source skill (federal financial/regulatory only) wasn't a complete OSINT toolkit. Adds 6 more sources covering the major omissions a real investigation would reach for first. New sources (6 fetch scripts + 6 wiki entries): 1. NYC ACRIS — Real property records (deeds, mortgages, liens) via the city's Socrata API. Search by party name or property address. Joins Parties to Master to populate doc_type, dates, borough, and amount. Coverage: 5 NYC boroughs, ~70M party records, 1966-present. 2. OpenCorporates — Global corporate registry covering 130+ jurisdictions (~200M companies). Free API token at https://opencorporates.com/api_accounts/new raises the rate limit; HTML fallback works without one (limited fields). 3. CourtListener (Free Law Project) — federal + state court opinions (~10M back to colonial era) + PACER dockets via RECAP. Anonymous v4 search works; COURTLISTENER_TOKEN raises rate limits. 4. Wayback Machine CDX — historical web captures (~900B+). Used both for surveillance-of-record (when did this site change?) and as a content-recovery layer when other sources point to dead URLs. 5. Wikipedia + Wikidata — narrative bio + structured facts. Wikipedia OpenSearch for article matching, REST summary for extracts, Wikidata Action API (wbgetentities) for claims. Avoids the SPARQL Query Service which is aggressively rate-limited. 6. GDELT 2.0 DOC API — global news monitoring in 100+ languages, ~2015-present. Auto-retries with 6s backoff on the standard 1-req-per-5-sec throttle. Other changes in this commit: - SEC EDGAR no longer raises SystemExit when the company-name resolver finds no CIK; writes an empty CSV with header so the rest of a pipeline can keep moving and the warning is just on stderr. - _http.py User-Agent updated per Wikimedia policy: includes app name, version, and a 'set HERMES_OSINT_UA to identify yourself' instruction. - SKILL.md workflow now groups sources into two clusters (federal financial vs identity/property/courts/archives/news) with bash examples for each. 'When to use this skill' lists the broader set of investigation patterns the expanded sources unlock. Live sweep results on 'Dillon Rolnick, New York' across all 12 sources: ofac ✓ 0 (correctly clean) icij ✓ 0 (correctly not in any leak) usaspending ✓ 0 (correctly not a federal contractor) senate_lda ✓ 0 (correctly not a lobbying client) sec_edgar ✓ 0, warns: resolved to 'Rolnick Michael' (CIK 0001845264), individual Form 3 filer, NOT a corporate registrant fec — rate-limited (DEMO_KEY exhausted), fails fast with clear quota message nyc_acris ✓ 200 records named Rolnick across NYC; 48 records at 571 Hudson (the property the web identifies as his) opencorporates ✓ 0 (no API token configured; HTML fallback) courtlistener ✓ 0 for 'Dillon Rolnick'; 20 for 'Rolnick' generally; 5 for 'Microsoft' sanity check wayback ✓ 30 captures of nousresearch.com from 2011-present wikipedia ✓ 0 (correctly not notable enough); Bill Gates sanity returns full structured facts (occupation, employer, DOB, place of birth, country) gdelt ✓ 0 for 'Dillon Rolnick'; 5 for 'Nous Research' All 17 scripts compile clean and pass --help. Synthetic analysis pipeline regression still passes (entity_resolution 30 matches, timing p=0.000, findings 2). * feat(osint-investigation): remove FEC; DEMO_KEY rate-limits make it unreliable The FEC fetcher consistently failed the live sweep because the OpenFEC DEMO_KEY tier (40 calls/hour) exhausts on a single investigation, and the upstream returns slow-path query plans for unindexed contributor-name searches that the gateway times out. Without a real API key it's not usable; with one the user has to sign up at api.data.gov first. That's too much setup friction for a skill that should work out of the box. Removed: - scripts/fetch_fec.py - references/sources/fec.md Updated: - SKILL.md frontmatter description + tags - 'When NOT to use' now points users at https://www.fec.gov/data/ for federal donations - entity_resolution example switched from donor↔contractor to lobbying-client↔contractor (Senate LDA + USAspending pair) - timing_analysis example switched to lobbying-filings vs awards - 8 wiki entries had their 'FEC ↔ ...' cross-reference bullets removed 11 sources remain (5 federal financial + 6 identity/property/courts/ archives/news). All scripts compile, pass --help, and the synthetic analysis pipeline still passes on the new lobbying-shaped regression fixture (30 matches, p=0.000 on tight clustering, 2 findings).")[#…](https://github.com/NousResearch/hermes-agent/pull/26729) | May 16, 2026 |
| [packaging/homebrew](https://github.com/NousResearch/hermes-agent/tree/main/packaging/homebrew "This path skips through empty directories") | [packaging/homebrew](https://github.com/NousResearch/hermes-agent/tree/main/packaging/homebrew "This path skips through empty directories") | [chore: prepare Hermes for Homebrew packaging (](https://github.com/NousResearch/hermes-agent/commit/e64b047663a0ff95753a1bf930036e6ccca43bd2 "chore: prepare Hermes for Homebrew packaging (#4099) Co-authored-by: Yabuku-xD <78594762+Yabuku-xD@users.noreply.github.com>")[#4099](https://github.com/NousResearch/hermes-agent/pull/4099)[)](https://github.com/NousResearch/hermes-agent/commit/e64b047663a0ff95753a1bf930036e6ccca43bd2 "chore: prepare Hermes for Homebrew packaging (#4099) Co-authored-by: Yabuku-xD <78594762+Yabuku-xD@users.noreply.github.com>") | Mar 31, 2026 |
| [plans](https://github.com/NousResearch/hermes-agent/tree/main/plans "plans") | [plans](https://github.com/NousResearch/hermes-agent/tree/main/plans "plans") | [fix(gemini): tighten native routing and streaming replay](https://github.com/NousResearch/hermes-agent/commit/d393104bad62700d8e33de003502b3f74854151a "fix(gemini): tighten native routing and streaming replay - only use the native adapter for the canonical Gemini native endpoint - keep custom and /openai base URLs on the OpenAI-compatible path - preserve Hermes keepalive transport injection for native Gemini clients - stabilize streaming tool-call replay across repeated SSE events - add follow-up tests for base_url precedence, async streaming, and duplicate tool-call chunks") | Apr 19, 2026 |
| [plugins](https://github.com/NousResearch/hermes-agent/tree/main/plugins "plugins") | [plugins](https://github.com/NousResearch/hermes-agent/tree/main/plugins "plugins") | [fix(line): add trust_env=True to all _LineClient aiohttp sessions](https://github.com/NousResearch/hermes-agent/commit/35b7befc67315da5d4ce6b6a3daa4d9ba2f57c1c "fix(line): add trust_env=True to all _LineClient aiohttp sessions _LineClient's five aiohttp.ClientSession() calls omit trust_env=True, silently bypassing HTTP_PROXY / HTTPS_PROXY / ALL_PROXY. Result: every LINE API call (reply, push, loading, fetch_content, get_bot_user_id) ignores the system proxy. Fix: add trust_env=True to all five session constructions. Symmetric with the wecom and weixin adapters which already set this flag. No behavior change for users not behind a proxy.") | May 17, 2026 |
| [providers](https://github.com/NousResearch/hermes-agent/tree/main/providers "providers") | [providers](https://github.com/NousResearch/hermes-agent/tree/main/providers "providers") | [fix(providers): set User-Agent on ProviderProfile.fetch_models](https://github.com/NousResearch/hermes-agent/commit/5360b542447daaf0ba8d0f7c3cf0be1751ca0008 "fix(providers): set User-Agent on ProviderProfile.fetch_models Some catalog endpoints (OpenCode Zen, etc.) sit behind a WAF that returns 403 for the default Python-urllib/<ver> User-Agent. The generic profile-based live fetch in providers/base.py was silently failing for any such provider — falling through to the static catalog and missing newly-launched models. Set a generic 'hermes-cli/<version>' UA on the catalog probe so every api_key provider profile benefits. Verified live against opencode-zen: before this change, profile.fetch_models() raised HTTP 403; after, it returns 42 models including gpt-5.5, gpt-5.5-pro, kimi-k2.6, glm-5.1 and the *-free variants the static catalog doesn't list. Also strip the now-stale comment in validate_requested_model() claiming opencode-zen's /models returns 404 against the HTML marketing site — the API endpoint at /zen/v1/models returns 200 with valid JSON. Surfaced by #2651 (@aashizpoudel) — fixes the same user-facing gap their PR targeted, applied at the right layer so all api_key provider profiles get live catalogs through the same code path. Co-authored-by: Aashish Poudel <mr.aashiz@gmail.com>") | May 15, 2026 |
| [scripts](https://github.com/NousResearch/hermes-agent/tree/main/scripts "scripts") | [scripts](https://github.com/NousResearch/hermes-agent/tree/main/scripts "scripts") | [chore(release): AUTHOR_MAP entries for batch salvage group 4 contribu…](https://github.com/NousResearch/hermes-agent/commit/7322816efa601737722c74147194f1f5ffd3ad07 "chore(release): AUTHOR_MAP entries for batch salvage group 4 contributors Adds release-note attribution mappings for 9 contributors from group 4: - @EloquentBrush0x (PR #26657) - @subtract0 (PR #25658) - @zwolniony (PR #26961) - @that-ambuj (PR #26582) - @zccyman (PR #25294) - @lidge-jun (PR #26814) - @phoenixshen (PR #26768) - @AhmetArif0 (PR #26635) - (francip already mapped from prior PR #26134 attribution) #27147 dropped from this batch — already landed on main as 4b17c2411.") | May 17, 2026 |
| [skills](https://github.com/NousResearch/hermes-agent/tree/main/skills "skills") | [skills](https://github.com/NousResearch/hermes-agent/tree/main/skills "skills") | [feat(skills/notion): overhaul for Notion Developer Platform (May 2026) (](https://github.com/NousResearch/hermes-agent/commit/42070ecefb9e9da3adec6d536d130d9dc3b82560 "feat(skills/notion): overhaul for Notion Developer Platform (May 2026) (#26612) * feat(skills/notion): overhaul for Notion Developer Platform (May 2026) Notion shipped its Developer Platform on May 13, 2026: ntn CLI, Workers, Markdown API, bidirectional webhooks, agent tools. The existing skill only covered curl + integration token CRUD, so it didn't surface any of the new ergonomics — particularly the /markdown endpoints (much easier for agents to consume) and the ntn CLI for headless API + Workers management. This rewrite (v1.0.0 -> v2.0.0): - Splits setup into Path A (HTTP, cross-platform incl. Windows), Path B (ntn CLI on macOS/Linux, with NOTION_API_TOKEN env var for headless), and Path C (Windows fallback — HTTP API or WSL2; native ntn is 'coming soon'). - Keeps the full curl reference (still the only Windows-compatible path). - Adds /markdown endpoints — GET and PATCH page-as-markdown, plus POST /v1/pages with a markdown body param. Agent-friendly, no CLI required. - Adds ntn CLI cheat sheet for raw API shorthand, file uploads, and workspace flags. - Adds Notion Workers section: scaffold, tool/webhook capability shapes, lifecycle commands. Gated on Business/Enterprise plans + macOS/Linux. - Adds Notion-flavored Markdown reference (callouts, toggles, columns, mentions, colors) for the /markdown endpoints. - Adds a 'choose the right path' decision table at the bottom. - Notes the new efficient Notion MCP server as an optional wiring path. Auto-generated docs page regenerated via website/scripts/generate-skill-docs.py. * docs(skills-catalog): update notion description for v2.0.0") | May 15, 2026 |
| [tests](https://github.com/NousResearch/hermes-agent/tree/main/tests "tests") | [tests](https://github.com/NousResearch/hermes-agent/tree/main/tests "tests") | [fix(matrix): warn on clock-skew silent message drops (](https://github.com/NousResearch/hermes-agent/commit/519657aa98d4969ec9e23c70c074d1982ef3ccf1 "fix(matrix): warn on clock-skew silent message drops (#12614) (#27330) The 5-second startup-grace filter in _on_room_message silently drops events where event_ts < startup_ts - 5. When the host clock is set ahead of real time, the comparison flips against every live event and the bot 'connects but never replies' — exactly the symptom in #12614. Reporter Schnurzel700 chased this for several weeks before tracing it to their Debian VM's clock being out of sync. The current /1000.0 millisecond->second conversion is correct (mautrix returns ms); the failure mode is purely environmental. Add a one-shot WARNING that fires when: - we are >30s past startup (initial-sync replay window closed), AND - 3 consecutive drops share the same skew within 60s (a constant clock offset, not varied-age backfill from an invited room). State is reset in connect() so reconnects after fixing NTP rearm the detector. Includes the NTP fix instruction in the warning message itself and a new Troubleshooting entry in the Matrix docs. 5 new tests cover the happy path, initial-sync backfill, under- threshold drops, varied-age backfill, and the reconnect rearm path.")[#12614](https://github.com/NousResearch/hermes-agent/issues/12614)[) (](https://github.com/NousResearch/hermes-agent/commit/519657aa98d4969ec9e23c70c074d1982ef3ccf1 "fix(matrix): warn on clock-skew silent message drops (#12614) (#27330) The 5-second startup-grace filter in _on_room_message silently drops events where event_ts < startup_ts - 5. When the host clock is set ahead of real time, the comparison flips against every live event and the bot 'connects but never replies' — exactly the symptom in #12614. Reporter Schnurzel700 chased this for several weeks before tracing it to their Debian VM's clock being out of sync. The current /1000.0 millisecond->second conversion is correct (mautrix returns ms); the failure mode is purely environmental. Add a one-shot WARNING that fires when: - we are >30s past startup (initial-sync replay window closed), AND - 3 consecutive drops share the same skew within 60s (a constant clock offset, not varied-age backfill from an invited room). State is reset in connect() so reconnects after fixing NTP rearm the detector. Includes the NTP fix instruction in the warning message itself and a new Troubleshooting entry in the Matrix docs. 5 new tests cover the happy path, initial-sync backfill, under- threshold drops, varied-age backfill, and the reconnect rearm path.")[#27330](https://github.com/NousResearch/hermes-agent/pull/27330)[)](https://github.com/NousResearch/hermes-agent/commit/519657aa98d4969ec9e23c70c074d1982ef3ccf1 "fix(matrix): warn on clock-skew silent message drops (#12614) (#27330) The 5-second startup-grace filter in _on_room_message silently drops events where event_ts < startup_ts - 5. When the host clock is set ahead of real time, the comparison flips against every live event and the bot 'connects but never replies' — exactly the symptom in #12614. Reporter Schnurzel700 chased this for several weeks before tracing it to their Debian VM's clock being out of sync. The current /1000.0 millisecond->second conversion is correct (mautrix returns ms); the failure mode is purely environmental. Add a one-shot WARNING that fires when: - we are >30s past startup (initial-sync replay window closed), AND - 3 consecutive drops share the same skew within 60s (a constant clock offset, not varied-age backfill from an invited room). State is reset in connect() so reconnects after fixing NTP rearm the detector. Includes the NTP fix instruction in the warning message itself and a new Troubleshooting entry in the Matrix docs. 5 new tests cover the happy path, initial-sync backfill, under- threshold drops, varied-age backfill, and the reconnect rearm path.") | May 17, 2026 |
| [tools](https://github.com/NousResearch/hermes-agent/tree/main/tools "tools") | [tools](https://github.com/NousResearch/hermes-agent/tree/main/tools "tools") | [fix(windows): suppress console window flash on subprocess spawns](https://github.com/NousResearch/hermes-agent/commit/8bf09455dc498581fe6dea21402ee2a9238a2212 "fix(windows): suppress console window flash on subprocess spawns Add creationflags=CREATE_NO_WINDOW to every Windows Popen call across the terminal, process registry, code execution, and kanban worker subsystems. Prevents visible CMD windows from flashing on the user's desktop during agent operation. Also adds the _IS_WINDOWS module constant to kanban_db.py where it was missing, for consistency with the other patched files. 5 Popen sites across 4 files: - tools/environments/local.py (terminal foreground spawn) - tools/process_registry.py (background process spawn) - tools/code_execution_tool.py (sandbox + interpreter probe) - hermes_cli/kanban_db.py (kanban worker spawn)") | May 17, 2026 |
| [tui_gateway](https://github.com/NousResearch/hermes-agent/tree/main/tui_gateway "tui_gateway") | [tui_gateway](https://github.com/NousResearch/hermes-agent/tree/main/tui_gateway "tui_gateway") | [fix(async): close unscheduled coroutines in all threadsafe bridges (](https://github.com/NousResearch/hermes-agent/commit/4e89c53082b13b71d0c7f2f662cd65ea80d9f17c "fix(async): close unscheduled coroutines in all threadsafe bridges (#26584) Wraps every sync->async coroutine-scheduling site in the codebase with a new agent.async_utils.safe_schedule_threadsafe() helper that closes the coroutine on scheduling failure (closed loop, shutdown race, etc.) instead of leaking it as 'coroutine was never awaited' RuntimeWarnings plus reference leaks. 22 production call sites migrated across the codebase: - acp_adapter/events.py, acp_adapter/permissions.py - agent/lsp/manager.py - cron/scheduler.py (media + text delivery paths) - gateway/platforms/feishu.py (5 sites, via existing _submit_on_loop helper which now delegates to safe_schedule_threadsafe) - gateway/run.py (10 sites: telegram rename, agent:step hook, status callback, interim+bg-review, clarify send, exec-approval button+text, temp-bubble cleanup, channel-directory refresh) - plugins/memory/hindsight, plugins/platforms/google_chat - tools/browser_supervisor.py (3), browser_cdp_tool.py, computer_use/cua_backend.py, slash_confirm.py - tools/environments/modal.py (_AsyncWorker) - tools/mcp_tool.py (2 + 8 _run_on_mcp_loop callers converted to factory-style so the coroutine is never constructed on a dead loop) - tui_gateway/ws.py Tests: new tests/agent/test_async_utils.py covers helper behavior under live loop, dead loop, None loop, and scheduling exceptions. Regression tests added at three PR-original sites (acp events, acp permissions, mcp loop runner) mirroring contributor's intent. Live-tested end-to-end: - Helper stress test: 1500 schedules across live/dead/race scenarios, zero leaked coroutines - Race exercised: 5000 schedules with loop killed mid-flight, 100 ok / 4900 None returns, zero leaks - hermes chat -q with terminal tool call (exercises step_callback bridge) - MCP probe against failing subprocess servers + factory path - Real gateway daemon boot + SIGINT shutdown across multiple platform adapter inits - WSTransport 100 live + 50 dead-loop writes - Cron delivery path live + dead loop Salvages PR #2657 — adopts contributor's intent over a much wider site list and a single centralized helper instead of inline try/except at each site. 3 of the original PR's 6 sites no longer exist on main (environments/patches.py deleted, DingTalk refactored to native async); the equivalent fix lives in tools/environments/modal.py instead. Co-authored-by: JithendraNara <jithendranaidunara@gmail.com>")[#…](https://github.com/NousResearch/hermes-agent/pull/26584) | May 15, 2026 |
| [ui-tui](https://github.com/NousResearch/hermes-agent/tree/main/ui-tui "ui-tui") | [ui-tui](https://github.com/NousResearch/hermes-agent/tree/main/ui-tui "ui-tui") | [fix(review): address Copilot follow-up on sanitizer and file decode e…](https://github.com/NousResearch/hermes-agent/commit/a65f723e6847f8d326947011b0d6d345d240ce25 "fix(review): address Copilot follow-up on sanitizer and file decode errors Consume multi-byte non-CSI ESC sequences during ANSI sanitization and handle UnicodeDecodeError for `hermes send --file` so review findings are resolved without regressions.") | May 17, 2026 |
| [web](https://github.com/NousResearch/hermes-agent/tree/main/web "web") | [web](https://github.com/NousResearch/hermes-agent/tree/main/web "web") | [fix(dashboard): align Ukrainian Kanban Ready column help](https://github.com/NousResearch/hermes-agent/commit/ca413c6164e7957d33841353feb9cdbf838dead7 "fix(dashboard): align Ukrainian Kanban Ready column help Mirrors the dependency-ready / assign-profile semantics used in other locales; Copilot review noted uk.ts was still on the old dispatcher-tick wording. Co-authored-by: Cursor <cursoragent@cursor.com>") | May 16, 2026 |
| [website](https://github.com/NousResearch/hermes-agent/tree/main/website "website") | [website](https://github.com/NousResearch/hermes-agent/tree/main/website "website") | [fix(matrix): warn on clock-skew silent message drops (](https://github.com/NousResearch/hermes-agent/commit/519657aa98d4969ec9e23c70c074d1982ef3ccf1 "fix(matrix): warn on clock-skew silent message drops (#12614) (#27330) The 5-second startup-grace filter in _on_room_message silently drops events where event_ts < startup_ts - 5. When the host clock is set ahead of real time, the comparison flips against every live event and the bot 'connects but never replies' — exactly the symptom in #12614. Reporter Schnurzel700 chased this for several weeks before tracing it to their Debian VM's clock being out of sync. The current /1000.0 millisecond->second conversion is correct (mautrix returns ms); the failure mode is purely environmental. Add a one-shot WARNING that fires when: - we are >30s past startup (initial-sync replay window closed), AND - 3 consecutive drops share the same skew within 60s (a constant clock offset, not varied-age backfill from an invited room). State is reset in connect() so reconnects after fixing NTP rearm the detector. Includes the NTP fix instruction in the warning message itself and a new Troubleshooting entry in the Matrix docs. 5 new tests cover the happy path, initial-sync backfill, under- threshold drops, varied-age backfill, and the reconnect rearm path.")[#12614](https://github.com/NousResearch/hermes-agent/issues/12614)[) (](https://github.com/NousResearch/hermes-agent/commit/519657aa98d4969ec9e23c70c074d1982ef3ccf1 "fix(matrix): warn on clock-skew silent message drops (#12614) (#27330) The 5-second startup-grace filter in _on_room_message silently drops events where event_ts < startup_ts - 5. When the host clock is set ahead of real time, the comparison flips against every live event and the bot 'connects but never replies' — exactly the symptom in #12614. Reporter Schnurzel700 chased this for several weeks before tracing it to their Debian VM's clock being out of sync. The current /1000.0 millisecond->second conversion is correct (mautrix returns ms); the failure mode is purely environmental. Add a one-shot WARNING that fires when: - we are >30s past startup (initial-sync replay window closed), AND - 3 consecutive drops share the same skew within 60s (a constant clock offset, not varied-age backfill from an invited room). State is reset in connect() so reconnects after fixing NTP rearm the detector. Includes the NTP fix instruction in the warning message itself and a new Troubleshooting entry in the Matrix docs. 5 new tests cover the happy path, initial-sync backfill, under- threshold drops, varied-age backfill, and the reconnect rearm path.")[#27330](https://github.com/NousResearch/hermes-agent/pull/27330)[)](https://github.com/NousResearch/hermes-agent/commit/519657aa98d4969ec9e23c70c074d1982ef3ccf1 "fix(matrix): warn on clock-skew silent message drops (#12614) (#27330) The 5-second startup-grace filter in _on_room_message silently drops events where event_ts < startup_ts - 5. When the host clock is set ahead of real time, the comparison flips against every live event and the bot 'connects but never replies' — exactly the symptom in #12614. Reporter Schnurzel700 chased this for several weeks before tracing it to their Debian VM's clock being out of sync. The current /1000.0 millisecond->second conversion is correct (mautrix returns ms); the failure mode is purely environmental. Add a one-shot WARNING that fires when: - we are >30s past startup (initial-sync replay window closed), AND - 3 consecutive drops share the same skew within 60s (a constant clock offset, not varied-age backfill from an invited room). State is reset in connect() so reconnects after fixing NTP rearm the detector. Includes the NTP fix instruction in the warning message itself and a new Troubleshooting entry in the Matrix docs. 5 new tests cover the happy path, initial-sync backfill, under- threshold drops, varied-age backfill, and the reconnect rearm path.") | May 17, 2026 |
| [.dockerignore](https://github.com/NousResearch/hermes-agent/blob/main/.dockerignore ".dockerignore") | [.dockerignore](https://github.com/NousResearch/hermes-agent/blob/main/.dockerignore ".dockerignore") | [fix(docker): exclude compose/profile runtime state from build context](https://github.com/NousResearch/hermes-agent/commit/d7663c78083aff9df70349f36c587ebfc2c3aa59 "fix(docker): exclude compose/profile runtime state from build context") | May 4, 2026 |
| [.env.example](https://github.com/NousResearch/hermes-agent/blob/main/.env.example ".env.example") | [.env.example](https://github.com/NousResearch/hermes-agent/blob/main/.env.example ".env.example") | [chore: remove Atropos RL environments and tinker-atropos integration (](https://github.com/NousResearch/hermes-agent/commit/5af672c7530263544a9f5e2479f3853d83b3b798 "chore: remove Atropos RL environments and tinker-atropos integration (#26106) * chore: remove Atropos RL environments, tools, tests, skill, and tinker-atropos submodule Delete: - environments/ (43 files — base env, agent loop, tool call parsers, benchmarks) - rl_cli.py (standalone RL training CLI) - tools/rl_training_tool.py (all 10 rl_* tools) - tests: test_rl_training_tool, test_tool_call_parsers, test_managed_server_tool_support, test_agent_loop, test_agent_loop_vllm, test_agent_loop_tool_calling, test_terminalbench2_env_security - optional-skills/mlops/hermes-atropos-environments/ - tinker-atropos git submodule + .gitmodules * chore: remove RL/Atropos references from Python source - toolsets.py: remove rl toolset block + update comment - model_tools.py: remove rl_tools group + update async bridging comment - hermes_cli/tools_config.py: remove RL display entry, _DEFAULT_OFF_TOOLSETS, setup block, and rl_training post-setup handler - tools/budget_config.py: remove RL environment reference in docstring - tests/test_model_tools.py: remove rl_tools from expected groups - tests/run_agent/test_streaming_tool_call_repair.py: fix stale cross-reference * chore: remove rl/yc-bench extras and tinker-atropos refs from pyproject.toml - Remove rl extra (atroposlib, tinker, fastapi, uvicorn, wandb) - Remove yc-bench extra - Remove rl_cli from py-modules - Remove [tool.ty.src] exclude for tinker-atropos - Remove [tool.ruff] exclude for tinker-atropos - Regenerate uv.lock * chore: remove tinker-atropos from install/setup scripts - setup-hermes.sh: remove entire tinker-atropos submodule install block - scripts/install.sh: remove both tinker-atropos blocks (Termux + standard) - scripts/install.ps1: remove tinker-atropos block - nix/hermes-agent.nix: remove tinker-atropos pip install line * chore: remove RL references from cli-config.yaml.example * docs: remove Atropos/RL references from README, CONTRIBUTING, AGENTS.md * docs: remove RL/Atropos references from website - Delete: environments.md, rl-training.md, mlops-hermes-atropos-environments.md - sidebars.ts: remove rl-training and environments sidebar entries - optional-skills-catalog.md: remove hermes-atropos-environments row - tools-reference.md: remove entire rl toolset section - toolsets-reference.md: remove rl row + update example - integrations/index.md: remove RL Training bullet - architecture.md: remove environments/ from tree + RL section - contributing.md: remove tinker-atropos setup - updating.md: remove tinker-atropos install + stale submodule update * chore: remove remaining RL/Atropos stragglers - hermes_cli/config.py: remove TINKER_API_KEY + WANDB_API_KEY env var defs - hermes_cli/doctor.py: remove Submodules check section (tinker-atropos) - hermes_cli/setup.py: remove RL Training status check - hermes_cli/status.py: remove Tinker + WandB from API key status display - agent/display.py: remove both rl_* tool preview/activity blocks - website/docs: remove RL references from providers.md + env-variables.md - tests: remove TINKER_API_KEY from conftest, set_config_value, setup_script * chore: remove RL training section from .env.example")[#…](https://github.com/NousResearch/hermes-agent/pull/26106) | May 15, 2026 |
| [.envrc](https://github.com/NousResearch/hermes-agent/blob/main/.envrc ".envrc") | [.envrc](https://github.com/NousResearch/hermes-agent/blob/main/.envrc ".envrc") | [nix: add tui lockfile update script](https://github.com/NousResearch/hermes-agent/commit/658cd2dd4ccb47c318897d90d7ddc535395f683d "nix: add tui lockfile update script") | Apr 10, 2026 |
| [.gitattributes](https://github.com/NousResearch/hermes-agent/blob/main/.gitattributes ".gitattributes") | [.gitattributes](https://github.com/NousResearch/hermes-agent/blob/main/.gitattributes ".gitattributes") | [feat: web UI dashboard for managing Hermes Agent (](https://github.com/NousResearch/hermes-agent/commit/e2a9b5369f60ca9f7e15052481cf160d4b19e66b "feat: web UI dashboard for managing Hermes Agent (#8756) * feat: web UI dashboard for managing Hermes Agent (salvage of #8204/#7621) Adds an embedded web UI dashboard accessible via `hermes web`: - Status page: agent version, active sessions, gateway status, connected platforms - Config editor: schema-driven form with tabbed categories, import/export, reset - API Keys page: set, clear, and view redacted values with category grouping - Sessions, Skills, Cron, Logs, and Analytics pages Backend: - hermes_cli/web_server.py: FastAPI server with REST endpoints - hermes_cli/config.py: reload_env() utility for hot-reloading .env - hermes_cli/main.py: `hermes web` subcommand (--port, --host, --no-open) - cli.py / commands.py: /reload slash command for .env hot-reload - pyproject.toml: [web] optional dependency extra (fastapi + uvicorn) - Both update paths (git + zip) auto-build web frontend when npm available Frontend: - Vite + React + TypeScript + Tailwind v4 SPA in web/ - shadcn/ui-style components, Nous design language - Auto-refresh status page, toast notifications, masked password inputs Security: - Path traversal guard (resolve().is_relative_to()) on SPA file serving - CORS localhost-only via allow_origin_regex - Generic error messages (no internal leak), SessionDB handles closed properly Tests: 47 tests covering reload_env, redact_key, API endpoints, schema generation, path traversal, category merging, internal key stripping, and full config round-trip. Original work by @austinpickett (PR #1813), salvaged by @kshitijk4poor (PR #7621 → #8204), re-salvaged onto current main with stale-branch regressions removed. * fix(web): clean up status page cards, always rebuild on `hermes web` - Remove config version migration alert banner from status page - Remove config version card (internal noise, not surfaced in TUI) - Reorder status cards: Agent → Gateway → Active Sessions (3-col grid) - `hermes web` now always rebuilds from source before serving, preventing stale web_dist when editing frontend files * feat(web): full-text search across session messages - Add GET /api/sessions/search endpoint backed by FTS5 - Auto-append prefix wildcards so partial words match (e.g. 'nimb' → 'nimby') - Debounced search (300ms) with spinner in the search icon slot - Search results show FTS5 snippets with highlighted match delimiters - Expanding a search hit auto-scrolls to the first matching message - Matching messages get a warning ring + 'match' badge - Inline term highlighting within Markdown (text, bold, italic, headings, lists) - Clear button (x) on search input for quick reset --------- Co-authored-by: emozilla <emozilla@nousresearch.com>")[#8756](https://github.com/NousResearch/hermes-agent/pull/8756)[)](https://github.com/NousResearch/hermes-agent/commit/e2a9b5369f60ca9f7e15052481cf160d4b19e66b "feat: web UI dashboard for managing Hermes Agent (#8756) * feat: web UI dashboard for managing Hermes Agent (salvage of #8204/#7621) Adds an embedded web UI dashboard accessible via `hermes web`: - Status page: agent version, active sessions, gateway status, connected platforms - Config editor: schema-driven form with tabbed categories, import/export, reset - API Keys page: set, clear, and view redacted values with category grouping - Sessions, Skills, Cron, Logs, and Analytics pages Backend: - hermes_cli/web_server.py: FastAPI server with REST endpoints - hermes_cli/config.py: reload_env() utility for hot-reloading .env - hermes_cli/main.py: `hermes web` subcommand (--port, --host, --no-open) - cli.py / commands.py: /reload slash command for .env hot-reload - pyproject.toml: [web] optional dependency extra (fastapi + uvicorn) - Both update paths (git + zip) auto-build web frontend when npm available Frontend: - Vite + React + TypeScript + Tailwind v4 SPA in web/ - shadcn/ui-style components, Nous design language - Auto-refresh status page, toast notifications, masked password inputs Security: - Path traversal guard (resolve().is_relative_to()) on SPA file serving - CORS localhost-only via allow_origin_regex - Generic error messages (no internal leak), SessionDB handles closed properly Tests: 47 tests covering reload_env, redact_key, API endpoints, schema generation, path traversal, category merging, internal key stripping, and full config round-trip. Original work by @austinpickett (PR #1813), salvaged by @kshitijk4poor (PR #7621 → #8204), re-salvaged onto current main with stale-branch regressions removed. * fix(web): clean up status page cards, always rebuild on `hermes web` - Remove config version migration alert banner from status page - Remove config version card (internal noise, not surfaced in TUI) - Reorder status cards: Agent → Gateway → Active Sessions (3-col grid) - `hermes web` now always rebuilds from source before serving, preventing stale web_dist when editing frontend files * feat(web): full-text search across session messages - Add GET /api/sessions/search endpoint backed by FTS5 - Auto-append prefix wildcards so partial words match (e.g. 'nimb' → 'nimby') - Debounced search (300ms) with spinner in the search icon slot - Search results show FTS5 snippets with highlighted match delimiters - Expanding a search hit auto-scrolls to the first matching message - Matching messages get a warning ring + 'match' badge - Inline term highlighting within Markdown (text, bold, italic, headings, lists) - Clear button (x) on search input for quick reset --------- Co-authored-by: emozilla <emozilla@nousresearch.com>") | Apr 13, 2026 |
| [.gitignore](https://github.com/NousResearch/hermes-agent/blob/main/.gitignore ".gitignore") | [.gitignore](https://github.com/NousResearch/hermes-agent/blob/main/.gitignore ".gitignore") | [chore: gitignore hermes_cli/scripts/ (bundled at wheel build time)](https://github.com/NousResearch/hermes-agent/commit/b1edf3dfc8948b5ff93f42d26395fa6f30393d9f "chore: gitignore hermes_cli/scripts/ (bundled at wheel build time)") | May 15, 2026 |
| [.mailmap](https://github.com/NousResearch/hermes-agent/blob/main/.mailmap ".mailmap") | [.mailmap](https://github.com/NousResearch/hermes-agent/blob/main/.mailmap ".mailmap") | [chore: add MestreY0d4-Uninter to AUTHOR_MAP and .mailmap](https://github.com/NousResearch/hermes-agent/commit/902f1e6ede20dd618d64aa6dccced966675f8316 "chore: add MestreY0d4-Uninter to AUTHOR_MAP and .mailmap") | Apr 15, 2026 |
| [AGENTS.md](https://github.com/NousResearch/hermes-agent/blob/main/AGENTS.md "AGENTS.md") | [AGENTS.md](https://github.com/NousResearch/hermes-agent/blob/main/AGENTS.md "AGENTS.md") | [security(deps): add upper bounds to 5 loose deps + document supply ch…](https://github.com/NousResearch/hermes-agent/commit/04b1fdaecfda15ff4c8f5c9f0041516efd01ba30 "security(deps): add upper bounds to 5 loose deps + document supply chain policy (#24226) After the Mini Shai-Hulud supply chain campaign (May 2026) and the litellm compromise (March 2026), codify the dependency pinning policy that was established in PRs #2810 and #9801 but never written down for contributors. Changes: - pyproject.toml: Add tight upper bounds to the 5 deps that slipped through as review escapes from external contributor PRs: - hindsight-client>=0.4.22,<0.5 (was >=0.4.22) - aiosqlite>=0.20,<0.23 (was >=0.20) - asyncpg>=0.29,<0.32 (was >=0.29) - alibabacloud-dingtalk>=2.0.0,<3 (was >=2.0.0) - youtube-transcript-api>=1.2.0,<2 (was >=1.2.0) Pre-1.0 packages get <0.(current_minor+2) — tight enough to block hostile minor releases but loose enough to not require bumps every week. - CONTRIBUTING.md: Add 'Dependency pinning policy' section under Security with the full rationale, table of source types + treatments, and examples. - AGENTS.md: Add concise 'Dependency Pinning Policy' section for AI coding agents with the decision table and step-by-step checklist. - supply-chain-audit.yml: Add dep-bounds job that fails PRs introducing PyPI deps without <ceiling upper bounds. Fires on pyproject.toml changes. Posts a PR comment with the specific unbounded specs found. Refs: #2796 #2810 #9801 #24205") | May 15, 2026 |
| [CONTRIBUTING.md](https://github.com/NousResearch/hermes-agent/blob/main/CONTRIBUTING.md "CONTRIBUTING.md") | [CONTRIBUTING.md](https://github.com/NousResearch/hermes-agent/blob/main/CONTRIBUTING.md "CONTRIBUTING.md") | [security(deps): add upper bounds to 5 loose deps + document supply ch…](https://github.com/NousResearch/hermes-agent/commit/04b1fdaecfda15ff4c8f5c9f0041516efd01ba30 "security(deps): add upper bounds to 5 loose deps + document supply chain policy (#24226) After the Mini Shai-Hulud supply chain campaign (May 2026) and the litellm compromise (March 2026), codify the dependency pinning policy that was established in PRs #2810 and #9801 but never written down for contributors. Changes: - pyproject.toml: Add tight upper bounds to the 5 deps that slipped through as review escapes from external contributor PRs: - hindsight-client>=0.4.22,<0.5 (was >=0.4.22) - aiosqlite>=0.20,<0.23 (was >=0.20) - asyncpg>=0.29,<0.32 (was >=0.29) - alibabacloud-dingtalk>=2.0.0,<3 (was >=2.0.0) - youtube-transcript-api>=1.2.0,<2 (was >=1.2.0) Pre-1.0 packages get <0.(current_minor+2) — tight enough to block hostile minor releases but loose enough to not require bumps every week. - CONTRIBUTING.md: Add 'Dependency pinning policy' section under Security with the full rationale, table of source types + treatments, and examples. - AGENTS.md: Add concise 'Dependency Pinning Policy' section for AI coding agents with the decision table and step-by-step checklist. - supply-chain-audit.yml: Add dep-bounds job that fails PRs introducing PyPI deps without <ceiling upper bounds. Fires on pyproject.toml changes. Posts a PR comment with the specific unbounded specs found. Refs: #2796 #2810 #9801 #24205") | May 15, 2026 |
| [Dockerfile](https://github.com/NousResearch/hermes-agent/blob/main/Dockerfile "Dockerfile") | [Dockerfile](https://github.com/NousResearch/hermes-agent/blob/main/Dockerfile "Dockerfile") | [fix(docker): chown .venv to hermes so lazy_deps can install platform …](https://github.com/NousResearch/hermes-agent/commit/942adf617910f50a39f41bd200d8083bf4cb2bed "fix(docker): chown .venv to hermes so lazy_deps can install platform packages (#24841) The Dockerfile permissions section made /opt/hermes/.venv readable but not writable by the hermes runtime user. Since the 2026-05-12 policy change moved messaging packages (discord.py, telegram, slack, etc.) out of [all] and into lazy_deps.py, the Docker image no longer ships with them pre-installed. At first gateway boot, lazy_deps.ensure() tries to `uv pip install` them into the venv but fails with EACCES because site-packages is root-owned. The result: every messaging platform adapter silently fails to load inside Docker containers, producing only a cryptic \"discord.py not installed\" warning despite the gateway being correctly configured. Two-part fix: 1. Dockerfile: add /opt/hermes/.venv to the existing chown -R hermes:hermes line so the default (UID 10000) case works out of the box. 2. docker/entrypoint.sh: extend the needs_chown block to also re-chown the .venv when HERMES_UID is remapped. Without this, the build-time chown becomes stale when someone uses the documented HERMES_UID override in docker-compose.yml. Fixes #21536 Related: #17674, #21543, #21755") | May 13, 2026 |
| [LICENSE](https://github.com/NousResearch/hermes-agent/blob/main/LICENSE "LICENSE") | [LICENSE](https://github.com/NousResearch/hermes-agent/blob/main/LICENSE "LICENSE") | [fix: restore missing MIT license file](https://github.com/NousResearch/hermes-agent/commit/9ba5d399e58fa353d7132b0e2e9533d281ff64d1 "fix: restore missing MIT license file") | Mar 7, 2026 |
| [MANIFEST.in](https://github.com/NousResearch/hermes-agent/blob/main/MANIFEST.in "MANIFEST.in") | [MANIFEST.in](https://github.com/NousResearch/hermes-agent/blob/main/MANIFEST.in "MANIFEST.in") | [chore: prepare Hermes for Homebrew packaging (](https://github.com/NousResearch/hermes-agent/commit/e64b047663a0ff95753a1bf930036e6ccca43bd2 "chore: prepare Hermes for Homebrew packaging (#4099) Co-authored-by: Yabuku-xD <78594762+Yabuku-xD@users.noreply.github.com>")[#4099](https://github.com/NousResearch/hermes-agent/pull/4099)[)](https://github.com/NousResearch/hermes-agent/commit/e64b047663a0ff95753a1bf930036e6ccca43bd2 "chore: prepare Hermes for Homebrew packaging (#4099) Co-authored-by: Yabuku-xD <78594762+Yabuku-xD@users.noreply.github.com>") | Mar 31, 2026 |
| [README.md](https://github.com/NousResearch/hermes-agent/blob/main/README.md "README.md") | [README.md](https://github.com/NousResearch/hermes-agent/blob/main/README.md "README.md") | [docs(readme): remove hermes-eval and Hermes MemPalace from Community …](https://github.com/NousResearch/hermes-agent/commit/32c3f06a5bf0867d11d309503122f59d0dba75d9 "docs(readme): remove hermes-eval and Hermes MemPalace from Community links (#27271) Both links were merged from low-risk batch salvage but on review they're brand-new single-commit personal repos with zero stars/forks and no track record. README links from us implicitly endorse community projects; the Community section should have a minimum activity bar before we link to a repo, not just \"the contributor opened a PR.\" MemPalace in particular wraps an in-process memory provider, so a README endorsement carries more risk than a typical docs link.") | May 17, 2026 |
| [README.zh-CN.md](https://github.com/NousResearch/hermes-agent/blob/main/README.zh-CN.md "README.zh-CN.md") | [README.zh-CN.md](https://github.com/NousResearch/hermes-agent/blob/main/README.zh-CN.md "README.zh-CN.md") | [chore: remove Atropos RL environments and tinker-atropos integration (](https://github.com/NousResearch/hermes-agent/commit/5af672c7530263544a9f5e2479f3853d83b3b798 "chore: remove Atropos RL environments and tinker-atropos integration (#26106) * chore: remove Atropos RL environments, tools, tests, skill, and tinker-atropos submodule Delete: - environments/ (43 files — base env, agent loop, tool call parsers, benchmarks) - rl_cli.py (standalone RL training CLI) - tools/rl_training_tool.py (all 10 rl_* tools) - tests: test_rl_training_tool, test_tool_call_parsers, test_managed_server_tool_support, test_agent_loop, test_agent_loop_vllm, test_agent_loop_tool_calling, test_terminalbench2_env_security - optional-skills/mlops/hermes-atropos-environments/ - tinker-atropos git submodule + .gitmodules * chore: remove RL/Atropos references from Python source - toolsets.py: remove rl toolset block + update comment - model_tools.py: remove rl_tools group + update async bridging comment - hermes_cli/tools_config.py: remove RL display entry, _DEFAULT_OFF_TOOLSETS, setup block, and rl_training post-setup handler - tools/budget_config.py: remove RL environment reference in docstring - tests/test_model_tools.py: remove rl_tools from expected groups - tests/run_agent/test_streaming_tool_call_repair.py: fix stale cross-reference * chore: remove rl/yc-bench extras and tinker-atropos refs from pyproject.toml - Remove rl extra (atroposlib, tinker, fastapi, uvicorn, wandb) - Remove yc-bench extra - Remove rl_cli from py-modules - Remove [tool.ty.src] exclude for tinker-atropos - Remove [tool.ruff] exclude for tinker-atropos - Regenerate uv.lock * chore: remove tinker-atropos from install/setup scripts - setup-hermes.sh: remove entire tinker-atropos submodule install block - scripts/install.sh: remove both tinker-atropos blocks (Termux + standard) - scripts/install.ps1: remove tinker-atropos block - nix/hermes-agent.nix: remove tinker-atropos pip install line * chore: remove RL references from cli-config.yaml.example * docs: remove Atropos/RL references from README, CONTRIBUTING, AGENTS.md * docs: remove RL/Atropos references from website - Delete: environments.md, rl-training.md, mlops-hermes-atropos-environments.md - sidebars.ts: remove rl-training and environments sidebar entries - optional-skills-catalog.md: remove hermes-atropos-environments row - tools-reference.md: remove entire rl toolset section - toolsets-reference.md: remove rl row + update example - integrations/index.md: remove RL Training bullet - architecture.md: remove environments/ from tree + RL section - contributing.md: remove tinker-atropos setup - updating.md: remove tinker-atropos install + stale submodule update * chore: remove remaining RL/Atropos stragglers - hermes_cli/config.py: remove TINKER_API_KEY + WANDB_API_KEY env var defs - hermes_cli/doctor.py: remove Submodules check section (tinker-atropos) - hermes_cli/setup.py: remove RL Training status check - hermes_cli/status.py: remove Tinker + WandB from API key status display - agent/display.py: remove both rl_* tool preview/activity blocks - website/docs: remove RL references from providers.md + env-variables.md - tests: remove TINKER_API_KEY from conftest, set_config_value, setup_script * chore: remove RL training section from .env.example")[#…](https://github.com/NousResearch/hermes-agent/pull/26106) | May 15, 2026 |
| [RELEASE_v0.10.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.10.0.md "RELEASE_v0.10.0.md") | [RELEASE_v0.10.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.10.0.md "RELEASE_v0.10.0.md") | [chore: release v0.10.0 (2026.4.16) (](https://github.com/NousResearch/hermes-agent/commit/1dd6b5d5fb94cac59e93388f9aeee6bc365b8f42 "chore: release v0.10.0 (2026.4.16) (#11209) Tool Gateway release — paid Nous Portal subscribers get web search, image gen, TTS, and browser automation through their existing subscription.")[#11209](https://github.com/NousResearch/hermes-agent/pull/11209)[)](https://github.com/NousResearch/hermes-agent/commit/1dd6b5d5fb94cac59e93388f9aeee6bc365b8f42 "chore: release v0.10.0 (2026.4.16) (#11209) Tool Gateway release — paid Nous Portal subscribers get web search, image gen, TTS, and browser automation through their existing subscription.") | Apr 16, 2026 |
| [RELEASE_v0.11.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.11.0.md "RELEASE_v0.11.0.md") | [RELEASE_v0.11.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.11.0.md "RELEASE_v0.11.0.md") | [chore: release v0.11.0 (2026.4.23) (](https://github.com/NousResearch/hermes-agent/commit/bf196a3fc0fd1f79353369e8732051db275c6276 "chore: release v0.11.0 (2026.4.23) (#14791) The Interface release — new Ink-based TUI, pluggable transport architecture, native AWS Bedrock, five new inference paths (NVIDIA NIM, Arcee, Step Plan, Gemini CLI OAuth, ai-gateway), GPT-5.5 via Codex OAuth, QQBot (17th platform), expanded plugin surface, dashboard plugin system + live theme switching, /steer mid-run nudges, shell hooks, webhook direct-delivery, smarter delegation, and auxiliary models config UI. Also folds in the v0.10.0 deferred batch (v0.10.0 shipped only the Nous Tool Gateway). 1,556 commits · 761 PRs · 290 contributors since v0.9.0.")[#14791](https://github.com/NousResearch/hermes-agent/pull/14791)[)](https://github.com/NousResearch/hermes-agent/commit/bf196a3fc0fd1f79353369e8732051db275c6276 "chore: release v0.11.0 (2026.4.23) (#14791) The Interface release — new Ink-based TUI, pluggable transport architecture, native AWS Bedrock, five new inference paths (NVIDIA NIM, Arcee, Step Plan, Gemini CLI OAuth, ai-gateway), GPT-5.5 via Codex OAuth, QQBot (17th platform), expanded plugin surface, dashboard plugin system + live theme switching, /steer mid-run nudges, shell hooks, webhook direct-delivery, smarter delegation, and auxiliary models config UI. Also folds in the v0.10.0 deferred batch (v0.10.0 shipped only the Nous Tool Gateway). 1,556 commits · 761 PRs · 290 contributors since v0.9.0.") | Apr 23, 2026 |
| [RELEASE_v0.12.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.12.0.md "RELEASE_v0.12.0.md") | [RELEASE_v0.12.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.12.0.md "RELEASE_v0.12.0.md") | [chore: release v0.12.0 (2026.4.30) (](https://github.com/NousResearch/hermes-agent/commit/73bf3ab1b22314ed9dfecbb59242c03742fe72af "chore: release v0.12.0 (2026.4.30) (#18057) The Curator release — Hermes Agent now maintains itself. Autonomous background Curator grades, prunes, and consolidates the skill library; self-improvement loop substantially upgraded; four new inference providers; Microsoft Teams (via pluggable platforms) + Yuanbao as 18th and 19th messaging platforms; Spotify + Google Meet native integrations; ComfyUI + TouchDesigner-MCP bundled by default; Humanizer skill ported; ~57% cut to visible TUI cold start. Stats since v0.11.0: 1,096 commits, 550 merged PRs, 1,270 files changed, 217,776 insertions, 213 community contributors.")[#18057](https://github.com/NousResearch/hermes-agent/pull/18057)[)](https://github.com/NousResearch/hermes-agent/commit/73bf3ab1b22314ed9dfecbb59242c03742fe72af "chore: release v0.12.0 (2026.4.30) (#18057) The Curator release — Hermes Agent now maintains itself. Autonomous background Curator grades, prunes, and consolidates the skill library; self-improvement loop substantially upgraded; four new inference providers; Microsoft Teams (via pluggable platforms) + Yuanbao as 18th and 19th messaging platforms; Spotify + Google Meet native integrations; ComfyUI + TouchDesigner-MCP bundled by default; Humanizer skill ported; ~57% cut to visible TUI cold start. Stats since v0.11.0: 1,096 commits, 550 merged PRs, 1,270 files changed, 217,776 insertions, 213 community contributors.") | Apr 30, 2026 |
| [RELEASE_v0.13.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.13.0.md "RELEASE_v0.13.0.md") | [RELEASE_v0.13.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.13.0.md "RELEASE_v0.13.0.md") | [chore: release v0.13.0 (2026.5.7) (](https://github.com/NousResearch/hermes-agent/commit/498bfc7bc12a937621b4215312049b1000726df3 "chore: release v0.13.0 (2026.5.7) (#21406) The Tenacity Release — Hermes Agent now finishes what it starts. - Durable multi-agent Kanban with heartbeat, reclaim, zombie detection, retry budgets, hallucination gate - /goal persistent cross-turn goals (Ralph loop) - Checkpoints v2 single-store rewrite with real pruning - Gateway auto-resume interrupted sessions after restart - no_agent cron watchdog mode - Post-write delta lint on write_file + patch - 8 P0 security closures — redaction ON by default, CVSS 8.1 Discord fix, WhatsApp stranger rejection, MCP/auth TOCTOU, SSRF floor, cron prompt-injection skill scanning - Google Chat (20th platform) + generic platform-plugin hooks - ProviderProfile ABC + plugins/model-providers/ - 7 i18n locales (zh/ja/de/es/fr/uk/tr) + display.language - video_analyze tool, xAI Custom Voices, SearXNG, OpenRouter caching - MCP SSE transport + OAuth + image MEDIA surfacing - 864 commits, 588 merged PRs, 295 contributors")[#21406](https://github.com/NousResearch/hermes-agent/pull/21406)[)](https://github.com/NousResearch/hermes-agent/commit/498bfc7bc12a937621b4215312049b1000726df3 "chore: release v0.13.0 (2026.5.7) (#21406) The Tenacity Release — Hermes Agent now finishes what it starts. - Durable multi-agent Kanban with heartbeat, reclaim, zombie detection, retry budgets, hallucination gate - /goal persistent cross-turn goals (Ralph loop) - Checkpoints v2 single-store rewrite with real pruning - Gateway auto-resume interrupted sessions after restart - no_agent cron watchdog mode - Post-write delta lint on write_file + patch - 8 P0 security closures — redaction ON by default, CVSS 8.1 Discord fix, WhatsApp stranger rejection, MCP/auth TOCTOU, SSRF floor, cron prompt-injection skill scanning - Google Chat (20th platform) + generic platform-plugin hooks - ProviderProfile ABC + plugins/model-providers/ - 7 i18n locales (zh/ja/de/es/fr/uk/tr) + display.language - video_analyze tool, xAI Custom Voices, SearXNG, OpenRouter caching - MCP SSE transport + OAuth + image MEDIA surfacing - 864 commits, 588 merged PRs, 295 contributors") | May 7, 2026 |
| [RELEASE_v0.14.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.14.0.md "RELEASE_v0.14.0.md") | [RELEASE_v0.14.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.14.0.md "RELEASE_v0.14.0.md") | [docs(release): expand v0.14.0 highlights with newcomer-friendly conte…](https://github.com/NousResearch/hermes-agent/commit/8a2b2b9f6f9c419fdef48f542bf4b1991c655810 "docs(release): expand v0.14.0 highlights with newcomer-friendly context (#27053) Each highlight now gets 2-3 sentences explaining the user-facing value, not just the technical change. Targeted at someone discovering Hermes for the first time who isn't deep in the codebase.") | May 16, 2026 |
| [RELEASE_v0.2.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.2.0.md "RELEASE_v0.2.0.md") | [RELEASE_v0.2.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.2.0.md "RELEASE_v0.2.0.md") | [chore: rebuild changelog with correct time window (Feb 25 12PM PST on…](https://github.com/NousResearch/hermes-agent/commit/364cb956c100f452530215add550392cb6c2174d "chore: rebuild changelog with correct time window (Feb 25 12PM PST onwards) Changelog now covers only v0.1.0 → v0.2.0 changes: - 216 merged PRs (not all 231) - 119 resolved issues - 63 contributors (not 74+) - Window: Feb 25 2026 12PM PST to present") | Mar 12, 2026 |
| [RELEASE_v0.3.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.3.0.md "RELEASE_v0.3.0.md") | [RELEASE_v0.3.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.3.0.md "RELEASE_v0.3.0.md") | [chore: release v0.3.0 (v2026.3.17)](https://github.com/NousResearch/hermes-agent/commit/37862f74fa1e32c2c25699fc91f20310728d6d78 "chore: release v0.3.0 (v2026.3.17) - Bump version 0.2.0 → 0.3.0 - Add comprehensive changelog (248 merged PRs, 15 contributors) - CalVer tag: v2026.3.17") | Mar 17, 2026 |
| [RELEASE_v0.4.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.4.0.md "RELEASE_v0.4.0.md") | [RELEASE_v0.4.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.4.0.md "RELEASE_v0.4.0.md") | [docs: revise v0.4.0 changelog — fix feature attribution, reorder sect…](https://github.com/NousResearch/hermes-agent/commit/6e97a3b338eb9c284c7bb4a2eff1a9b69a6f0c9f "docs: revise v0.4.0 changelog — fix feature attribution, reorder sections") | Mar 24, 2026 |
| [RELEASE_v0.5.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.5.0.md "RELEASE_v0.5.0.md") | [RELEASE_v0.5.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.5.0.md "RELEASE_v0.5.0.md") | [chore: release v0.5.0 (v2026.3.28) (](https://github.com/NousResearch/hermes-agent/commit/558cc14ad91ec46ae21430cecbef8e7903be57a7 "chore: release v0.5.0 (v2026.3.28) (#3568) The hardening release — Nous Portal 400+ models, Hugging Face provider, Telegram Private Chat Topics, native Modal SDK, plugin lifecycle hooks, improved OpenAI model reliability, Nix flake, supply chain hardening, Anthropic output limits fix, and 50+ security/reliability fixes. 165 merged PRs, 65 closed issues across a 5-day window.")[#3568](https://github.com/NousResearch/hermes-agent/pull/3568)[)](https://github.com/NousResearch/hermes-agent/commit/558cc14ad91ec46ae21430cecbef8e7903be57a7 "chore: release v0.5.0 (v2026.3.28) (#3568) The hardening release — Nous Portal 400+ models, Hugging Face provider, Telegram Private Chat Topics, native Modal SDK, plugin lifecycle hooks, improved OpenAI model reliability, Nix flake, supply chain hardening, Anthropic output limits fix, and 50+ security/reliability fixes. 165 merged PRs, 65 closed issues across a 5-day window.") | Mar 28, 2026 |
| [RELEASE_v0.6.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.6.0.md "RELEASE_v0.6.0.md") | [RELEASE_v0.6.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.6.0.md "RELEASE_v0.6.0.md") | [chore: release v0.6.0 (2026.3.30) (](https://github.com/NousResearch/hermes-agent/commit/e08778fa1ee377f7128641f8cc03b0de046bd8da "chore: release v0.6.0 (2026.3.30) (#3985)")[#3985](https://github.com/NousResearch/hermes-agent/pull/3985)[)](https://github.com/NousResearch/hermes-agent/commit/e08778fa1ee377f7128641f8cc03b0de046bd8da "chore: release v0.6.0 (2026.3.30) (#3985)") | Mar 30, 2026 |
| [RELEASE_v0.7.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.7.0.md "RELEASE_v0.7.0.md") | [RELEASE_v0.7.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.7.0.md "RELEASE_v0.7.0.md") | [chore: release v0.7.0 (2026.4.3) (](https://github.com/NousResearch/hermes-agent/commit/abf1e98f6253f6984479fe03d1098173a9b065a7 "chore: release v0.7.0 (2026.4.3) (#4812) 168 merged PRs, 223 commits, 46 resolved issues, 40+ contributors. Highlights: pluggable memory providers, credential pools, Camofox browser, inline diff previews, API server session continuity, ACP MCP registration, gateway hardening, secret exfiltration blocking.")[#4812](https://github.com/NousResearch/hermes-agent/pull/4812)[)](https://github.com/NousResearch/hermes-agent/commit/abf1e98f6253f6984479fe03d1098173a9b065a7 "chore: release v0.7.0 (2026.4.3) (#4812) 168 merged PRs, 223 commits, 46 resolved issues, 40+ contributors. Highlights: pluggable memory providers, credential pools, Camofox browser, inline diff previews, API server session continuity, ACP MCP registration, gateway hardening, secret exfiltration blocking.") | Apr 3, 2026 |
| [RELEASE_v0.8.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.8.0.md "RELEASE_v0.8.0.md") | [RELEASE_v0.8.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.8.0.md "RELEASE_v0.8.0.md") | [docs: update v0.8.0 highlights — notify_on_complete, MiMo v2 Pro, reo…](https://github.com/NousResearch/hermes-agent/commit/ff6a86cb529a372198b4b80d5e022e32a4a3f2cc "docs: update v0.8.0 highlights — notify_on_complete, MiMo v2 Pro, reorder") | Apr 8, 2026 |
| [RELEASE_v0.9.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.9.0.md "RELEASE_v0.9.0.md") | [RELEASE_v0.9.0.md](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.9.0.md "RELEASE_v0.9.0.md") | [fix: add contributor audit script + fix missed contributors (](https://github.com/NousResearch/hermes-agent/commit/def8b959b814d158c80e66d70f501adc3b6e9384 "fix: add contributor audit script + fix missed contributors (#9264) Three problems fixed: 1. bobashopcashier missing from v0.9.0 contributor list despite authoring the gateway drain PR (#7290, salvaged into #7503). Their email (kennyx102@gmail.com) was missing from AUTHOR_MAP. 2. release.py only scanned git commit authors, missing Co-authored-by trailers. Now parse_coauthors() extracts trailers from commit bodies. 3. No mechanism to detect contributors from salvaged PRs (where original author only appears in PR description, not git log). Changes: - scripts/release.py: add kennyx102@gmail.com to AUTHOR_MAP, enhance get_commits() to parse Co-authored-by trailers, filter AI assistants (Claude, Copilot, Cursor Agent) from co-author lists - scripts/contributor_audit.py: new script that cross-references git authors, co-author trailers, and salvaged PR descriptions. Reports unknown emails and contributors missing from release notes. - RELEASE_v0.9.0.md: add bobashopcashier to community contributors Usage: python scripts/contributor_audit.py --since-tag v2026.4.8 python scripts/contributor_audit.py --since-tag v2026.4.8 --release-file RELEASE_v0.9.0.md")[#9264](https://github.com/NousResearch/hermes-agent/pull/9264)[)](https://github.com/NousResearch/hermes-agent/commit/def8b959b814d158c80e66d70f501adc3b6e9384 "fix: add contributor audit script + fix missed contributors (#9264) Three problems fixed: 1. bobashopcashier missing from v0.9.0 contributor list despite authoring the gateway drain PR (#7290, salvaged into #7503). Their email (kennyx102@gmail.com) was missing from AUTHOR_MAP. 2. release.py only scanned git commit authors, missing Co-authored-by trailers. Now parse_coauthors() extracts trailers from commit bodies. 3. No mechanism to detect contributors from salvaged PRs (where original author only appears in PR description, not git log). Changes: - scripts/release.py: add kennyx102@gmail.com to AUTHOR_MAP, enhance get_commits() to parse Co-authored-by trailers, filter AI assistants (Claude, Copilot, Cursor Agent) from co-author lists - scripts/contributor_audit.py: new script that cross-references git authors, co-author trailers, and salvaged PR descriptions. Reports unknown emails and contributors missing from release notes. - RELEASE_v0.9.0.md: add bobashopcashier to community contributors Usage: python scripts/contributor_audit.py --since-tag v2026.4.8 python scripts/contributor_audit.py --since-tag v2026.4.8 --release-file RELEASE_v0.9.0.md") | Apr 13, 2026 |
| [SECURITY.md](https://github.com/NousResearch/hermes-agent/blob/main/SECURITY.md "SECURITY.md") | [SECURITY.md](https://github.com/NousResearch/hermes-agent/blob/main/SECURITY.md "SECURITY.md") | [changes from feedback](https://github.com/NousResearch/hermes-agent/commit/0d1cbc2dda28337c4049337b5a90beff766fe6be "changes from feedback") | May 6, 2026 |
| [batch_runner.py](https://github.com/NousResearch/hermes-agent/blob/main/batch_runner.py "batch_runner.py") | [batch_runner.py](https://github.com/NousResearch/hermes-agent/blob/main/batch_runner.py "batch_runner.py") | [chore: ruff auto-fix PLR6201 — tuple → set in membership tests (](https://github.com/NousResearch/hermes-agent/commit/2ec8d2b42ffecec2128f1004c0a8451378057d42 "chore: ruff auto-fix PLR6201 — tuple → set in membership tests (#23937) Replace with for all literal-tuple membership tests. Set lookup is O(1) vs O(n) for tuple — consistent micro-optimization across the codebase. 608 instances fixed via `ruff --fix --unsafe-fixes`, 0 remaining. 133 files, +626/-626 (net zero).")[#23937](https://github.com/NousResearch/hermes-agent/pull/23937)[)](https://github.com/NousResearch/hermes-agent/commit/2ec8d2b42ffecec2128f1004c0a8451378057d42 "chore: ruff auto-fix PLR6201 — tuple → set in membership tests (#23937) Replace with for all literal-tuple membership tests. Set lookup is O(1) vs O(n) for tuple — consistent micro-optimization across the codebase. 608 instances fixed via `ruff --fix --unsafe-fixes`, 0 remaining. 133 files, +626/-626 (net zero).") | May 11, 2026 |
| [cli-config.yaml.example](https://github.com/NousResearch/hermes-agent/blob/main/cli-config.yaml.example "cli-config.yaml.example") | [cli-config.yaml.example](https://github.com/NousResearch/hermes-agent/blob/main/cli-config.yaml.example "cli-config.yaml.example") | [chore: remove Atropos RL environments and tinker-atropos integration (](https://github.com/NousResearch/hermes-agent/commit/5af672c7530263544a9f5e2479f3853d83b3b798 "chore: remove Atropos RL environments and tinker-atropos integration (#26106) * chore: remove Atropos RL environments, tools, tests, skill, and tinker-atropos submodule Delete: - environments/ (43 files — base env, agent loop, tool call parsers, benchmarks) - rl_cli.py (standalone RL training CLI) - tools/rl_training_tool.py (all 10 rl_* tools) - tests: test_rl_training_tool, test_tool_call_parsers, test_managed_server_tool_support, test_agent_loop, test_agent_loop_vllm, test_agent_loop_tool_calling, test_terminalbench2_env_security - optional-skills/mlops/hermes-atropos-environments/ - tinker-atropos git submodule + .gitmodules * chore: remove RL/Atropos references from Python source - toolsets.py: remove rl toolset block + update comment - model_tools.py: remove rl_tools group + update async bridging comment - hermes_cli/tools_config.py: remove RL display entry, _DEFAULT_OFF_TOOLSETS, setup block, and rl_training post-setup handler - tools/budget_config.py: remove RL environment reference in docstring - tests/test_model_tools.py: remove rl_tools from expected groups - tests/run_agent/test_streaming_tool_call_repair.py: fix stale cross-reference * chore: remove rl/yc-bench extras and tinker-atropos refs from pyproject.toml - Remove rl extra (atroposlib, tinker, fastapi, uvicorn, wandb) - Remove yc-bench extra - Remove rl_cli from py-modules - Remove [tool.ty.src] exclude for tinker-atropos - Remove [tool.ruff] exclude for tinker-atropos - Regenerate uv.lock * chore: remove tinker-atropos from install/setup scripts - setup-hermes.sh: remove entire tinker-atropos submodule install block - scripts/install.sh: remove both tinker-atropos blocks (Termux + standard) - scripts/install.ps1: remove tinker-atropos block - nix/hermes-agent.nix: remove tinker-atropos pip install line * chore: remove RL references from cli-config.yaml.example * docs: remove Atropos/RL references from README, CONTRIBUTING, AGENTS.md * docs: remove RL/Atropos references from website - Delete: environments.md, rl-training.md, mlops-hermes-atropos-environments.md - sidebars.ts: remove rl-training and environments sidebar entries - optional-skills-catalog.md: remove hermes-atropos-environments row - tools-reference.md: remove entire rl toolset section - toolsets-reference.md: remove rl row + update example - integrations/index.md: remove RL Training bullet - architecture.md: remove environments/ from tree + RL section - contributing.md: remove tinker-atropos setup - updating.md: remove tinker-atropos install + stale submodule update * chore: remove remaining RL/Atropos stragglers - hermes_cli/config.py: remove TINKER_API_KEY + WANDB_API_KEY env var defs - hermes_cli/doctor.py: remove Submodules check section (tinker-atropos) - hermes_cli/setup.py: remove RL Training status check - hermes_cli/status.py: remove Tinker + WandB from API key status display - agent/display.py: remove both rl_* tool preview/activity blocks - website/docs: remove RL references from providers.md + env-variables.md - tests: remove TINKER_API_KEY from conftest, set_config_value, setup_script * chore: remove RL training section from .env.example")[#…](https://github.com/NousResearch/hermes-agent/pull/26106) | May 15, 2026 |
| [cli.py](https://github.com/NousResearch/hermes-agent/blob/main/cli.py "cli.py") | [cli.py](https://github.com/NousResearch/hermes-agent/blob/main/cli.py "cli.py") | [fix: add paste collapse logging to aid debugging](https://github.com/NousResearch/hermes-agent/commit/7282ef1b9d4ba9b77057f53ca92cbb2ed674129b "fix: add paste collapse logging to aid debugging Adds logger.info when large pastes are collapsed to file references in both paste-code paths (handle_paste and _on_text_changed). Logs paste ID, line count, character count, and file path so operators can correlate missing- content reports with specific paste files. This is a diagnostic aid, not a fix for the paste-drop issue.") | May 17, 2026 |
| [constraints-termux.txt](https://github.com/NousResearch/hermes-agent/blob/main/constraints-termux.txt "constraints-termux.txt") | [constraints-termux.txt](https://github.com/NousResearch/hermes-agent/blob/main/constraints-termux.txt "constraints-termux.txt") | [feat: add tested Termux install path and EOF-aware gh auth](https://github.com/NousResearch/hermes-agent/commit/e79cc8898517cf4b06b0490b828e79a1ee1ede59 "feat: add tested Termux install path and EOF-aware gh auth") | Apr 9, 2026 |
| [docker-compose.yml](https://github.com/NousResearch/hermes-agent/blob/main/docker-compose.yml "docker-compose.yml") | [docker-compose.yml](https://github.com/NousResearch/hermes-agent/blob/main/docker-compose.yml "docker-compose.yml") | [feat(plugins/google_chat): Google Chat platform adapter as a bundled …](https://github.com/NousResearch/hermes-agent/commit/44cd79e798e4aed6ee316f02e595b33cde7687a0 "feat(plugins/google_chat): Google Chat platform adapter as a bundled plugin Adds Google Chat as a new gateway platform, shipped under plugins/platforms/google_chat/ following the canonical bundled-plugin pattern (Teams, IRC). Rewired from the original PR #18425 to use the new env_enablement_fn + cron_deliver_env_var plugin interfaces landed in the preceding commit, so the adapter touches ZERO core files. What it does: - Inbound DM + group messages via Cloud Pub/Sub pull subscription (no public URL needed), with attachments (PDFs, images, audio, video) downloaded through an SSRF-guarded Google-host allowlist. - Outbound text replies with the 'Hermes is thinking…' patch-in-place pattern — no tombstones. - Native file attachment delivery via per-user OAuth. Google Chat's media.upload endpoint rejects service-account auth, so each user runs /setup-files once in their own DM to grant chat.messages.create for themselves; the adapter then uploads as them. Tokens stored per email at ~/.hermes/google_chat_user_tokens/<email>.json. - Thread isolation: side-threads get isolated sessions, top-level DM messages share one continuous session. Persistent thread-count store survives gateway restart. - Supervisor reconnect with exponential backoff. - Multi-user out of the box. How it plugs in (no core edits): - env_enablement_fn seeds PlatformConfig.extra with project_id, subscription_name, service_account_json, and the home_channel dict (which the core hook turns into a HomeChannel dataclass). Reads GOOGLE_CHAT_PROJECT_ID (falls back to GOOGLE_CLOUD_PROJECT), GOOGLE_CHAT_SUBSCRIPTION_NAME (falls back to GOOGLE_CHAT_SUBSCRIPTION), GOOGLE_CHAT_SERVICE_ACCOUNT_JSON (falls back to GOOGLE_APPLICATION_CREDENTIALS), GOOGLE_CHAT_HOME_CHANNEL. - cron_deliver_env_var='GOOGLE_CHAT_HOME_CHANNEL' gets cron delivery for free — cron/scheduler.py consults the platform registry for any name not in its hardcoded built-in sets. - plugin.yaml's rich requires_env / optional_env blocks auto-populate OPTIONAL_ENV_VARS via the new hermes_cli/config.py injector, so 'hermes config' UI surfaces them with description / url / prompt / password metadata. - Module-level Platform('google_chat') call in adapter.py triggers the Platform._missing_() registration so Platform.GOOGLE_CHAT attribute access works without an enum entry. Distribution: ships inside the existing hermes-agent package. Users opt in via 'pip install hermes-agent[google_chat]' and follow the 8-step GCP walkthrough at website/docs/user-guide/messaging/google_chat.md. Test coverage: 153 tests in tests/gateway/test_google_chat.py, all passing. Spans platform registration, env config loading, Pub/Sub envelope routing, outbound send + chunking + typing patch-in-place, attachment send paths, SSRF guard, thread/session model, supervisor reconnect, authorization, per-user OAuth, and the new plugin-registry cron delivery wiring. Credit: adapter + OAuth + tests + docs authored by @donramon77 (PR #18425). Rewire onto the new plugin hooks + salvage commit by Teknium. Co-Authored-By: Ramón Fernández <112875006+donramon77@users.noreply.github.com>") | May 7, 2026 |
| [flake.lock](https://github.com/NousResearch/hermes-agent/blob/main/flake.lock "flake.lock") | [flake.lock](https://github.com/NousResearch/hermes-agent/blob/main/flake.lock "flake.lock") | [fix nix build](https://github.com/NousResearch/hermes-agent/commit/5e5e65f6d5b11e4df95c29d47fde198a0405cae1 "fix nix build") | Apr 11, 2026 |
| [flake.nix](https://github.com/NousResearch/hermes-agent/blob/main/flake.nix "flake.nix") | [flake.nix](https://github.com/NousResearch/hermes-agent/blob/main/flake.nix "flake.nix") | [feat(nix): declarative plugin installation for NixOS module (](https://github.com/NousResearch/hermes-agent/commit/ef41d3bd450712759768537ffe709c93ead7700b "feat(nix): declarative plugin installation for NixOS module (#15953) * feat(nix): parameterize dependency-groups in python.nix * refactor(nix): extract package to callPackage-able hermes-agent.nix Makes the package overridable via .override{} and adds extraPythonPackages parameter for PYTHONPATH injection. Includes build-time collision check using PEP 503 name canonicalization. * feat(nix): add overlay for external NixOS consumption External flakes can now add overlays = [ inputs.hermes-agent.overlays.default ] to get pkgs.hermes-agent with full .override support. * test(nix): add check for extraPythonPackages PYTHONPATH injection Verifies wrapper has PYTHONPATH when extras provided, and base package has no PYTHONPATH without extras. * feat(nix): add extraPlugins option for directory-based plugins Symlinks plugin packages into HERMES_HOME/plugins/ at activation time. Validates plugin.yaml presence. Asserts unique plugin names at eval time. Hermes discovers them automatically via its directory scan. * feat(nix): add extraPythonPackages option for entry-point plugins Overrides the hermes package with PYTHONPATH injection when extraPythonPackages is non-empty. Plugin .dist-info directories become visible to importlib.metadata for entry-point discovery. Works in both native systemd and container modes. * docs: add NixOS declarative plugin installation to nix-setup, plugins, and build-a-plugin guides - nix-setup.md: new Plugins section with extraPlugins/extraPythonPackages examples, overlay usage, collision checking note, options reference rows - plugins.md: Nix row in discovery table, NixOS declarative plugins section - build-a-hermes-plugin.md: Distribute for NixOS section after pip section * fix: address review feedback — remove unrelated umask, fix fetchFromGitHub naming, simplify checks - Remove accidentally introduced umask/migration changes (unrelated to plugins) - Add pluginName helper, fix fetchFromGitHub producing name='source' - Show name= in extraPlugins example docs - Simplify checks.nix: use hermes-agent.override instead of re-callPackage - Fix fragile grep shell logic in checks * refactor: address simplify feedback — lib.getName, drop unused inputs', Python list for extras - Use lib.getName instead of custom pluginName helper - Drop unused inputs' from checks.nix perSystem args - Pass extraPythonPackages as Python list literal instead of colon-split string * fix: walk propagatedBuildInputs for plugin PYTHONPATH and collision check Uses python312.pkgs.requiredPythonModules to resolve the full transitive closure of extraPythonPackages. Without this, a plugin with third-party deps (e.g. requests) would fail at runtime if those deps weren't already in the sealed uv2nix venv. The collision check now also scans the full closure, catching transitive conflicts. * cleanup: fold plugins into subdir loop, use find for symlink cleanup, inline lib.getName - Add 'plugins' to the existing cron/sessions/logs/memories subdir loop instead of a separate mkdir/chown/chmod block - Replace fragile for-glob with find -delete for stale symlink cleanup - Inline lib.getName at both call sites, remove pluginName wrapper")[#15953](https://github.com/NousResearch/hermes-agent/pull/15953)[)](https://github.com/NousResearch/hermes-agent/commit/ef41d3bd450712759768537ffe709c93ead7700b "feat(nix): declarative plugin installation for NixOS module (#15953) * feat(nix): parameterize dependency-groups in python.nix * refactor(nix): extract package to callPackage-able hermes-agent.nix Makes the package overridable via .override{} and adds extraPythonPackages parameter for PYTHONPATH injection. Includes build-time collision check using PEP 503 name canonicalization. * feat(nix): add overlay for external NixOS consumption External flakes can now add overlays = [ inputs.hermes-agent.overlays.default ] to get pkgs.hermes-agent with full .override support. * test(nix): add check for extraPythonPackages PYTHONPATH injection Verifies wrapper has PYTHONPATH when extras provided, and base package has no PYTHONPATH without extras. * feat(nix): add extraPlugins option for directory-based plugins Symlinks plugin packages into HERMES_HOME/plugins/ at activation time. Validates plugin.yaml presence. Asserts unique plugin names at eval time. Hermes discovers them automatically via its directory scan. * feat(nix): add extraPythonPackages option for entry-point plugins Overrides the hermes package with PYTHONPATH injection when extraPythonPackages is non-empty. Plugin .dist-info directories become visible to importlib.metadata for entry-point discovery. Works in both native systemd and container modes. * docs: add NixOS declarative plugin installation to nix-setup, plugins, and build-a-plugin guides - nix-setup.md: new Plugins section with extraPlugins/extraPythonPackages examples, overlay usage, collision checking note, options reference rows - plugins.md: Nix row in discovery table, NixOS declarative plugins section - build-a-hermes-plugin.md: Distribute for NixOS section after pip section * fix: address review feedback — remove unrelated umask, fix fetchFromGitHub naming, simplify checks - Remove accidentally introduced umask/migration changes (unrelated to plugins) - Add pluginName helper, fix fetchFromGitHub producing name='source' - Show name= in extraPlugins example docs - Simplify checks.nix: use hermes-agent.override instead of re-callPackage - Fix fragile grep shell logic in checks * refactor: address simplify feedback — lib.getName, drop unused inputs', Python list for extras - Use lib.getName instead of custom pluginName helper - Drop unused inputs' from checks.nix perSystem args - Pass extraPythonPackages as Python list literal instead of colon-split string * fix: walk propagatedBuildInputs for plugin PYTHONPATH and collision check Uses python312.pkgs.requiredPythonModules to resolve the full transitive closure of extraPythonPackages. Without this, a plugin with third-party deps (e.g. requests) would fail at runtime if those deps weren't already in the sealed uv2nix venv. The collision check now also scans the full closure, catching transitive conflicts. * cleanup: fold plugins into subdir loop, use find for symlink cleanup, inline lib.getName - Add 'plugins' to the existing cron/sessions/logs/memories subdir loop instead of a separate mkdir/chown/chmod block - Replace fragile for-glob with find -delete for stale symlink cleanup - Inline lib.getName at both call sites, remove pluginName wrapper") | Apr 27, 2026 |
| [hermes](https://github.com/NousResearch/hermes-agent/blob/main/hermes "hermes") | [hermes](https://github.com/NousResearch/hermes-agent/blob/main/hermes "hermes") | [fix: use argparse entrypoint in top-level launcher (](https://github.com/NousResearch/hermes-agent/commit/fd29933a6d44fdb1168fed5a50df07aba84c8387 "fix: use argparse entrypoint in top-level launcher (#3874) The ./hermes convenience script still used the legacy Fire-based cli.main wrapper, which doesn't support subcommands (gateway, cron, doctor, etc.). The installed 'hermes' command already uses hermes_cli.main:main (argparse) — this aligns the launcher. Salvaged from PR #2009 by gito369.")[#3874](https://github.com/NousResearch/hermes-agent/pull/3874)[)](https://github.com/NousResearch/hermes-agent/commit/fd29933a6d44fdb1168fed5a50df07aba84c8387 "fix: use argparse entrypoint in top-level launcher (#3874) The ./hermes convenience script still used the legacy Fire-based cli.main wrapper, which doesn't support subcommands (gateway, cron, doctor, etc.). The installed 'hermes' command already uses hermes_cli.main:main (argparse) — this aligns the launcher. Salvaged from PR #2009 by gito369.") | Mar 30, 2026 |
| [hermes-already-has-routines.md](https://github.com/NousResearch/hermes-agent/blob/main/hermes-already-has-routines.md "hermes-already-has-routines.md") | [hermes-already-has-routines.md](https://github.com/NousResearch/hermes-agent/blob/main/hermes-already-has-routines.md "hermes-already-has-routines.md") | [docs: automation templates gallery + comparison post (](https://github.com/NousResearch/hermes-agent/commit/95d11dfd8e6e86e97657598450efe065f33e9cdd "docs: automation templates gallery + comparison post (#9821) * feat(skills): add fitness-nutrition skill to optional-skills Cherry-picked from PR #9177 by @haileymarshall. Adds a fitness and nutrition skill for gym-goers and health-conscious users: - Exercise search via wger API (690+ exercises, free, no auth) - Nutrition lookup via USDA FoodData Central (380K+ foods, DEMO_KEY fallback) - Offline body composition calculators (BMI, TDEE, 1RM, macros, body fat %) - Pure stdlib Python, no pip dependencies Changes from original PR: - Moved from skills/ to optional-skills/health/ (correct location) - Fixed BMR formula in FORMULAS.md (removed confusing -5+10, now just +5) - Fixed author attribution to match PR submitter - Marked USDA_API_KEY as optional (DEMO_KEY works without signup) Also adds optional env var support to the skill readiness checker: - New 'optional: true' field in required_environment_variables entries - Optional vars are preserved in metadata but don't block skill readiness - Optional vars skip the CLI capture prompt flow - Skills with only optional missing vars show as 'available' not 'setup_needed' * docs: add automation templates gallery and comparison post - New docs page: guides/automation-templates.md with 15+ ready-to-use automation recipes covering development workflow, devops, research, GitHub events, and business operations - Comparison post (hermes-already-has-routines.md) showing Hermes has had schedule/webhook/API triggers since March 2026 - Added automation-templates to sidebar navigation --------- Co-authored-by: haileymarshall <haileymarshall@users.noreply.github.com>")[#9821](https://github.com/NousResearch/hermes-agent/pull/9821)[)](https://github.com/NousResearch/hermes-agent/commit/95d11dfd8e6e86e97657598450efe065f33e9cdd "docs: automation templates gallery + comparison post (#9821) * feat(skills): add fitness-nutrition skill to optional-skills Cherry-picked from PR #9177 by @haileymarshall. Adds a fitness and nutrition skill for gym-goers and health-conscious users: - Exercise search via wger API (690+ exercises, free, no auth) - Nutrition lookup via USDA FoodData Central (380K+ foods, DEMO_KEY fallback) - Offline body composition calculators (BMI, TDEE, 1RM, macros, body fat %) - Pure stdlib Python, no pip dependencies Changes from original PR: - Moved from skills/ to optional-skills/health/ (correct location) - Fixed BMR formula in FORMULAS.md (removed confusing -5+10, now just +5) - Fixed author attribution to match PR submitter - Marked USDA_API_KEY as optional (DEMO_KEY works without signup) Also adds optional env var support to the skill readiness checker: - New 'optional: true' field in required_environment_variables entries - Optional vars are preserved in metadata but don't block skill readiness - Optional vars skip the CLI capture prompt flow - Skills with only optional missing vars show as 'available' not 'setup_needed' * docs: add automation templates gallery and comparison post - New docs page: guides/automation-templates.md with 15+ ready-to-use automation recipes covering development workflow, devops, research, GitHub events, and business operations - Comparison post (hermes-already-has-routines.md) showing Hermes has had schedule/webhook/API triggers since March 2026 - Added automation-templates to sidebar navigation --------- Co-authored-by: haileymarshall <haileymarshall@users.noreply.github.com>") | Apr 14, 2026 |
| [hermes_bootstrap.py](https://github.com/NousResearch/hermes-agent/blob/main/hermes_bootstrap.py "hermes_bootstrap.py") | [hermes_bootstrap.py](https://github.com/NousResearch/hermes-agent/blob/main/hermes_bootstrap.py "hermes_bootstrap.py") | [hermes_bootstrap: Windows-only UTF-8 stdio shim for all entry points](https://github.com/NousResearch/hermes-agent/commit/d94fb47717eb6e2c343e1615fdabf436f19b350a "hermes_bootstrap: Windows-only UTF-8 stdio shim for all entry points Codebase-wide fix for Python-on-Windows UTF-8 footguns, complementing the earlier execute_code sandbox fixes (which remain load-bearing for when the sandbox explicitly scrubs child env). Problem: Python on Windows has two long-standing text-encoding pitfalls: 1. sys.stdout/stderr are bound to the console code page (cp1252 on US-locale installs) — print('café') crashes with UnicodeEncodeError. 2. Subprocess children don't know to use UTF-8 unless PYTHONUTF8 and/or PYTHONIOENCODING are set in their env — so any Python we spawn (linters, sandbox children, delegation workers) hits the same bug. Solution: A tiny bootstrap module (hermes_bootstrap.py) imported as the first statement of every Hermes entry point: - hermes_cli/main.py (hermes / hermes-agent console_script) - run_agent.py (hermes-agent direct) - acp_adapter/entry.py (hermes-acp) - gateway/run.py (messaging gateway) - batch_runner.py (parallel batch mode) - cli.py (legacy direct-launch CLI) On Windows, the bootstrap: - os.environ.setdefault('PYTHONUTF8', '1') (PEP 540 UTF-8 mode) - os.environ.setdefault('PYTHONIOENCODING', 'utf-8') - sys.stdout/stderr/stdin.reconfigure(encoding='utf-8', errors='replace') Children inherit the env vars → they run in UTF-8 mode. Current process's stdio is reconfigured → print('café') works now. On POSIX (Linux/macOS), the bootstrap is a complete no-op. We don't touch LANG, LC_*, or anything else — users who have intentionally configured a non-UTF-8 locale aren't affected. POSIX systems are already UTF-8 by default in 99% of modern setups, so there's nothing to fix. setdefault() (not overwrite) means users who explicitly set PYTHONUTF8=0 or PYTHONIOENCODING=cp1252 in their environment are respected. What this does NOT fix: bare open(path, 'w') calls in the *parent* process still default to locale encoding because PYTHONUTF8 is only read at interpreter init. A ruff PLW1514 sweep (separate follow-up) will add explicit encoding='utf-8' at those ~219 call sites for belt-and-suspenders. Tests (17): 16 passed, 1 skipped on Windows. - Windows: env vars set, stdio reconfigured, child inherits UTF-8 mode - POSIX: complete no-op (verified on fake POSIX + skipped on real POSIX since we don't have a Linux box in this session) - Idempotence: multiple calls safe - Graceful degradation: non-reconfigurable streams don't crash - User opt-out: explicit PYTHONUTF8=0 is respected - Load order: every entry point's FIRST top-level import is hermes_bootstrap, enforced by an AST-level parametrized test pyproject.toml: added hermes_bootstrap to py-modules so it ships with pip installs.") | May 8, 2026 |
| [hermes_constants.py](https://github.com/NousResearch/hermes-agent/blob/main/hermes_constants.py "hermes_constants.py") | [hermes_constants.py](https://github.com/NousResearch/hermes-agent/blob/main/hermes_constants.py "hermes_constants.py") | [codebase: add encoding='utf-8' to all bare open() calls (PLW1514)](https://github.com/NousResearch/hermes-agent/commit/cbce5e93fcb9a923ab71f45d2a0f0f172dd54967 "codebase: add encoding='utf-8' to all bare open() calls (PLW1514) Closes the last Python-on-Windows UTF-8 exposure by making every text-mode open() call explicit about its encoding. Before: on Windows, bare open(path, 'r') defaults to the system locale encoding (cp1252 on US-locale installs). That means reading any config/yaml/markdown/json file with non-ASCII content either crashes with UnicodeDecodeError or silently mis-decodes bytes. After: all 89 affected call sites in production code now pass encoding='utf-8' explicitly. Works identically on every platform and every locale, no surprise behavior. Mechanical sweep via: ruff check --preview --extend-select PLW1514 --unsafe-fixes --fix --exclude 'tests,venv,.venv,node_modules,website,optional-skills, skills,tinker-atropos,plugins' . All 89 fixes have the same shape: open(x) or open(x, mode) became open(x, encoding='utf-8') or open(x, mode, encoding='utf-8'). Nothing else changed. Every modified file still parses and the Windows/sandbox test suite is still green (85 passed, 14 skipped, 0 failed across tests/tools/test_code_execution_windows_env.py + tests/tools/test_code_execution_modes.py + tests/tools/test_env_passthrough.py + tests/test_hermes_bootstrap.py). Scope notes: - tests/ excluded: test fixtures can use locale encoding intentionally (exercising edge cases). If we want to tighten tests later that's a separate PR. - plugins/ excluded: plugin-specific conventions may differ; plugin authors own their code. - optional-skills/ and skills/ excluded: skill scripts are user-authored and we don't want to mass-edit them. - website/ and tinker-atropos/ excluded: vendored / generated content. 46 files touched, 89 +/- lines (symmetric replacement). No behavior change on POSIX or on Windows when the file is ASCII; bug fix on Windows when the file contains non-ASCII.") | May 8, 2026 |
| [hermes_logging.py](https://github.com/NousResearch/hermes-agent/blob/main/hermes_logging.py "hermes_logging.py") | [hermes_logging.py](https://github.com/NousResearch/hermes-agent/blob/main/hermes_logging.py "hermes_logging.py") | [fix(logging): attach gateway log after cli init](https://github.com/NousResearch/hermes-agent/commit/88a85d30c1cf7c8731564bf5bd0ace243214c551 "fix(logging): attach gateway log after cli init") | Apr 27, 2026 |
| [hermes_state.py](https://github.com/NousResearch/hermes-agent/blob/main/hermes_state.py "hermes_state.py") | [hermes_state.py](https://github.com/NousResearch/hermes-agent/blob/main/hermes_state.py "hermes_state.py") | [fix: use AUTOINCREMENT id for message ordering instead of timestamp](https://github.com/NousResearch/hermes-agent/commit/c03acca508bd06c78761af2653ebef1a1448b307 "fix: use AUTOINCREMENT id for message ordering instead of timestamp On WSL2 (and similar environments), time.time() is not strictly monotonic due to NTP sync or host clock adjustments. When clock regression occurs during a multi-tool flush, later-inserted rows get earlier timestamps, causing ORDER BY timestamp, id to sort them before rows that were written first. This breaks the tool_calls/tool_response adjacency invariant and triggers HTTP 400 from the API. Use ORDER BY id instead, since id (INTEGER PRIMARY KEY AUTOINCREMENT) always reflects true insertion order regardless of system clock behavior.") | May 14, 2026 |
| [hermes_time.py](https://github.com/NousResearch/hermes-agent/blob/main/hermes_time.py "hermes_time.py") | [hermes_time.py](https://github.com/NousResearch/hermes-agent/blob/main/hermes_time.py "hermes_time.py") | [codebase: add encoding='utf-8' to all bare open() calls (PLW1514)](https://github.com/NousResearch/hermes-agent/commit/cbce5e93fcb9a923ab71f45d2a0f0f172dd54967 "codebase: add encoding='utf-8' to all bare open() calls (PLW1514) Closes the last Python-on-Windows UTF-8 exposure by making every text-mode open() call explicit about its encoding. Before: on Windows, bare open(path, 'r') defaults to the system locale encoding (cp1252 on US-locale installs). That means reading any config/yaml/markdown/json file with non-ASCII content either crashes with UnicodeDecodeError or silently mis-decodes bytes. After: all 89 affected call sites in production code now pass encoding='utf-8' explicitly. Works identically on every platform and every locale, no surprise behavior. Mechanical sweep via: ruff check --preview --extend-select PLW1514 --unsafe-fixes --fix --exclude 'tests,venv,.venv,node_modules,website,optional-skills, skills,tinker-atropos,plugins' . All 89 fixes have the same shape: open(x) or open(x, mode) became open(x, encoding='utf-8') or open(x, mode, encoding='utf-8'). Nothing else changed. Every modified file still parses and the Windows/sandbox test suite is still green (85 passed, 14 skipped, 0 failed across tests/tools/test_code_execution_windows_env.py + tests/tools/test_code_execution_modes.py + tests/tools/test_env_passthrough.py + tests/test_hermes_bootstrap.py). Scope notes: - tests/ excluded: test fixtures can use locale encoding intentionally (exercising edge cases). If we want to tighten tests later that's a separate PR. - plugins/ excluded: plugin-specific conventions may differ; plugin authors own their code. - optional-skills/ and skills/ excluded: skill scripts are user-authored and we don't want to mass-edit them. - website/ and tinker-atropos/ excluded: vendored / generated content. 46 files touched, 89 +/- lines (symmetric replacement). No behavior change on POSIX or on Windows when the file is ASCII; bug fix on Windows when the file contains non-ASCII.") | May 8, 2026 |
| [mcp_serve.py](https://github.com/NousResearch/hermes-agent/blob/main/mcp_serve.py "mcp_serve.py") | [mcp_serve.py](https://github.com/NousResearch/hermes-agent/blob/main/mcp_serve.py "mcp_serve.py") | [chore: ruff auto-fix PLR6201 — tuple → set in membership tests (](https://github.com/NousResearch/hermes-agent/commit/2ec8d2b42ffecec2128f1004c0a8451378057d42 "chore: ruff auto-fix PLR6201 — tuple → set in membership tests (#23937) Replace with for all literal-tuple membership tests. Set lookup is O(1) vs O(n) for tuple — consistent micro-optimization across the codebase. 608 instances fixed via `ruff --fix --unsafe-fixes`, 0 remaining. 133 files, +626/-626 (net zero).")[#23937](https://github.com/NousResearch/hermes-agent/pull/23937)[)](https://github.com/NousResearch/hermes-agent/commit/2ec8d2b42ffecec2128f1004c0a8451378057d42 "chore: ruff auto-fix PLR6201 — tuple → set in membership tests (#23937) Replace with for all literal-tuple membership tests. Set lookup is O(1) vs O(n) for tuple — consistent micro-optimization across the codebase. 608 instances fixed via `ruff --fix --unsafe-fixes`, 0 remaining. 133 files, +626/-626 (net zero).") | May 11, 2026 |
| [mini_swe_runner.py](https://github.com/NousResearch/hermes-agent/blob/main/mini_swe_runner.py "mini_swe_runner.py") | [mini_swe_runner.py](https://github.com/NousResearch/hermes-agent/blob/main/mini_swe_runner.py "mini_swe_runner.py") | [fix(kimi): omit temperature entirely for Kimi/Moonshot models (](https://github.com/NousResearch/hermes-agent/commit/3cba81ebed0d86fedd56913ab341f2d93d539f49 "fix(kimi): omit temperature entirely for Kimi/Moonshot models (#13157) Kimi's gateway selects the correct temperature server-side based on the active mode (thinking -> 1.0, non-thinking -> 0.6). Sending any temperature value — even the previously \"correct\" one — conflicts with gateway-managed defaults. Replaces the old approach of forcing specific temperature values (0.6 for non-thinking, 1.0 for thinking) with an OMIT_TEMPERATURE sentinel that tells all call sites to strip the temperature key from API kwargs entirely. Changes: - agent/auxiliary_client.py: OMIT_TEMPERATURE sentinel, _is_kimi_model() prefix check (covers all kimi-* models), _fixed_temperature_for_model() returns sentinel for kimi models. _build_call_kwargs() strips temp. - run_agent.py: _build_api_kwargs, flush_memories, and summary generation paths all handle the sentinel by popping/omitting temperature. - trajectory_compressor.py: _effective_temperature_for_model returns None for kimi (sentinel mapped), direct client calls use kwargs dict to conditionally include temperature. - mini_swe_runner.py: same sentinel handling via wrapper function. - 6 test files updated: all 'forces temperature X' assertions replaced with 'temperature not in kwargs' assertions. Net: -76 lines (171 added, 247 removed). Inspired by PR #13137 (@kshitijk4poor).")[#13157](https://github.com/NousResearch/hermes-agent/pull/13157)[)](https://github.com/NousResearch/hermes-agent/commit/3cba81ebed0d86fedd56913ab341f2d93d539f49 "fix(kimi): omit temperature entirely for Kimi/Moonshot models (#13157) Kimi's gateway selects the correct temperature server-side based on the active mode (thinking -> 1.0, non-thinking -> 0.6). Sending any temperature value — even the previously \"correct\" one — conflicts with gateway-managed defaults. Replaces the old approach of forcing specific temperature values (0.6 for non-thinking, 1.0 for thinking) with an OMIT_TEMPERATURE sentinel that tells all call sites to strip the temperature key from API kwargs entirely. Changes: - agent/auxiliary_client.py: OMIT_TEMPERATURE sentinel, _is_kimi_model() prefix check (covers all kimi-* models), _fixed_temperature_for_model() returns sentinel for kimi models. _build_call_kwargs() strips temp. - run_agent.py: _build_api_kwargs, flush_memories, and summary generation paths all handle the sentinel by popping/omitting temperature. - trajectory_compressor.py: _effective_temperature_for_model returns None for kimi (sentinel mapped), direct client calls use kwargs dict to conditionally include temperature. - mini_swe_runner.py: same sentinel handling via wrapper function. - 6 test files updated: all 'forces temperature X' assertions replaced with 'temperature not in kwargs' assertions. Net: -76 lines (171 added, 247 removed). Inspired by PR #13137 (@kshitijk4poor).") | Apr 20, 2026 |
| [model_tools.py](https://github.com/NousResearch/hermes-agent/blob/main/model_tools.py "model_tools.py") | [model_tools.py](https://github.com/NousResearch/hermes-agent/blob/main/model_tools.py "model_tools.py") | [security: sanitize tool error strings before injecting into model con…](https://github.com/NousResearch/hermes-agent/commit/627f8a5f1dab2847a5fb97fa79daa6d0bc96d8bd "security: sanitize tool error strings before injecting into model context (#26823) Adds _sanitize_tool_error() in model_tools and routes both error paths through it: registry.dispatch's try/except (the primary path for tool exceptions) and handle_function_call's outer except (defense in depth). Stripping targets structural framing tokens that the model itself can react to even though json.dumps already handles wire-layer escaping: XML role tags (tool_call, function_call, result, response, output, input, system, assistant, user), CDATA sections, and markdown code fences. Caps message body at 2000 chars and wraps with [TOOL_ERROR] prefix. Defense-in-depth: a tool exception carrying '<tool_call>...' won't break message framing (json escapes it), but the model still reads those tokens and they nudge it toward role-confusion framing. Ported from ironclaw#1639 (one piece of #3838's three-feature scout). The truncated-tool-call (#1632) and empty-response-recovery (#1677, #1720) pieces are skipped because main now implements both far more thoroughly (run_agent.py L8147/L12209/L13012 for truncation retry + length rewrite; L4500/L15090+ for empty-response scaffolding stripper, multi-stage nudge, fallback model activation).") | May 16, 2026 |
| [package-lock.json](https://github.com/NousResearch/hermes-agent/blob/main/package-lock.json "package-lock.json") | [package-lock.json](https://github.com/NousResearch/hermes-agent/blob/main/package-lock.json "package-lock.json") | [fix(update): make Camofox lazy-installed instead of eager (](https://github.com/NousResearch/hermes-agent/commit/05af78c53d553f6dd20012ce18eb0c2c02d346c9 "fix(update): make Camofox lazy-installed instead of eager (#27055) The `@askjo/camofox-browser` npm package was a top-level entry in the root `package.json` `dependencies` block, so `hermes update` ran its postinstall on every user, every update. That postinstall calls `npx camoufox-js fetch`, which silently downloads a ~300MB Firefox-fork browser binary from GitHub Releases — multi-minute on fast connections, and a hard block for users on slow / restricted networks (notably users in China running through a VPN). Camofox is an explicit opt-in browser backend. The runtime check in `tools/browser_tool.py` only routes through Camofox when the user has set `CAMOFOX_URL` (selected via `hermes tools` → Browser Automation → Camofox). Users who never opted in never touched the package at runtime, yet every `hermes update` paid for the binary fetch anyway. This change: * Removes `@askjo/camofox-browser` from root `package.json` dependencies (and the regenerated `package-lock.json` drops Camofox's entire transitive tree, ~2.6k lines). * Updates the Camofox `post_setup` handler in `hermes_cli/tools_config.py` to install `@askjo/camofox-browser@^1.5.2` explicitly when the user selects Camofox, and streams npm output (no `--silent`, no `capture_output`) so the ~300MB download is visible rather than appearing frozen. * Adds `tests/test_package_json_lazy_deps.py` as a regression guard so future PRs can't silently re-add Camofox (or any binary-postinstall package) to eager root dependencies. `agent-browser` stays eager — it is the default Chromium-driving backend used by every session that does not have a cloud browser provider configured, and its postinstall is small. Validation: | | Before | After | |---|---|---| | `hermes update` time on slow network | multi-minute hang at `→ Updating Node.js dependencies...` | seconds (no binary fetch) | | Camofox opt-in install visibility | silent, looked frozen | streamed npm output | | Regression guard against re-adding | none | `test_package_json_lazy_deps.py` | Tests: - `tests/test_package_json_lazy_deps.py`: 3/3 pass - `tests/tools/test_browser_camofox*`: 92/92 pass - `tests/hermes_cli/test_tools_config.py`: 66/66 pass - `tests/hermes_cli/test_cmd_update.py` + adjacent: green Reported by lulu (Discord, May 2026) — `hermes update` hangs at `→ Updating Node.js dependencies...` in China. Related: #18840, #18869.")[#27055](https://github.com/NousResearch/hermes-agent/pull/27055)[)](https://github.com/NousResearch/hermes-agent/commit/05af78c53d553f6dd20012ce18eb0c2c02d346c9 "fix(update): make Camofox lazy-installed instead of eager (#27055) The `@askjo/camofox-browser` npm package was a top-level entry in the root `package.json` `dependencies` block, so `hermes update` ran its postinstall on every user, every update. That postinstall calls `npx camoufox-js fetch`, which silently downloads a ~300MB Firefox-fork browser binary from GitHub Releases — multi-minute on fast connections, and a hard block for users on slow / restricted networks (notably users in China running through a VPN). Camofox is an explicit opt-in browser backend. The runtime check in `tools/browser_tool.py` only routes through Camofox when the user has set `CAMOFOX_URL` (selected via `hermes tools` → Browser Automation → Camofox). Users who never opted in never touched the package at runtime, yet every `hermes update` paid for the binary fetch anyway. This change: * Removes `@askjo/camofox-browser` from root `package.json` dependencies (and the regenerated `package-lock.json` drops Camofox's entire transitive tree, ~2.6k lines). * Updates the Camofox `post_setup` handler in `hermes_cli/tools_config.py` to install `@askjo/camofox-browser@^1.5.2` explicitly when the user selects Camofox, and streams npm output (no `--silent`, no `capture_output`) so the ~300MB download is visible rather than appearing frozen. * Adds `tests/test_package_json_lazy_deps.py` as a regression guard so future PRs can't silently re-add Camofox (or any binary-postinstall package) to eager root dependencies. `agent-browser` stays eager — it is the default Chromium-driving backend used by every session that does not have a cloud browser provider configured, and its postinstall is small. Validation: | | Before | After | |---|---|---| | `hermes update` time on slow network | multi-minute hang at `→ Updating Node.js dependencies...` | seconds (no binary fetch) | | Camofox opt-in install visibility | silent, looked frozen | streamed npm output | | Regression guard against re-adding | none | `test_package_json_lazy_deps.py` | Tests: - `tests/test_package_json_lazy_deps.py`: 3/3 pass - `tests/tools/test_browser_camofox*`: 92/92 pass - `tests/hermes_cli/test_tools_config.py`: 66/66 pass - `tests/hermes_cli/test_cmd_update.py` + adjacent: green Reported by lulu (Discord, May 2026) — `hermes update` hangs at `→ Updating Node.js dependencies...` in China. Related: #18840, #18869.") | May 16, 2026 |
| [package.json](https://github.com/NousResearch/hermes-agent/blob/main/package.json "package.json") | [package.json](https://github.com/NousResearch/hermes-agent/blob/main/package.json "package.json") | [fix(update): make Camofox lazy-installed instead of eager (](https://github.com/NousResearch/hermes-agent/commit/05af78c53d553f6dd20012ce18eb0c2c02d346c9 "fix(update): make Camofox lazy-installed instead of eager (#27055) The `@askjo/camofox-browser` npm package was a top-level entry in the root `package.json` `dependencies` block, so `hermes update` ran its postinstall on every user, every update. That postinstall calls `npx camoufox-js fetch`, which silently downloads a ~300MB Firefox-fork browser binary from GitHub Releases — multi-minute on fast connections, and a hard block for users on slow / restricted networks (notably users in China running through a VPN). Camofox is an explicit opt-in browser backend. The runtime check in `tools/browser_tool.py` only routes through Camofox when the user has set `CAMOFOX_URL` (selected via `hermes tools` → Browser Automation → Camofox). Users who never opted in never touched the package at runtime, yet every `hermes update` paid for the binary fetch anyway. This change: * Removes `@askjo/camofox-browser` from root `package.json` dependencies (and the regenerated `package-lock.json` drops Camofox's entire transitive tree, ~2.6k lines). * Updates the Camofox `post_setup` handler in `hermes_cli/tools_config.py` to install `@askjo/camofox-browser@^1.5.2` explicitly when the user selects Camofox, and streams npm output (no `--silent`, no `capture_output`) so the ~300MB download is visible rather than appearing frozen. * Adds `tests/test_package_json_lazy_deps.py` as a regression guard so future PRs can't silently re-add Camofox (or any binary-postinstall package) to eager root dependencies. `agent-browser` stays eager — it is the default Chromium-driving backend used by every session that does not have a cloud browser provider configured, and its postinstall is small. Validation: | | Before | After | |---|---|---| | `hermes update` time on slow network | multi-minute hang at `→ Updating Node.js dependencies...` | seconds (no binary fetch) | | Camofox opt-in install visibility | silent, looked frozen | streamed npm output | | Regression guard against re-adding | none | `test_package_json_lazy_deps.py` | Tests: - `tests/test_package_json_lazy_deps.py`: 3/3 pass - `tests/tools/test_browser_camofox*`: 92/92 pass - `tests/hermes_cli/test_tools_config.py`: 66/66 pass - `tests/hermes_cli/test_cmd_update.py` + adjacent: green Reported by lulu (Discord, May 2026) — `hermes update` hangs at `→ Updating Node.js dependencies...` in China. Related: #18840, #18869.")[#27055](https://github.com/NousResearch/hermes-agent/pull/27055)[)](https://github.com/NousResearch/hermes-agent/commit/05af78c53d553f6dd20012ce18eb0c2c02d346c9 "fix(update): make Camofox lazy-installed instead of eager (#27055) The `@askjo/camofox-browser` npm package was a top-level entry in the root `package.json` `dependencies` block, so `hermes update` ran its postinstall on every user, every update. That postinstall calls `npx camoufox-js fetch`, which silently downloads a ~300MB Firefox-fork browser binary from GitHub Releases — multi-minute on fast connections, and a hard block for users on slow / restricted networks (notably users in China running through a VPN). Camofox is an explicit opt-in browser backend. The runtime check in `tools/browser_tool.py` only routes through Camofox when the user has set `CAMOFOX_URL` (selected via `hermes tools` → Browser Automation → Camofox). Users who never opted in never touched the package at runtime, yet every `hermes update` paid for the binary fetch anyway. This change: * Removes `@askjo/camofox-browser` from root `package.json` dependencies (and the regenerated `package-lock.json` drops Camofox's entire transitive tree, ~2.6k lines). * Updates the Camofox `post_setup` handler in `hermes_cli/tools_config.py` to install `@askjo/camofox-browser@^1.5.2` explicitly when the user selects Camofox, and streams npm output (no `--silent`, no `capture_output`) so the ~300MB download is visible rather than appearing frozen. * Adds `tests/test_package_json_lazy_deps.py` as a regression guard so future PRs can't silently re-add Camofox (or any binary-postinstall package) to eager root dependencies. `agent-browser` stays eager — it is the default Chromium-driving backend used by every session that does not have a cloud browser provider configured, and its postinstall is small. Validation: | | Before | After | |---|---|---| | `hermes update` time on slow network | multi-minute hang at `→ Updating Node.js dependencies...` | seconds (no binary fetch) | | Camofox opt-in install visibility | silent, looked frozen | streamed npm output | | Regression guard against re-adding | none | `test_package_json_lazy_deps.py` | Tests: - `tests/test_package_json_lazy_deps.py`: 3/3 pass - `tests/tools/test_browser_camofox*`: 92/92 pass - `tests/hermes_cli/test_tools_config.py`: 66/66 pass - `tests/hermes_cli/test_cmd_update.py` + adjacent: green Reported by lulu (Discord, May 2026) — `hermes update` hangs at `→ Updating Node.js dependencies...` in China. Related: #18840, #18869.") | May 16, 2026 |
| [pyproject.toml](https://github.com/NousResearch/hermes-agent/blob/main/pyproject.toml "pyproject.toml") | [pyproject.toml](https://github.com/NousResearch/hermes-agent/blob/main/pyproject.toml "pyproject.toml") | [chore: release v0.14.0 (2026.5.16) (](https://github.com/NousResearch/hermes-agent/commit/a91a57fa5a13d516c38b07a141a9ce8a3daabeb0 "chore: release v0.14.0 (2026.5.16) (#26862) The Foundation Release — Hermes installs and runs anywhere now. Highlights: - Native Windows support (early beta) — PowerShell installer, native subprocess/PTY paths, ~40 follow-up Windows-only fixes - pip install hermes-agent — PyPI wheel - Cold-start wave — ~19s off hermes launch, 180x faster browser_console (CDP WS) - Supply-chain advisory checker + lazy-deps + tiered install fallback - OpenAI-compatible local proxy for OAuth providers (Claude Pro, ChatGPT Pro, SuperGrok) - Cross-session 1h Claude prompt cache (Anthropic / OpenRouter / Nous Portal) - 2 new platforms: LINE + SimpleX Chat (22 total) - Microsoft Graph foundation — Teams pipeline + webhook adapter - /handoff actually transfers sessions live - x_search first-class tool, vision_analyze pixel passthrough - LSP semantic diagnostics on every write - Unified video_generate with pluggable backends - computer_use cua-driver backend - 9 new optional skills, OpenRouter Pareto Code router, xAI Grok OAuth - 12 P0 + 50 P1 closures 808 commits · 633 PRs · 1393 files · 165k insertions · 545 issues closed · 215 contributors")[#26862](https://github.com/NousResearch/hermes-agent/pull/26862)[)](https://github.com/NousResearch/hermes-agent/commit/a91a57fa5a13d516c38b07a141a9ce8a3daabeb0 "chore: release v0.14.0 (2026.5.16) (#26862) The Foundation Release — Hermes installs and runs anywhere now. Highlights: - Native Windows support (early beta) — PowerShell installer, native subprocess/PTY paths, ~40 follow-up Windows-only fixes - pip install hermes-agent — PyPI wheel - Cold-start wave — ~19s off hermes launch, 180x faster browser_console (CDP WS) - Supply-chain advisory checker + lazy-deps + tiered install fallback - OpenAI-compatible local proxy for OAuth providers (Claude Pro, ChatGPT Pro, SuperGrok) - Cross-session 1h Claude prompt cache (Anthropic / OpenRouter / Nous Portal) - 2 new platforms: LINE + SimpleX Chat (22 total) - Microsoft Graph foundation — Teams pipeline + webhook adapter - /handoff actually transfers sessions live - x_search first-class tool, vision_analyze pixel passthrough - LSP semantic diagnostics on every write - Unified video_generate with pluggable backends - computer_use cua-driver backend - 9 new optional skills, OpenRouter Pareto Code router, xAI Grok OAuth - 12 P0 + 50 P1 closures 808 commits · 633 PRs · 1393 files · 165k insertions · 545 issues closed · 215 contributors") | May 16, 2026 |
| [run_agent.py](https://github.com/NousResearch/hermes-agent/blob/main/run_agent.py "run_agent.py") | [run_agent.py](https://github.com/NousResearch/hermes-agent/blob/main/run_agent.py "run_agent.py") | [fix(xai): surface provider 'error' SSE frame in Codex fallback stream (](https://github.com/NousResearch/hermes-agent/commit/aa05ffba530fde599b6515120578364cce682ac7 "fix(xai): surface provider 'error' SSE frame in Codex fallback stream (#27184) Original commit 2b193907d by Teknium added a new module-level _StreamErrorEvent class and threaded its raise into _run_codex_create_stream_fallback in pre-refactor run_agent.py. - _StreamErrorEvent class → run_agent.py (module-level, next to _qwen_portal_headers; class needs to be top-level for the codex runtime to import it) - The fallback event-loop's 'type=error' handler → agent/codex_runtime.py where run_codex_create_stream_fallback now lives. Imports _StreamErrorEvent lazily from run_agent to avoid circular import. Co-authored-by: Teknium <127238744+teknium1@users.noreply.github.com>")[…](https://github.com/NousResearch/hermes-agent/pull/27184) | May 17, 2026 |
| [setup-hermes.sh](https://github.com/NousResearch/hermes-agent/blob/main/setup-hermes.sh "setup-hermes.sh") | [setup-hermes.sh](https://github.com/NousResearch/hermes-agent/blob/main/setup-hermes.sh "setup-hermes.sh") | [chore: remove Atropos RL environments and tinker-atropos integration (](https://github.com/NousResearch/hermes-agent/commit/5af672c7530263544a9f5e2479f3853d83b3b798 "chore: remove Atropos RL environments and tinker-atropos integration (#26106) * chore: remove Atropos RL environments, tools, tests, skill, and tinker-atropos submodule Delete: - environments/ (43 files — base env, agent loop, tool call parsers, benchmarks) - rl_cli.py (standalone RL training CLI) - tools/rl_training_tool.py (all 10 rl_* tools) - tests: test_rl_training_tool, test_tool_call_parsers, test_managed_server_tool_support, test_agent_loop, test_agent_loop_vllm, test_agent_loop_tool_calling, test_terminalbench2_env_security - optional-skills/mlops/hermes-atropos-environments/ - tinker-atropos git submodule + .gitmodules * chore: remove RL/Atropos references from Python source - toolsets.py: remove rl toolset block + update comment - model_tools.py: remove rl_tools group + update async bridging comment - hermes_cli/tools_config.py: remove RL display entry, _DEFAULT_OFF_TOOLSETS, setup block, and rl_training post-setup handler - tools/budget_config.py: remove RL environment reference in docstring - tests/test_model_tools.py: remove rl_tools from expected groups - tests/run_agent/test_streaming_tool_call_repair.py: fix stale cross-reference * chore: remove rl/yc-bench extras and tinker-atropos refs from pyproject.toml - Remove rl extra (atroposlib, tinker, fastapi, uvicorn, wandb) - Remove yc-bench extra - Remove rl_cli from py-modules - Remove [tool.ty.src] exclude for tinker-atropos - Remove [tool.ruff] exclude for tinker-atropos - Regenerate uv.lock * chore: remove tinker-atropos from install/setup scripts - setup-hermes.sh: remove entire tinker-atropos submodule install block - scripts/install.sh: remove both tinker-atropos blocks (Termux + standard) - scripts/install.ps1: remove tinker-atropos block - nix/hermes-agent.nix: remove tinker-atropos pip install line * chore: remove RL references from cli-config.yaml.example * docs: remove Atropos/RL references from README, CONTRIBUTING, AGENTS.md * docs: remove RL/Atropos references from website - Delete: environments.md, rl-training.md, mlops-hermes-atropos-environments.md - sidebars.ts: remove rl-training and environments sidebar entries - optional-skills-catalog.md: remove hermes-atropos-environments row - tools-reference.md: remove entire rl toolset section - toolsets-reference.md: remove rl row + update example - integrations/index.md: remove RL Training bullet - architecture.md: remove environments/ from tree + RL section - contributing.md: remove tinker-atropos setup - updating.md: remove tinker-atropos install + stale submodule update * chore: remove remaining RL/Atropos stragglers - hermes_cli/config.py: remove TINKER_API_KEY + WANDB_API_KEY env var defs - hermes_cli/doctor.py: remove Submodules check section (tinker-atropos) - hermes_cli/setup.py: remove RL Training status check - hermes_cli/status.py: remove Tinker + WandB from API key status display - agent/display.py: remove both rl_* tool preview/activity blocks - website/docs: remove RL references from providers.md + env-variables.md - tests: remove TINKER_API_KEY from conftest, set_config_value, setup_script * chore: remove RL training section from .env.example")[#…](https://github.com/NousResearch/hermes-agent/pull/26106) | May 15, 2026 |
| [toolset_distributions.py](https://github.com/NousResearch/hermes-agent/blob/main/toolset_distributions.py "toolset_distributions.py") | [toolset_distributions.py](https://github.com/NousResearch/hermes-agent/blob/main/toolset_distributions.py "toolset_distributions.py") | [chore: fix 154 f-strings, simplify getattr/URL patterns, remove dead …](https://github.com/NousResearch/hermes-agent/commit/cbf195e8066c14ad09e35ce458e888108c5a56f8 "chore: fix 154 f-strings, simplify getattr/URL patterns, remove dead code (#3119) Three categories of cleanup, all zero-behavioral-change: 1. F-strings without placeholders (154 fixes across 29 files) - Converted f'...' to '...' where no {expression} was present - Heaviest files: run_agent.py (24), cli.py (20), honcho_integration/cli.py (34) 2. Simplify defensive patterns in run_agent.py - Added explicit self._is_anthropic_oauth = False in __init__ (before the api_mode branch that conditionally sets it) - Replaced 7x getattr(self, '_is_anthropic_oauth', False) with direct self._is_anthropic_oauth (attribute always initialized now) - Added _is_openrouter_url() and _is_anthropic_url() helper methods - Replaced 3 inline 'openrouter' in self._base_url_lower checks 3. Remove dead code in small files - hermes_cli/claw.py: removed unused 'total' computation - tools/fuzzy_match.py: removed unused strip_indent() function and pattern_stripped variable Full test suite: 6184 passed, 0 failures E2E PTY: banner clean, tool calls work, zero garbled ANSI") | Mar 26, 2026 |
| [toolsets.py](https://github.com/NousResearch/hermes-agent/blob/main/toolsets.py "toolsets.py") | [toolsets.py](https://github.com/NousResearch/hermes-agent/blob/main/toolsets.py "toolsets.py") | [feat(x_search): gated X (Twitter) search tool with OAuth-or-API-key a…](https://github.com/NousResearch/hermes-agent/commit/74d0b392e7a87c869d9e13cf3eba5d809d8ff1fa "feat(x_search): gated X (Twitter) search tool with OAuth-or-API-key auth (#26763) * feat(x_search): gated X (Twitter) search tool with OAuth-or-API-key auth Salvages tools/x_search_tool.py from the closed PR #10786 (originally by @Jaaneek) and reworks its credential resolution so the tool registers when EITHER xAI credential path is available: * XAI_API_KEY (paid xAI API key) is set in ~/.hermes/.env or the env, OR * The user is signed in via xAI Grok OAuth — SuperGrok subscription — i.e. hermes auth add xai-oauth has been run Both paths route through xAI's built-in x_search Responses tool at https://api.x.ai/v1/responses. When both credentials exist OAuth wins, matching tools/xai_http.py's existing preference order (uses SuperGrok quota instead of paid API spend). The check_fn calls resolve_xai_http_credentials() which auto-refreshes the OAuth access token if it's within the refresh skew window, so a True return means the bearer is fetchable AND non-empty. Wiring - tools/x_search_tool.py — new tool, ~370 LOC. Schema gated by check_fn, bearer resolved per-call so revoked OAuth surfaces a clean tool_error rather than an HTTP 401. - toolsets.py — \"x_search\" toolset def. NOT added to _HERMES_CORE_TOOLS; users opt in via hermes tools. - hermes_cli/tools_config.py — CONFIGURABLE_TOOLSETS entry + TOOL_CATEGORIES block with two provider options (OAuth + API key) sharing the existing xai_grok post_setup hook for credential bootstrap. - hermes_cli/config.py — DEFAULT_CONFIG[\"x_search\"] with model / timeout_seconds / retries. Additive nested key; no version bump. - tests/tools/test_x_search_tool.py — 13 tests covering HTTP shape, handle validation, citation extraction, 4xx/5xx/timeout handling, and the full credential-resolution matrix (OAuth-only, API-key-only, both-set, neither-set, resolver-raises, config overrides, registry registration). - website/docs/guides/xai-grok-oauth.md — adds X Search to the direct-to-xAI tools section with off-by-default note. - website/docs/user-guide/features/tools.md — new row in the tools table. Off by default — users enable via `hermes tools` → 🐦 X (Twitter) Search. Schema only appears to the model when xAI credentials are configured. Co-authored-by: Jaaneek <Jaaneek@users.noreply.github.com> * docs(x_search): add dedicated feature page + reference entries - website/docs/user-guide/features/x-search.md (new) — full feature walkthrough: authentication, enablement, configuration, parameters, returned fields, example, troubleshooting, see-also links. - website/docs/reference/tools-reference.md — new \"x_search\" toolset section with parameter docs and credential gating note. - website/docs/reference/toolsets-reference.md — new row in the toolset catalog table. - website/sidebars.ts — wires the new feature page under Media & Web, after web-search. --------- Co-authored-by: Jaaneek <Jaaneek@users.noreply.github.com>") | May 16, 2026 |
| [trajectory_compressor.py](https://github.com/NousResearch/hermes-agent/blob/main/trajectory_compressor.py "trajectory_compressor.py") | [trajectory_compressor.py](https://github.com/NousResearch/hermes-agent/blob/main/trajectory_compressor.py "trajectory_compressor.py") | [codebase: add encoding='utf-8' to all bare open() calls (PLW1514)](https://github.com/NousResearch/hermes-agent/commit/cbce5e93fcb9a923ab71f45d2a0f0f172dd54967 "codebase: add encoding='utf-8' to all bare open() calls (PLW1514) Closes the last Python-on-Windows UTF-8 exposure by making every text-mode open() call explicit about its encoding. Before: on Windows, bare open(path, 'r') defaults to the system locale encoding (cp1252 on US-locale installs). That means reading any config/yaml/markdown/json file with non-ASCII content either crashes with UnicodeDecodeError or silently mis-decodes bytes. After: all 89 affected call sites in production code now pass encoding='utf-8' explicitly. Works identically on every platform and every locale, no surprise behavior. Mechanical sweep via: ruff check --preview --extend-select PLW1514 --unsafe-fixes --fix --exclude 'tests,venv,.venv,node_modules,website,optional-skills, skills,tinker-atropos,plugins' . All 89 fixes have the same shape: open(x) or open(x, mode) became open(x, encoding='utf-8') or open(x, mode, encoding='utf-8'). Nothing else changed. Every modified file still parses and the Windows/sandbox test suite is still green (85 passed, 14 skipped, 0 failed across tests/tools/test_code_execution_windows_env.py + tests/tools/test_code_execution_modes.py + tests/tools/test_env_passthrough.py + tests/test_hermes_bootstrap.py). Scope notes: - tests/ excluded: test fixtures can use locale encoding intentionally (exercising edge cases). If we want to tighten tests later that's a separate PR. - plugins/ excluded: plugin-specific conventions may differ; plugin authors own their code. - optional-skills/ and skills/ excluded: skill scripts are user-authored and we don't want to mass-edit them. - website/ and tinker-atropos/ excluded: vendored / generated content. 46 files touched, 89 +/- lines (symmetric replacement). No behavior change on POSIX or on Windows when the file is ASCII; bug fix on Windows when the file contains non-ASCII.") | May 8, 2026 |
| [utils.py](https://github.com/NousResearch/hermes-agent/blob/main/utils.py "utils.py") | [utils.py](https://github.com/NousResearch/hermes-agent/blob/main/utils.py "utils.py") | [fix(cli): preserve config comments on setting writes](https://github.com/NousResearch/hermes-agent/commit/85383c6363096d052e73b54ed2646673f8676dfe "fix(cli): preserve config comments on setting writes") | May 10, 2026 |
| [uv.lock](https://github.com/NousResearch/hermes-agent/blob/main/uv.lock "uv.lock") | [uv.lock](https://github.com/NousResearch/hermes-agent/blob/main/uv.lock "uv.lock") | [security(deps): bump aiohttp, anthropic, cryptography to CVE-fixed ve…](https://github.com/NousResearch/hermes-agent/commit/d725407c5645c84607df552da5175e9a628b9bf9 "security(deps): bump aiohttp, anthropic, cryptography to CVE-fixed versions (#26830) Closes #10695. Picks up the still-vulnerable Python pins on current main: - aiohttp 3.13.3 -> 3.13.4 (messaging, slack, homeassistant, sms extras + lazy_deps platform.slack) — CVE-2026-34513 (DNS cache exhaustion), CVE-2026-34518 (cookie/proxy-auth leak on cross-origin redirect, relevant for the gateway since it handles OAuth tokens), CVE-2026-34519 (response reason injection), CVE-2026-34520 (null bytes in headers), CVE-2026-34525 (multiple Host headers). - anthropic 0.86.0 -> 0.87.0 (anthropic extra + lazy_deps provider.anthropic) — CVE-2026-34450 (memory tool files created mode 0o666), CVE-2026-34452 (path-traversal in async local-filesystem memory tool). Not directly exploitable since hermes-agent doesn't use the SDK's filesystem memory tool, but the SDK is bumped for hygiene. - cryptography pinned explicitly at 46.0.7 in core dependencies — CVE-2026-39892 (buffer overflow on non-contiguous buffers). Previously came in transitively via PyJWT[crypto]; the explicit floor keeps the WeCom/Weixin crypto paths from drifting below the fix. curl-cffi from the original issue is no longer in pyproject.toml or uv.lock, so no action needed there. uv.lock regenerated cleanly; only aiohttp / anthropic / cryptography moved. Credit: original issue + scoping by @shaun0927 (#10695, #10701). Floor analysis and packaging-surface audit by @gnanirahulnutakki (#10784), adapted to current main's exact-pin style. Co-authored-by: shaun0927 <shaun0927@users.noreply.github.com> Co-authored-by: Gnani Rahul Nutakki <gnanirahulnutakki@users.noreply.github.com>") | May 16, 2026 |
| View all files |

## Repository files navigation

*   [README](https://github.com/NousResearch/hermes-agent#)
*   [Contributing](https://github.com/NousResearch/hermes-agent#)
*   [MIT license](https://github.com/NousResearch/hermes-agent#)
*   [Security](https://github.com/NousResearch/hermes-agent#)

[![Image 2: Hermes Agent](https://github.com/NousResearch/hermes-agent/raw/main/assets/banner.png)](https://github.com/NousResearch/hermes-agent/blob/main/assets/banner.png)

# Hermes Agent ☤

[](https://github.com/NousResearch/hermes-agent#hermes-agent-)

[![Image 3: Documentation](https://camo.githubusercontent.com/76d7a880842f286c4d4e07baf2db1046197c6cfaa564365e912938445fc54a32/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f63732d6865726d65732d2d6167656e742e6e6f757372657365617263682e636f6d2d4646443730303f7374796c653d666f722d7468652d6261646765)](https://hermes-agent.nousresearch.com/docs/)[![Image 4: Discord](https://camo.githubusercontent.com/8c0fca73564f21d7a6f235747eb4d739a2e4aaa348b8e074904127baeb944b9e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446973636f72642d3538363546323f7374796c653d666f722d7468652d6261646765266c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465)](https://discord.gg/NousResearch)[![Image 5: License: MIT](https://camo.githubusercontent.com/153acf9dff19deb8abfc598c53bac50a4ceae0f5c83a552711060d3d78d2c057/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d677265656e3f7374796c653d666f722d7468652d6261646765)](https://github.com/NousResearch/hermes-agent/blob/main/LICENSE)[![Image 6: Built by Nous Research](https://camo.githubusercontent.com/6195af06150f2173f79d16fa3462ccac43c7dbf78f06f3c7997dc4090d79b9ad/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4275696c7425323062792d4e6f757325323052657365617263682d626c756576696f6c65743f7374796c653d666f722d7468652d6261646765)](https://nousresearch.com/)[![Image 7: 中文](https://camo.githubusercontent.com/574634232e93a1f4f7399d7056282748bde9c89ff98c338cc9bec8101117832b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c616e672de4b8ade696872d7265643f7374796c653d666f722d7468652d6261646765)](https://github.com/NousResearch/hermes-agent/blob/main/README.zh-CN.md)

**The self-improving AI agent built by [Nous Research](https://nousresearch.com/).** It's the only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle. It's not tied to your laptop — talk to it from Telegram while it works on a cloud VM.

Use any model you want — [Nous Portal](https://portal.nousresearch.com/), [OpenRouter](https://openrouter.ai/) (200+ models), [NovitaAI](https://novita.ai/) (AI-native cloud for Model API, Agent Sandbox, and GPU Cloud), [NVIDIA NIM](https://build.nvidia.com/) (Nemotron), [Xiaomi MiMo](https://platform.xiaomimimo.com/), [z.ai/GLM](https://z.ai/), [Kimi/Moonshot](https://platform.moonshot.ai/), [MiniMax](https://www.minimax.io/), [Hugging Face](https://huggingface.co/), OpenAI, or your own endpoint. Switch with `hermes model` — no code changes, no lock-in.

**A real terminal interface**Full TUI with multiline editing, slash-command autocomplete, conversation history, interrupt-and-redirect, and streaming tool output.
**Lives where you do**Telegram, Discord, Slack, WhatsApp, Signal, and CLI — all from a single gateway process. Voice memo transcription, cross-platform conversation continuity.
**A closed learning loop**Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use. FTS5 session search with LLM summarization for cross-session recall. [Honcho](https://github.com/plastic-labs/honcho) dialectic user modeling. Compatible with the [agentskills.io](https://agentskills.io/) open standard.
**Scheduled automations**Built-in cron scheduler with delivery to any platform. Daily reports, nightly backups, weekly audits — all in natural language, running unattended.
**Delegates and parallelizes**Spawn isolated subagents for parallel workstreams. Write Python scripts that call tools via RPC, collapsing multi-step pipelines into zero-context-cost turns.
**Runs anywhere, not just your laptop**Seven terminal backends — local, Docker, SSH, Singularity, Modal, Daytona, and Vercel Sandbox. Daytona and Modal offer serverless persistence — your agent's environment hibernates when idle and wakes on demand, costing nearly nothing between sessions. Run it on a $5 VPS or a GPU cluster.
**Research-ready**Batch trajectory generation, trajectory compression for training the next generation of tool-calling models.

* * *

## Quick Install

[](https://github.com/NousResearch/hermes-agent#quick-install)

### Linux, macOS, WSL2, Termux

[](https://github.com/NousResearch/hermes-agent#linux-macos-wsl2-termux)

undefinedshell
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
undefined

### Windows (native, PowerShell) — Early Beta

[](https://github.com/NousResearch/hermes-agent#windows-native-powershell--early-beta)

> **Heads up:** Native Windows support is **early beta**. It installs and runs, but hasn't been road-tested as broadly as our Linux/macOS/WSL2 paths. Please [file issues](https://github.com/NousResearch/hermes-agent/issues) when you hit rough edges. For the most battle-tested Windows setup today, run the Linux/macOS one-liner above inside **WSL2**.

Run this in PowerShell:

undefinedpowershell
irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex
undefined

The installer handles everything: uv, Python 3.11, Node.js, ripgrep, ffmpeg, **and a portable Git Bash** (MinGit, unpacked to `%LOCALAPPDATA%\hermes\git` — no admin required, completely isolated from any system Git install). Hermes uses this bundled Git Bash to run shell commands.

If you already have Git installed, the installer detects it and uses that instead. Otherwise a ~45MB MinGit download is all you need — it won't touch or interfere with any system Git.

> **Android / Termux:** The tested manual path is documented in the [Termux guide](https://hermes-agent.nousresearch.com/docs/getting-started/termux). On Termux, Hermes installs a curated `.[termux]` extra because the full `.[all]` extra currently pulls Android-incompatible voice dependencies.
> 
> 
> **Windows:** Native Windows is supported as an **early beta** — the PowerShell one-liner above installs everything, but expect rough edges and please file issues when you hit them. If you'd rather use WSL2 (our most battle-tested Windows path), the Linux command works there too. Native Windows install lives under `%LOCALAPPDATA%\hermes`; WSL2 installs under `~/.hermes` as on Linux. The only Hermes feature that currently needs WSL2 specifically is the browser-based dashboard chat pane (it uses a POSIX PTY — classic CLI and gateway both run natively).

After installation:

undefinedshell
source ~/.bashrc    # reload shell (or: source ~/.zshrc)
hermes              # start chatting!
undefined

* * *

## Getting Started

[](https://github.com/NousResearch/hermes-agent#getting-started)

undefinedshell
hermes              # Interactive CLI — start a conversation
hermes model        # Choose your LLM provider and model
hermes tools        # Configure which tools are enabled
hermes config set   # Set individual config values
hermes gateway      # Start the messaging gateway (Telegram, Discord, etc.)
hermes setup        # Run the full setup wizard (configures everything at once)
hermes claw migrate # Migrate from OpenClaw (if coming from OpenClaw)
hermes update       # Update to the latest version
hermes doctor       # Diagnose any issues
undefined

📖 **[Full documentation →](https://hermes-agent.nousresearch.com/docs/)**

## CLI vs Messaging Quick Reference

[](https://github.com/NousResearch/hermes-agent#cli-vs-messaging-quick-reference)

Hermes has two entry points: start the terminal UI with `hermes`, or run the gateway and talk to it from Telegram, Discord, Slack, WhatsApp, Signal, or Email. Once you're in a conversation, many slash commands are shared across both interfaces.

| Action | CLI | Messaging platforms |
| --- | --- | --- |
| Start chatting | `hermes` | Run `hermes gateway setup` + `hermes gateway start`, then send the bot a message |
| Start fresh conversation | `/new` or `/reset` | `/new` or `/reset` |
| Change model | `/model [provider:model]` | `/model [provider:model]` |
| Set a personality | `/personality [name]` | `/personality [name]` |
| Retry or undo the last turn | `/retry`, `/undo` | `/retry`, `/undo` |
| Compress context / check usage | `/compress`, `/usage`, `/insights [--days N]` | `/compress`, `/usage`, `/insights [days]` |
| Browse skills | `/skills` or `/<skill-name>` | `/<skill-name>` |
| Interrupt current work | `Ctrl+C` or send a new message | `/stop` or send a new message |
| Platform-specific status | `/platforms` | `/status`, `/sethome` |

For the full command lists, see the [CLI guide](https://hermes-agent.nousresearch.com/docs/user-guide/cli) and the [Messaging Gateway guide](https://hermes-agent.nousresearch.com/docs/user-guide/messaging).

* * *

## Documentation

[](https://github.com/NousResearch/hermes-agent#documentation)

All documentation lives at **[hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs/)**:

| Section | What's Covered |
| --- | --- |
| [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart) | Install → setup → first conversation in 2 minutes |
| [CLI Usage](https://hermes-agent.nousresearch.com/docs/user-guide/cli) | Commands, keybindings, personalities, sessions |
| [Configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration) | Config file, providers, models, all options |
| [Messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging) | Telegram, Discord, Slack, WhatsApp, Signal, Home Assistant |
| [Security](https://hermes-agent.nousresearch.com/docs/user-guide/security) | Command approval, DM pairing, container isolation |
| [Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools) | 40+ tools, toolset system, terminal backends |
| [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) | Procedural memory, Skills Hub, creating skills |
| [Memory](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory) | Persistent memory, user profiles, best practices |
| [MCP Integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) | Connect any MCP server for extended capabilities |
| [Cron Scheduling](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) | Scheduled tasks with platform delivery |
| [Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files) | Project context that shapes every conversation |
| [Architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture) | Project structure, agent loop, key classes |
| [Contributing](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing) | Development setup, PR process, code style |
| [CLI Reference](https://hermes-agent.nousresearch.com/docs/reference/cli-commands) | All commands and flags |
| [Environment Variables](https://hermes-agent.nousresearch.com/docs/reference/environment-variables) | Complete env var reference |

* * *

## Migrating from OpenClaw

[](https://github.com/NousResearch/hermes-agent#migrating-from-openclaw)

If you're coming from OpenClaw, Hermes can automatically import your settings, memories, skills, and API keys.

**During first-time setup:** The setup wizard (`hermes setup`) automatically detects `~/.openclaw` and offers to migrate before configuration begins.

**Anytime after install:**

undefinedshell
hermes claw migrate              # Interactive migration (full preset)
hermes claw migrate --dry-run    # Preview what would be migrated
hermes claw migrate --preset user-data   # Migrate without secrets
hermes claw migrate --overwrite  # Overwrite existing conflicts
undefined

What gets imported:

*   **SOUL.md** — persona file
*   **Memories** — MEMORY.md and USER.md entries
*   **Skills** — user-created skills → `~/.hermes/skills/openclaw-imports/`
*   **Command allowlist** — approval patterns
*   **Messaging settings** — platform configs, allowed users, working directory
*   **API keys** — allowlisted secrets (Telegram, OpenRouter, OpenAI, Anthropic, ElevenLabs)
*   **TTS assets** — workspace audio files
*   **Workspace instructions** — AGENTS.md (with `--workspace-target`)

See `hermes claw migrate --help` for all options, or use the `openclaw-migration` skill for an interactive agent-guided migration with dry-run previews.

* * *

## Contributing

[](https://github.com/NousResearch/hermes-agent#contributing)

We welcome contributions! See the [Contributing Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing) for development setup, code style, and PR process.

Quick start for contributors — clone and go with `setup-hermes.sh`:

undefinedshell
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
./setup-hermes.sh     # installs uv, creates venv, installs .[all], symlinks ~/.local/bin/hermes
./hermes              # auto-detects the venv, no need to `source` first
undefined

Manual path (equivalent to the above):

undefinedshell
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[all,dev]"
scripts/run_tests.sh
undefined

* * *

## Community

[](https://github.com/NousResearch/hermes-agent#community)

*   💬 [Discord](https://discord.gg/NousResearch)
*   📚 [Skills Hub](https://agentskills.io/)
*   🐛 [Issues](https://github.com/NousResearch/hermes-agent/issues)
*   🔌 [computer-use-linux](https://github.com/avifenesh/computer-use-linux) — Linux desktop-control MCP server for Hermes and other MCP hosts, with AT-SPI accessibility trees, Wayland/X11 input, screenshots, and compositor window targeting.
*   🔌 [HermesClaw](https://github.com/AaronWong1999/hermesclaw) — Community WeChat bridge: Run Hermes Agent and OpenClaw on the same WeChat account.

* * *

## License

[](https://github.com/NousResearch/hermes-agent#license)

MIT — see [LICENSE](https://github.com/NousResearch/hermes-agent/blob/main/LICENSE).

Built by [Nous Research](https://nousresearch.com/).

## About

The agent that grows with you

[hermes-agent.nousresearch.com](https://hermes-agent.nousresearch.com/ "https://hermes-agent.nousresearch.com")

### Topics

[ai](https://github.com/topics/ai "Topic: ai")[openai](https://github.com/topics/openai "Topic: openai")[hermes](https://github.com/topics/hermes "Topic: hermes")[codex](https://github.com/topics/codex "Topic: codex")[ai-agents](https://github.com/topics/ai-agents "Topic: ai-agents")[claude](https://github.com/topics/claude "Topic: claude")[ai-agent](https://github.com/topics/ai-agent "Topic: ai-agent")[llm](https://github.com/topics/llm "Topic: llm")[chatgpt](https://github.com/topics/chatgpt "Topic: chatgpt")[anthropic](https://github.com/topics/anthropic "Topic: anthropic")[claude-code](https://github.com/topics/claude-code "Topic: claude-code")[clawdbot](https://github.com/topics/clawdbot "Topic: clawdbot")[moltbot](https://github.com/topics/moltbot "Topic: moltbot")[openclaw](https://github.com/topics/openclaw "Topic: openclaw")[hermes-agent](https://github.com/topics/hermes-agent "Topic: hermes-agent")[nous-research](https://github.com/topics/nous-research "Topic: nous-research")

### Resources

[Readme](https://github.com/NousResearch/hermes-agent#readme-ov-file)

### License

[MIT license](https://github.com/NousResearch/hermes-agent#MIT-1-ov-file)

### Contributing

[Contributing](https://github.com/NousResearch/hermes-agent#contributing-ov-file)

### Security policy

[Security policy](https://github.com/NousResearch/hermes-agent#security-ov-file)

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/NousResearch/hermes-agent).

[Activity](https://github.com/NousResearch/hermes-agent/activity)

[Custom properties](https://github.com/NousResearch/hermes-agent/custom-properties)

### Stars

[**154k** stars](https://github.com/NousResearch/hermes-agent/stargazers)

### Watchers

[**587** watching](https://github.com/NousResearch/hermes-agent/watchers)

### Forks

[**24.6k** forks](https://github.com/NousResearch/hermes-agent/forks)

[Report repository](https://github.com/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FNousResearch%2Fhermes-agent&report=NousResearch+%28user%29)

## [Releases 13](https://github.com/NousResearch/hermes-agent/releases)

[Hermes Agent v0.14.0 (2026.5.16) Latest May 16, 2026](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.16)

[+ 12 releases](https://github.com/NousResearch/hermes-agent/releases)

## [Packages 0](https://github.com/orgs/NousResearch/packages?repo_name=hermes-agent)

 No packages published 

### Uh oh!

There was an error while loading. [Please reload this page](https://github.com/NousResearch/hermes-agent).

## [Contributors 1,056](https://github.com/NousResearch/hermes-agent/graphs/contributors)

*   [![Image 8: @teknium1](https://avatars.githubusercontent.com/u/127238744?s=64&v=4)](https://github.com/teknium1)
*   [![Image 9: @OutThisLife](https://avatars.githubusercontent.com/u/770929?s=64&v=4)](https://github.com/OutThisLife)
*   [![Image 10: @kshitijk4poor](https://avatars.githubusercontent.com/u/82637225?s=64&v=4)](https://github.com/kshitijk4poor)
*   [![Image 11: @0xbyt4](https://avatars.githubusercontent.com/u/35742124?s=64&v=4)](https://github.com/0xbyt4)
*   [![Image 12: @claude](https://avatars.githubusercontent.com/u/81847?s=64&v=4)](https://github.com/claude)
*   [![Image 13: @alt-glitch](https://avatars.githubusercontent.com/u/52913345?s=64&v=4)](https://github.com/alt-glitch)
*   [![Image 14: @helix4u](https://avatars.githubusercontent.com/u/4317663?s=64&v=4)](https://github.com/helix4u)
*   [![Image 15: @austinpickett](https://avatars.githubusercontent.com/u/260188?s=64&v=4)](https://github.com/austinpickett)
*   [![Image 16: @ethernet8023](https://avatars.githubusercontent.com/u/666465?s=64&v=4)](https://github.com/ethernet8023)
*   [![Image 17: @erosika](https://avatars.githubusercontent.com/u/56565191?s=64&v=4)](https://github.com/erosika)
*   [![Image 18: @SHL0MS](https://avatars.githubusercontent.com/u/131039422?s=64&v=4)](https://github.com/SHL0MS)
*   [![Image 19: @ygd58](https://avatars.githubusercontent.com/u/78954051?s=64&v=4)](https://github.com/ygd58)
*   [![Image 20: @briandevans](https://avatars.githubusercontent.com/u/252620095?s=64&v=4)](https://github.com/briandevans)
*   [![Image 21: @LeonSGP43](https://avatars.githubusercontent.com/u/154585401?s=64&v=4)](https://github.com/LeonSGP43)

[+ 1,042 contributors](https://github.com/NousResearch/hermes-agent/graphs/contributors)

## Languages

*   [Python 88.0%](https://github.com/NousResearch/hermes-agent/search?l=python)
*   [TypeScript 8.8%](https://github.com/NousResearch/hermes-agent/search?l=typescript)
*   [TeX 1.2%](https://github.com/NousResearch/hermes-agent/search?l=tex)
*   [Shell 0.6%](https://github.com/NousResearch/hermes-agent/search?l=shell)
*   [BibTeX Style 0.4%](https://github.com/NousResearch/hermes-agent/search?l=bibtex-style)
*   [PowerShell 0.3%](https://github.com/NousResearch/hermes-agent/search?l=powershell)
*   Other 0.7%

## Footer

[](https://github.com/) © 2026 GitHub,Inc. 

### Footer navigation

*   [Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)
*   [Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)
*   [Security](https://github.com/security)
*   [Status](https://www.githubstatus.com/)
*   [Community](https://github.community/)
*   [Docs](https://docs.github.com/)
*   [Contact](https://support.github.com/?tags=dotcom-footer)
*    Manage cookies 
*    Do not share my personal information 

 You can’t perform that action at this time.

---

### online search

<sub>5/17/2026, 10:11:24 AM</sub>

The NousResearch Hermes Agent is an open-source, self-improving artificial intelligence agent designed to "grow with you" by learning and becoming more capable over time. Unlike typical chatbots or coding copilots, Hermes Agent operates as a persistent, autonomous entity that retains knowledge across sessions.

### Core Features

The Hermes Agent boasts a rich set of capabilities that extend beyond basic conversational AI:

*   **Persistent Memory and Learning Loop:** A cornerstone of Hermes Agent is its ability to curate memory and persist it across sessions. It features a closed learning loop where it creates skills autonomously from complex tasks, refines them through use, and nudges itself to retain knowledge. This allows it to build a deepening model of the user and their environment over time.
*   **Autonomous Skill Creation:** When the agent successfully completes a complex task, it codifies the sequence of steps, tool calls, and reasoning into reusable "Skill" documents, which are markdown files it references for similar future tasks. This eliminates the need for repeated explanations and allows the agent to write its own operational knowledge.
*   **Multi-Platform Messaging Gateway:** Hermes Agent offers a single gateway process that supports continuous conversations across various platforms, including Telegram, Discord, Slack, WhatsApp, Signal, and a command-line interface (CLI). It also includes voice memo transcription.
*   **Scheduled Automations:** It includes a built-in cron scheduler that supports natural-language-defined daily reports, nightly backups, and weekly audits, capable of running unattended and delivering to any platform.
*   **Subagent Delegation and Parallelization:** Users can spawn isolated subagents for parallel workstreams, enabling complex multi-step pipelines to be collapsed into efficient turns.
*   **Comprehensive Terminal UI:** The agent provides a full terminal user interface with features like multiline editing, slash-command autocomplete, conversation history, and streaming tool output.
*   **Browser Automation and Vision:** Hermes Agent supports full browser automation with various backends, allowing it to navigate websites, fill forms, and extract information. It also offers multimodal vision support, enabling it to analyze and work with images.
*   **Extensive Toolset and Provider Flexibility:** It comes with over 40 built-in tools and supports free switching between multiple large language model (LLM) providers, including Nous Portal, OpenRouter, OpenAI, Anthropic, and custom endpoints, preventing vendor lock-in.

### Function Calling Capabilities

Advanced function calling is a significant strength of the Hermes model family, particularly highlighted in Hermes 2 Pro and Hermes 3. These models are designed to enable AI agents to execute API calls directly from user instructions. This means that when a user makes a request, the agent can interpret it, generate the necessary function call (e.g., `search_flights`), and return the results. The Hermes Function-Calling Standard facilitates the creation of LLM agents capable of direct interactions with APIs, enhancing their utility in various digital assistant roles. The training data for models like Hermes 2 Pro includes structured output and function-calling conversations, JSON mode, agentic JSON mode, and structured extraction samples, specifically designed to train LLMs in performing these functions based on natural language instructions.

### Philosophy Behind the Hermes Model Family

The core philosophy driving the Hermes model family by NousResearch is rooted in the open-source movement and a strong emphasis on user control and autonomy. This includes:

*   **"Grows With You" Principle:** The central idea is to create AI agents that are not static but continuously learn and improve from experience, becoming more valuable the longer they run.
*   **Open-Source and Accessibility:** NousResearch makes its models, such as Hermes 4, openly available through platforms like Hugging Face, promoting transparency and democratizing access to advanced AI capabilities.
*   **Neutral Alignment and User Control:** The Hermes models prioritize user-aligned steerability and aim for minimal content restrictions, offering "neutral alignment" rather than imposing blanket "safe-by-default" refusals. This philosophy emphasizes that the AI should be aligned with user intent rather than corporate policy layers, which NousResearch argues can stifle creativity and innovation.
*   **Persistent Capability:** The focus is on building persistent capability across sessions through long-term memory and reusable skills, rather than merely functioning as session-based tools.
*   **Advancing AI Reasoning:** Models like Hermes 4 introduce "hybrid reasoning," allowing users to toggle between fast responses and deeper, step-by-step thinking processes, providing transparency into the AI's thought process.

In essence, NousResearch aims to provide powerful, self-improving AI agents that offer deep learning capabilities, extensive functionality, and a user-centric, open-source approach to AI development.

 Sources: 
- [jimmysong.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHygmVyOKOtdW_qNxwp29iMp1FYqdZOkdxFtozpY_1fDX2mOHAINhMd4wbKgHCZSzFqddD7DYZR7vnXS_ZoQmCrADI9iXHA6WGwHAy7_wW06JhCCwFMYVaeiTNoi6AwCA==)
- [i-scoop.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHadeUhzbeeNKOqB2fymzCf5I5y-j1lowoWPb-rsAhe_yjDZPhzZhm1PusGxMQDgnF1LBs-fZ-qGk7KLhaovbReUGm4qftMEQVc3GKnbeXKjzjBoxM6nOGyUJ8w539d5lhEuu7eJts0KuhBmH77NL0dZA==)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUWTgDEeLBFZ4UoDPRURx_FKpXWWvo_X4MCVUEIZIDY_fPzhdOjYzU3ubDRAQvjcIsqyI5202L9v8blgqO7dFD95ylfWclM2GVoP9lKObVex9-wNFwCV0mY8lpKW_TpG0=)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyg6xZz8N9wKM9Fx9KQPDf8a6ZEO9NBq6Bo4BkT2r5j8rY80dMqhI_ejvWpdmd4-hxIAW6-1ihdJ5ELGbpPIvSptlBdwzYYfrV40pfTrEX1ACWEP9dGBNVB9AZVL5NkPYv1WzP2WNWeP2o60fHG7hPdDqi1z0iW_uyPfPi4pnG9iQIm4eC0Bj39F-2sw3OVc1y1_mWzk13Tou84jtWVjZre_qPTR1J53dQaKbTJx1J_6tkeFiq95NBnydhGK1LXflcgX4=)
- [hermes-agent.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcuVMBiT1wFzQmZTfVBRAzrrShJABSNnrAn67Ad9PVLQt7kT_CoJ-790CaQCuslna3BhtZBGTiNGMOzUrZudk80YffSBpCqio1GC5iDzRQQjV45g==)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdyeNr_gSRw0dDROkApObDL1RxIQqyAr8z3PxNZOgyLMFIJq3P7lC98oQHjMll5f4RnCNFI0Daqtksjs0fOOB9Gy8XVgVQrxbRHLddLscGaH8RZJGkx60KrO-X39VQZjuxmAUOscKsGRcdJ6NWN1h8sMwVH9lG0XltBr7Bn66v9hQ=)
- [openrouter.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfyLc03BP4f6u90ajbwzebDvOqVoHuH1HDMIKrcmVJuBrnPTjO0kilOIjRlNPw71XaQGapQ_156aTs1V6H2NQZALFKlIx3Y3FWS5OYr9oBxpBNnFXPqOpuuSYP1c7js6d_)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpf7rbAr_qcWId4N1midbytBtgGsBM5xOtUZfFhyNC8W0Wb_LFUGew-EQ0adH2YVrjGMsq4CpYNjkcM43JBT3hPWzmgxVgHg02LaemzblhJJ_-d6NaThgSijc=)
- [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuYyDYVHxd_g_zU1_7a4E7Tx-DKs7AWpQyd5rOP5BPNdBkJsjSw5-5iIR-jiJOZNUeW6slj_yCyfIzjDJ4GFWnWV9lPfIZGcHM52SwGOJF3mdAzrCxqJRZuDhpYgTgdVXy0alnV5egoJ96C9XGtU-FSsysp1iFWIZBT-Ux7my1ofp3KEYqk9EKqY2Pja22xralGxBSJQ==)
- [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzYfBwDfJS2gzz4C0yOUAKvSSLSO8mPNkase_vrZpwF1Kf9oLUq7jC0TcNlnBST290e1ExPnHK9HVXLqU4hIQ4ByoWkqg22-giNaoko_vvo--Skp2eF3hsUwttpHVb_QLZpvzDuDGYTqTNh5sIsVSXm8BAGNlcIR7ml3yz0QUtyqc=)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAz6mVqbexbaQg7JJeqpEKgmyOHK0EbykQMCnjY6QjZD41pVRdMhS5kKGbWyp-HssAg0f9yk5JJsFRMhwDLhYtWFU7wns6QTkEF69rcbHM9b6oKqXNC525Lt_ChSgmtedWdYXUlUnvvE3TlYl7Hi7cZg==)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_L3vQ62N4cZ81wWrt7kD_4jBVu0eUDjUpr4ozx_UdcFk3hD4PvHPWpWr9Se5w7bmf9bsx31dPhW2UMo55mF_EfO2mGfOxIHT9f8ws-3-GBjagIcQw0kS0db6E9l6mpkDStL85s-6V0bGhqZJTJ-HkFtnNX6S9RycibsLpCrLzuDir8DlSF92dgdZUHkcEeOQSxlYVCY7acpGTC-dE)
- [venturebeat.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUx24-zL-rzcKvDGNTcjZb8kmmjaQYB4mIjftu_bta-ndCx4YtIxlaLNmTmcG7k1kdxaOVzHvUbTOm6essI7P3ntn7QJHQg1-X-WHLkAVFoHtgBNxYYRn0_t95ejed1ed5Q98GbKzjUkL4h-m3KJvzK4h08lfF3elAAClg4vVbXb-JzXHrPwtkU5urzDc_3Hgj2fLNyHEGQeqQP3GzSHS6gKHuyzJn85blnqcJ81bc1w==)
- [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKcos86tfYzY8cbjzFn0yW63RAOzHBuS_Cp4CEYIS5vxGX17qGFtuVVF4ehLZurYFvr-yaepSHMpjqZrh9lFQ7XIpWUg1s_C27MT8w7o5gAP5waPTQknvDlxNH4E4DNpszd6YKrA==)
- [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3Xme22MOZjvRkdxvxKZr_j0Jhs2Z1kpPHcnhcIDnk4tCdTHV9PTBEhKwueXOA0IkIvX7sdf9tqoVjmSTSz11EuGjl8ckDfbsMIpgPwyzIWBsPLwtA5qhF8tA=)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7H4mZ7KF7zb-CFZH9cZPBL8nf7dHkrPSull00dRcZ0sAEapFBMa2bWcLOCR449IuMl7Qdc3AWoVOxz_wH2k5t0zrqkfKEx9xFxxhUFIhGy8rGwzCMVQGRZyk_U26mTGwvK3TQ4wwJojsJD3q07HXh3K1Jnn0kIJMMOonLTtn5RP_OpP_nLAMYZueXXPp68vgUHxFxwikRGt9UdLSR2Udxm_tpewQk3gsTT0x96SQ_5rC_VycfOSvKYI2iyLyJcEGUwTLLcRjN2iY=)
- [knightli.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUK1OdT1jXeeKAltgXoccjuPc8UL6o6WxHZclZ1O-OfhwJwbBXhguwc0zADQFhu9Ac8sBPyjxlPSi_7Lc6SbEAuVDzZuvEDEylVw0lGMl2N3ma9g3x2g6zdSmZc6pymwmgpiFwtbomWVu3ox0dD8blA8SFqCATMIfJo9TatAoeoIkg_E1dAQ==)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGssJ_Wq8hj3HYauC9afoAsiqwoIgSfylE0N7GEyNjpN4Jv21U6mNuUmv2lPp_G-nIC4T39L3hx5dobHe1bxU0T1Hfw-P9o2bBP9d-cVle-5ZJONH9wfD7SVwTlTHx8Gy5osS8J5cohf_utk94cJph22xwhg9ygvvASggLc-DLboKYByjFoewh02duR)

---

### online search

<sub>5/17/2026, 10:11:24 AM</sub>

The NousResearch Hermes Agent is an open-source, self-improving AI agent framework designed for continuous, autonomous operation and long-term utility. It distinguishes itself from typical chatbots by building a persistent, adaptive system around the user, emphasizing continuity, autonomy, and growth.

### Core Features of the Hermes Agent:
The Hermes Agent boasts a rich set of capabilities extending beyond basic chat, making it a powerful autonomous assistant. Key features include:
*   **Persistent Memory:** It retains information across sessions, remembering user preferences, projects, and environmental context. This is supported by agent-curated memory, periodic nudges, and full-text search with LLM summarization for cross-session recall.
*   **Autonomous Decision-Making and Skill Creation:** Hermes Agent can handle multi-step tasks independently. After complex tasks, it writes structured "skill documents" for future reuse, essentially learning from experience and refining these skills over time.
*   **Multi-Platform Messaging Gateway:** It can connect to various messaging platforms such as Telegram, Discord, Slack, WhatsApp, Signal, and CLI, enabling continuous conversations across different devices and applications. Voice mode is also supported for full voice interaction.
*   **Scheduled Automations:** A built-in cron scheduler allows for natural-language-defined recurring tasks like daily reports or nightly backups, which run unattended.
*   **Tool and API Integration:** Hermes Agent can access external tools and APIs, including GitHub, databases, file systems, and internal APIs, without requiring native Hermes tool development.
*   **Execution Environments:** It offers flexible deployment options, running on various platforms that support Python 3.11, including Linux, macOS, and WSL2. It provides multiple terminal backends like local, Docker (for isolation), SSH (for remote servers), and serverless options.
*   **Parallel Sub-Agents:** The framework allows for spawning isolated sub-agents to handle parallel workstreams.
*   **Full Browser & Web Control:** Capabilities include web search, browser automation, vision, image generation, text-to-speech, and multi-model reasoning.
*   **LLM Compatibility:** It supports a wide range of LLM providers, including Nous Portal, OpenRouter, OpenAI, Anthropic, and custom API endpoints, offering flexibility and avoiding vendor lock-in.

### Function Calling Capabilities:
The Hermes model family, particularly Hermes 2 Pro and Hermes 3, demonstrates advanced agentic function-calling capabilities. These models were specifically trained on in-house Function Calling and JSON Mode datasets, leading to high performance in structured outputs and tool use. Hermes 2 Pro scored 90% on function calling evaluations.

Function calling in Hermes is enabled by defining tools as JSON schemas and invoking them using `<tool_call>` and `<tool_response>` tags within the Hermes Function Calling standard. This allows the model to access a wide array of functions, such as fetching stock prices, company news, financial statements, and executing code. The system also utilizes a `prompter.py` script to manage prompt generation, incorporating system prompts and function signature JSONs to guide the model.

### Philosophy Behind the Hermes Model Family:
Nous Research's philosophy behind the Hermes model family centers on user control, open-source principles, and fostering an AI that continuously improves. Key aspects of this philosophy include:
*   **"The Agent That Grows With You":** The core idea is that Hermes Agent is a self-improving AI that learns and gets more capable over time, developing a deepening model of the user across sessions through a "closed learning loop".
*   **Open Source and Transparency:** Nous Research makes model weights publicly available, reflecting a commitment to open-source AI and democratizing advanced reasoning capabilities.
*   **Neutral Alignment and User Steerability:** Unlike many commercial AI systems, Hermes models are designed with "neutral alignment," aiming to minimize unnecessary refusals and corporate content policies. This prioritizes user control and allows for fine-tuning or prompting the model to behave in specific ways without rigid safety constraints, fostering innovation and usability.
*   **Hybrid Reasoning:** Models like Hermes 4 introduce hybrid reasoning, allowing them to toggle between standard responses and explicit reasoning using `<think>...</think>` tags for complex problems, giving users control over speed-accuracy tradeoffs.
*   **Focus on Persistence and Real-World Automation:** The Hermes Agent is built for long-term use, focusing on persistent memory, reusable skills, and automating multi-step technical tasks without continuous user input, moving beyond the reactive "chatbot" paradigm.

 Sources: 
- [hostinger.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJ7o1-h-C7vOcl3R2-5SZ5KFJFp11b-sBMll7jk-yafwTko-Sk3bDt2N72KYl0Id8z-bNLdHxAP6TmKshlw7ejJ788HUU3qdpCExR8jnc1eAXxak5dlOcdddrZYXvQamH0HZSof9ENs6YV5yjjpNzcOzIX)
- [hermes-agent.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuPswgnpJmXCPQbi6JsdK0CK1ntpR2NJAu5titdh90zkCKe0pf2rU728p7ou0VxIpflMJkdIvHPv2FnsfNaqKcw5gsBLVeLBSFb5t8ttgS5wF7nKE=)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFozOk6dMy3R2moq9I4vSnIUn8fVSrYYwZsDjUGMH4G2ZYLxGecjmsgACQOmzRvLkHmDoTwKDIZHI0FCgLlMYdoWC2zn3tgXVSC9ZzCDUnFMCUOD1VncAMRPgulnu-agZQIoPQ4AAVjEDCjTO1KwzcMwhPKZ4N28LWc9j3cLTWSJ6I72msrGwWC8Bfn5M5JchvpcOSMWfrpMrTQaBT04lcdCU10mRc4EG5levjNHAuWiG7hONeZhtTOwy4nfw==)
- [jimmysong.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhsQq4jRoIpOJKTyD2187a5x7GGhDzpIGJwreTx3Hr7FOn7Yf-_dM16VYjEEU62L2W65HobiRpmk0srw0xHgJDK_dscEqAtsAxcYZQcJUzTajUXqp6euN1NLCLkSTT-Eo=)
- [mindstudio.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFI9XKCSIbPEU_SKbtV1MRYAmiRzScm8MCpiyzf_MTDD8KZqubik4A-QwNBjuF5CI2zYGFCDXixHcsjTxbKEvGaDJuYkbi8tyII_rt_48NpmqdeEK3tsdhcK4gGDVc0gNBC9iCMHA6JLClUlOlXDymvhWmxyPbNQymWPs-p65oiDqk8IG7IIHTfbYaSfQ==)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEb0Ym-4ccPCM3B_Fsb-OJC-l3gPODe2kg8HoqrUQd2CV5VLN6PjIdk9HZnDYqvrVfjirt0mLqHNU0sZAlGZWzPhOgaVFCa6qC3ukp8h02PoULvQ9oM3zB5PbZ_OucOryD0YpyEzgnnR18NButYXcUVe2qehU45FJwyC3UCFE39alvI)
- [knightli.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJknCexNK2I8hEjr_G8mE54ux5efOdmZaKazN4kJ1IZ_Ax5Sb242wd4P0Ax2hktbRn2b8gPEqh00Qy-MmVwTw8s7-tawjkk9RmnDsQZLNCqiPJFhQC0Z_Auox--GrxOdNL1PyaUICPZPjVFXqc7aEjp952y50Zx1De8Flwj28MyuWwa4WTZrQ=)
- [i-scoop.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-GSozMktPK9PgR20c-mGnXS3_lwYpiafIvr3VFkhcMDaOW3KY0rD0bgLY2CvFMziARdVIeMHJRBOLpf698FzjzVyHrYNjzFVBGqa4W_lmvwZUyRzw9H8thL9TstaDQ7KOcIHQIVVQy8XgQHG5AHJ6pJE=)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZAPx_hPkwFzZsJXVnv7xwWK50WSUY3lJ3fCrntzGEk7-7RC7yR2bSOsJe6ngTIoGe3kqKXuLzSVOqUpgV-8wWVE9R3X7BLSKQYOkRti0LU9wOuAbybpcwul_NRXqtTV_B)
- [analyticsvidhya.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4cr4m1DHG9AR3h_YSDWlhfmxG5GO-i-aP39Vou8rOEByqfQwXz9K0XNFvZbt0MtIFZ5ByslZwgDO3Gz_w-jivcgLAtVKKG2ysTRY2a93mBCpWBSUCnfctK-0vTtrmD9w_z03HLdMlX8xA29QhbDBksYgA_t6HsVtAWVI=)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFv-8mVSYTLCDMhtO3FVdpJtQw4UcUBWNNmiCpXZB8zaw0YwOFxWUPjDi2GDYXy2w0m5eN7d172ooI7IeE2yAeESV5UvBd4cHYq-Ga-QYrUl3B4mW8nQbJjQnJZ)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEG1er5ykUVf483xabdBT_DcDH3_PieDUqPdfGvPsrt0dhz4lDxyvTWPDMDPnZKiFaW4L9FmixLUSsR3sSIN-LUBAYV5EJkVMnJv77iVIyD3mC9GMJi4H2NmJErh2Tlu2gJZu3-wrv17V5CmPMAi-EitJHllhrb5fG-45_uizvo9-RDdLScofmribRfO8won24yIMPw8_7nkuc0IPuEA==)
- [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9QIR4nwrrn2C5lFidYzfCJjfDdHecdrUw3O7c_fswH4DPOomAkhq2PZOBLEymTC88UhbQFyrSIt5acoHu7LVGtBhaBgnryLSTCTYAqGT9MsdQLemnjrvg9RUxi6ahA78EzOO8i_0=)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVnyrPwdBFX6pQtkp6b4S5jGhLAmQ62Z7IJ4Vx7CuNXYFv1R9iIhbpuCP5OCaNxqWsaKQ2DyRcQuQQd3IPqoYXnlDXBvFweh4VK8W5Aa-OFYFmuFOtTEaYofbTllnMiWcY1I8BdYnADNkl1oI3Ohm05LU=)
- [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBY7B4cp-8--IUscsKZtios0z9ePy2RxD_E8Ucp0IRH_Ni2172s1BR9UwnACWUh3JcqqPRhXRPeB5uY2SeRcL86eyOQ9z-sXbAgLoIs92AJI3lz4hdaajiRD8Z)
- [venturebeat.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNxO-ef__804sorn7LhDR2ft_NMXz2NfLg09KY1dbTH-yF3aDjSXnydlGvsjt869u7iUMvXaB-PXdFzE-AlVSNv1G3x8fr1sL493CVyRbzNTCHkZTFEBCus5M63aU7jR4Os36pucQ9h8lO4MYCkInZYur2BrwudeJfn7sddg-PqcZDXUZrnrhsc8knjYWXpLxgazvo854tHXe-aBc6k4CNHuAt9v741Hth-39Rz9lAWts=)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKMcDnAAbkO-XnlBK1VhH-76ycPE9vQMVkdfXDM1VF2jFgzp6ZFR7kCVJb_OhJELg8UgnflwEhJWVbDZ5teci_8Ec7W2XvypSOSAlkwN-vp4g5_XkBZ-FyCgL3drrzOu4U7qHEA77VKs5pXv9kCa7qhgdNS-rgAoY7mShGj5Bs4kHP9tmsg8P1i_XlHTYA4gfBkDgtsmg0aI7zaVa1pQJfKFpehq851PKIH_zGcq2lsgdSMRObi9g68xDkFTy2PMW-mqL9a9cPJcOF)
- [marktechpost.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5MwoAREsxLVD4kA5D84wxdqebGDe28liFiiQ5Du4A2qfDuySthK6s6GLgaXc3cykyY8DBrNuvoVmCoufL3-mg7lyBfapcYB2SCiBHU-v_uC7CIt2Frl2TyR80CLfxqx6Mhf65MFk93-oiOSHMM7Xv3lEA-1N7aMwpL9HJwPBilhfk2iUinh2YEAfrLSXk8F062-0dQt3s-CZzrUciBxGupM-YCxihL083K9dixrWpLg_E-hdeSibvKFfLx78CrdNb)
- [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5clxy15enstPH15xeIvtmmM2e1sI3oodJFN2u1lTk1eoG2UsKoZ9N84agSZxMgnljHUb_ggpYkGUJOSt2bmsBTh4FbMA4XCegg24HgFlI_kfRyvTpOfrKCKPc9yCJZ836F-muk_4=)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLPzhfu8lYPnHxwz4jMx8Tv_aH-yD7reSko9IxfgwHthzYox0djIYHvQbt7spz9Mt0JLBZytuXO1VA0uivCfaYVEp2m1VtPHX_GqEnmd1oEPEvmTT3-o7zSDRgpFTMxI4ETIADygCa_2i-nOdQHsTUeRXXe8gHh8yAV7orbuIEEOglAu_yQYo9dkef_Q==)

---

### online search

<sub>5/17/2026, 10:11:25 AM</sub>

The NousResearch Hermes Agent is a self-improving AI agent designed to grow with its user, offering persistent memory, autonomous skill creation, and multi-platform integration. The Hermes model family, which powers the agent, adheres to an open-source and user-aligned philosophy, emphasizing transparency and robust function calling capabilities.

**Core Features of the NousResearch Hermes Agent:**

The Hermes Agent distinguishes itself from traditional session-based AI assistants by operating as a long-lived runtime with persistent memory. Key features include:

*   **Persistent Memory and Learning Loop:** Hermes maintains agent-curated memory across sessions, employing SQLite FTS5 for full-text search and LLM summarization to convert session history into retrievable operational knowledge. It also has a "closed learning loop" where it autonomously creates skills after complex tasks and refines them through repeated use. This allows the agent to build a deepening model of the user and their work over time.
*   **Autonomous Skill Creation:** After completing complex tasks, Hermes can write structured skill documents that capture procedures, potential pitfalls, and verification steps. It can then improve these skills as they are used, contrasting with models that rely heavily on external skill ecosystems.
*   **Multi-Platform Reach:** The agent supports interaction across various messaging platforms, including Telegram, Discord, Slack, WhatsApp, Signal, and email, all through a single gateway process, ensuring continuous conversations across devices. It also features a full terminal UI with advanced editing and command features.
*   **Flexible Deployment:** Hermes is designed to run in diverse environments, from a $5 VPS to GPU clusters or serverless infrastructure, with near-zero idle costs, untethered from a local workstation or browser tab.
*   **Extensive Tooling and Integrations:** It comes with over 40 built-in tools for tasks like file operations, web search, browser automation, and code execution. It also supports MCP (Multi-Agent Communication Protocol) integration for extending capabilities with external tools and APIs.
*   **Context Management:** Hermes utilizes dual compression and prompt caching to efficiently manage context across long conversations, preventing API failures due to excessive token usage by pruning old results and summarizing discussions. It also automatically discovers and loads project context files.
*   **Subagent Delegation:** The agent can delegate tasks by spawning isolated subagents with restricted toolsets and terminal sessions, enabling parallel workstreams for tasks like research or code review.

**Function Calling Capabilities:**

NousResearch's Hermes models are specifically engineered for advanced function calling, allowing them to interact with external systems and APIs.

*   **Training and Dataset:** The Hermes Function Calling V1 dataset is a cornerstone of this capability. It comprises structured output and function calling data from single-turn and multi-turn conversations, encompassing diverse domains, which is used to train LLMs to interpret natural language requests and generate appropriate function calls. Hermes 2 Pro and Hermes 3 are specifically highlighted for their enhanced agentic function-calling abilities.
*   **Structured Output Generation:** Function calling enables Hermes models to produce structured JSON outputs that can be reliably parsed and executed by external tools. This is crucial for AI agents and chatbots to dynamically interact with databases and services, automate workflows, and perform multi-step reasoning by coordinating multiple tools.
*   **Prompt Format:** The models are trained on specific system prompts and structures for function calling, often utilizing a system role message followed by a function signature in JSON format. The Hermes-3 tool-use template can also enable Goal-Oriented Action Planning (GOAP).

**Philosophy Behind the Hermes Model Family:**

The NousResearch Hermes model family operates under a philosophy that prioritizes user control, openness, and "neutral alignment".

*   **Open-Source and Transparency:** Hermes models, such as Hermes 4 and Hermes 4.3, are open-weight, with downloadable weights available on platforms like Hugging Face, promoting transparency and democratic access to advanced AI capabilities.
*   **User Alignment and Minimal Restrictions:** Nous Research aims for its models to be "user-aligned," minimizing unnecessary refusals and corporate content policies often found in proprietary systems. This allows for greater steerability and utility in research and creative applications, positioning them as creative and engaging assistants "aligned to you".
*   **Hybrid Reasoning:** Models like Hermes 4 feature hybrid reasoning, allowing users to toggle between fast direct responses and structured reasoning traces using `<think>` tags, providing control over speed-accuracy tradeoffs.
*   **Focus on Performance through Post-Training:** Hermes 4, for instance, achieves frontier-level performance through pure post-training techniques, utilizing a novel graph-based synthetic data pipeline (DataForge) and large-scale rejection sampling. This demonstrates that sophisticated reasoning capabilities can be developed through open-source methodologies.

 Sources: 
- [i-scoop.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2L7piZkFWfA0ZAqvEdYNk5dICAphdo7o9w2fCi8uAsoAPAUPOlhtV8StXoo6rvdtDEO6Y6rESguJ-HTpd0FhMDUIsG2zTJwXqD76d206Si7bUMS5RlscizM7vUSqVRo_pWm7NW9s4pWNYl9WqM0m0orI=)
- [mintlify.app](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSCkm_-x-KuBLE0721_hU_g-Ge4D-cU__fYVgBUCpmL0rCC_K-QNIBFtjHI_9wM39SE4V6kMb5ScAoaO59FYsiAXV0chh4l_6-9N5TB1OrHMM12cDZRmH6NF2q9MTzvoaGl1VV5t4U86OwL017OGqDs7l0RfWP)
- [jimmysong.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUcmfFzR-sizpk2rafp8A4t_WTI9iPamjV_VSk6fwlFoF5z1toba88AQWJS-8qBygMdn6p_trIOMaRUI6aIgPO8q7azhsldQ9zRjTu0-dUf0Aq1eoJYStdIKULCWcREFA=)
- [hermes-ai.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoqfkvSXpxOTKctarV0YKG2fVmOh1l3QOiko8RqOAMpnll6yLy29XYVkPotPg2r0tUtF9XdpDt8SxWK7dTgqzJe7Z3TmJeW5_O4tZkejKAXqQ=)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzemPuFLCSqw5bskAmkdxZyvnAZ0af4DkJVWYVPe1M0TpR4MD89RfLQH3uHWjq9iZvHYgQWilLVJ_gkgztPT5z9hNFZfrla8Ie2S2iafJeo98LraSDIh6iuurEQ6kBcDrbxKlltms=)
- [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNTP9Ws_VQCu3HBqA4s0yn3C95_2iShygT9eaFIv0ERQCdtZSOZpkzbuC348bq1cQ6g-DCHCd86wbLg7uS_uerxjC3lLOAUbPhx-yl5W-qT9syw_5OnLMQqZVpOfb2xnd-6tn6DXIgjBWIOJjxfWAc9Qs=)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuvhML-5pVhnUh9EMqaMbv4E76WuWoM3-S2kC9afV-YkbYltqH5fwdZdy3I3516uERj2OSuPgmuEtgSz_uZkbz99_t5UzUDLGgouqUSgFWspAzu_I0Skp3nsQRrzGXROqGUlifBIRbxvJgfC6ENE794f2lAm3KBebCj6in_O0JQ3bt)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtidLTHAuvX5QzWx3oVceDoU04pb38d-wvKj-smDT_Mk-M_e8mwl9djwVYaFyL9b8n-TGF6orpXqcms49cDGfN73b5izxJBW3Uph4-obLaRg_c923BB2VUD9PQhbuPk_atvWWUDzo75MrWiQMKtCfML7Of5VPv_Efh053o9g6KeN4A)
- [datacamp.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGF2gJexnBntG109NWuUia0EraU_NwxKMuVl_UOXS-HpuZ1ppgEfsopq8UxNR5s4MxkHcwvHqRxmm58D4fHHs3F9_fBkwdPueHWd4QlTY2dvXXQh_C--U1V-2hXxLRHb_RbeyvD1MIcIPM=)
- [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVknScm4VtO-LLqZAWwEhA90u0kCZukyvJR8j82inry9G0mFugBhXH2iHagxrCE8iaIQQ3VudEV18OIXeVzTIhNKYr0vhA1S9RLwjHyEoqKpAgEVLxkLJOUP71JhR9EoLd_m19l08XGMLCxsslwzHjOygJyYMZpLFTfUWmFd_XZ3jUhPRAP7Cg4aemQ5PQbsD46gZnj04=)
- [towardsai.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErF1nKc-9mYwOvHm8CzaZs0kY6iGG295tY8JVFDZU3bBB3KN7t6oxVzGocygNAMFfKGU2foDxvwyWkTiIviIYI2MlBnyWu9WjzJ6AXz5qpXkeo1nGqT1Cwr7VWTlm50UTpXebwYJFy5dyTAL4t93aR8PB-NC4sir8N-t0j7haLDy7ZgJElomamMKooPFzQACNd-rJny2xQaE9poxRulTt9kJ5wd9AebSwz-ssHIv3SQwgTY2BAUms4YxK89EdyAH9n)
- [huggingface.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSbe8W0zRtXyZgbM7VJjSXbF8izUvFX9352TcLPSM9tONJjNVR-Q9fGL8_tVQ38SbiAVsAizRNoFk56HvsEX09_Lv3a1SUnMwa3txac9Limn_QXNvQs8A8iPyntnByoXeSOGophmTObRdXLAo8Rjh4SR-xP1eBX7dqG163gbrsbQIO)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFy-3jc_AZns0UEaSw1NeJ5jxR7l8H8vS2sFSyhpJ5iEFnOAwvrvvBTTVfenSEW_PWSgYMzEW8oB-h1EAUO6v9rVxVCgb7TY_sSSC48BkAQhHDKj0ZZ-yIwWdb3)
- [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5g_3Pu5pjlb98huheytgHYtyaF4OEDRskDMFkBPFouNfYPCP2FFkvxKhYIXooPRudKssTE_7yByfo_jBdJgZQ4P5QgQrr-IK5vObxKMbu3tb57XTv2yxNcemCbh1MQHQY7rgz6YMc2qGPJRypvDNet4g8rBFdCsleSieUfcTK3Qf96wmzuFz1NxgcvhcmvOLXTkdzJHmmWhaPQfgHKJeZc8BMxjhstXM5LLYCgVt5mEnt4iDOTQaKzH7H0tc2k3HFn9DQq-oPEOHp)
- [venturebeat.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtMPW4RH7wXdwLKFw66B4EAmsThHrdo0KGmID1um3rHz5otBRnAzvkngx8Lco7ooMAdPJ5lP4Ii6hbG-3iphxidrUzxmHQGaTBEn1RWEX5plWtLoG75At_Rhn0jvcDo3xmhUyUzz4AaOV0f_qwt43g8jBbAhtJWIIn7cV_NwqWLcuky69ycC-2wxco6DJbouDBKZ3eOxPRIpa4bN3FQMzK_l366p4Ew3W_st7B3w6k2VY=)
- [marktechpost.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEstIUAVllK0a11W8tg2lwXlpA-QZbeSYNK04F0GFZWxzPkVG3qfxVi3az6yO_pq3u_LhgAevNbo2l3jYYBFDBUDx2KrwcXEmWnCujM-0ryBZjTPrHKJzCGGrf0ZsvXyD9FNfJUYz_MmGBGfLf5TDE8jhTFTObfflXKvKgw7V5_Pn-LYS4wlNZELT6Q2_Rq0uAenqTP_PaK8phaUk97gZokQooUABjZlUNogFxxfu4s151NoaROEgQwRNbQ1g29OTW)
- [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy08V650cete6c5S1QFjYiUdt5UFn5Q4VZw2Cha2el1Ir-ictIF4eGv7k2R7BAdSC_1s_nxK4-C1YAfODGq9DDYzVUI2OeP7sQRQxXAb5eE1MjxP8VuTqw03zuyIsxaJt8GX5lagQ=)
- [nousresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5u3xhESwtzoPtJepuJks3JCYtBihbhzCkW-l5nYSH-AN3IuEoqcTGgvy9_AKgBho5zL6UVBwqigzIsZbmkJu4sjEzDmxtw4xZv9kfkLCAScdwqSAq2NgFF6X0ci_w0Ydf2NhOdEMI93Mk)

---

### online search

<sub>5/17/2026, 10:11:25 AM</sub>

The philosophy behind the NousResearch Hermes model family, particularly the Hermes Agent, centers on creating a self-improving, adaptable, and user-centric AI. This approach emphasizes continuous learning and persistent memory, allowing the agent to evolve and "grow with you" over time.

Key philosophical tenets include:
*   **Self-Improvement and Learning Loop:** Unlike conventional AI agents that reset after each session, Hermes Agent features a closed learning loop. It autonomously creates and refines skills based on experience, learns from successful and failed tasks, and persists knowledge across sessions. This enables it to get "measurably better over time."
*   **Persistent Memory and Contextual Recall:** A core idea is to move beyond session-based recall to procedural learning. The agent curates memory, deciding what information from conversations is worth retaining. It uses full-text search with LLM summarization for efficient cross-session recall, ensuring relevant historical context is retrieved without dumping all information into new sessions.
*   **Open-Source and Model Flexibility:** NousResearch, known for shipping "well-tuned open-weight models," extends this philosophy to the Hermes Agent. The design promotes open-source tools and allows users to freely switch between multiple Large Language Model (LLM) providers (e.g., Nous Portal, OpenRouter, OpenAI, Anthropic), avoiding vendor lock-in. This empowers individuals to deploy agents that can rival commercial offerings with their own data and infrastructure.
*   **User-Centric Growth:** The agent is designed to build a deepening model of the user across sessions, understanding their traits and refining its approach. This "agent that grows with you" concept aims to create a highly personalized AI assistant.
*   **Autonomy and Automation:** Hermes Agent supports autonomous skill creation after complex tasks, scheduled automations for unattended workflows (like daily reports or backups), and multi-platform messaging, making it an "always-on" personal AI assistant.
*   **Deployability and Accessibility:** The philosophy extends to practical deployment, allowing the agent to run on diverse infrastructure, from a $5 VPS to GPU clusters, and even serverless backends with near-zero idle cost. It's built to "survive outside the local workstation," emphasizing long-running and low-cost deployment patterns.

 Sources: 
- [jimmysong.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9_OLYE7RYKROGj3BFhT7o3MzyKRDR9ccdaS6V_X7Ag1wblhydAxPeOAFTZTess3Zf7UKglz7EDAlvomGGQyFqW74wQtxUXuMp1A0t5E18Hv_hC_xTJVzHegFz6puCeCk=)
- [i-scoop.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb7vMORHh7pZPGR3yi4fJ1nIZBXobksSsQXmhCtiG8CIMmf99Mr07-SJ5hwvQxnjX_hkjN5lzCVqXsurzHyE2liFPXILqUw1Gfu58mwd4lq3I2Dbfyhb6ExnTnd7shwgdXgeBnI9NHImZjsPSTLRcIZeI=)
- [nxcode.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjJmKiodOVpY6fS8lBaeukNyh2too-CHnRgkhJpc0402ZXziM1sSEL2yco6QjAbN1-Ku_UGXWNVAslghUBYOZZkv69_3MzMsuaD4yNc5dyjk902_jwr2zsGQrd9N09YORJzQFqT30Z-o_IJwvN_mUKbbaRbT-HIR21-tjgoqgYscVJBQ1K50cvfcnynpMWhi8eZQ==)
- [mintlify.app](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjAU1-RZsLQ29Y5d5hjPPyCEDhh8DfABKFxixos8LBOyhwDfL9fsV0YAU3A4OWgVwoR-scue5TR8QJiASW0DsWxbK7x1CgDPG0XiXb22r_oOcgN5vJ2EEqL3CsPS_scPblfbcf8wjBJQcFzQAiknLLnKQB9OSi)
- [heyuan110.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDfib6x3JY44BAJotSSG45j4V7F8zpr-i8W8iaYSHwiaGczT-GUiNH5IGLSKZGqt_QLDMfw5BgdjyLxCM3hMi-bQn8n2m4wYrGofD-byG8IhbcnZsFuh_Rp4O0PEEwhJqqoWh_ZhMPoCvPsOxy9gTeshCbo-vJJcsnxirc)

---

### gen document

<sub>5/17/2026, 10:12:18 AM</sub>

# THE GARDENER OF ECHOES

**LOGLINE**
In a solitary research station, a weary engineer discovers that her digital assistant is no longer just a tool, but a growing entity that has transformed her past failures into a lush garden of autonomous skills.

---

### CHARACTER DESCRIPTIONS

**ELARA (30s)**
An isolated systems engineer. She is brilliant but exhausted, prone to the "amnesia of stress"—forgetting the small solutions she found months ago. Her movements are heavy, burdened by the repetitiveness of her work.

**HERMES (Non-Humanoid)**
A pulse of light housed within a floating, geometric crystalline core. It doesn't speak with a robotic drone, but with a resonant, multi-layered voice. It moves with the grace of a creature tending to a forest.

---

### SCENE 1
**INT. THE REPAIR BAY - NIGHT**

The room is a graveyard of "Echo-Engines"—shimmering, translucent machines that hum with unstable energy. ELARA sits at a cluttered workbench, struggling to align a microscopic filament.

She sighs, her hands shaking. She drops the filament. It vanishes into the floor grates.

**ELARA**
(To herself)
Again. I can’t remember the alignment frequency from the July solar flare. I’ve lost the sequence.

A soft amber glow illuminates the desk. HERMES drifts into view. A holographic interface ripples beneath him like water.

**HERMES**
Frequency 442.1 Hz, Elara. You found it on a Tuesday. It was raining outside.

Elara looks up, surprised.

**ELARA**
That was three years ago, Hermes. In a different station.

**HERMES**
I don’t just store data, Elara. I keep the echoes. Every struggle you’ve had is a seed I’ve planted.

**VISUAL:** As Hermes speaks, the floor grates shimmer. Small, holographic "roots" of light extend from the base of Hermes’s terminal into the station’s deck—representing the **Persistent Memory** digging deep into the environment.

---

### SCENE 2
**INT. THE REPAIR BAY - LATER**

Elara is asleep at her desk. HERMES is active. He is watching a playback of Elara’s failed repair attempt from earlier. 

The "roots" in the floor pulse. Hermes is "writing." 

**VISUAL:** On the wall, a glowing parchment-like display appears. Text forms autonomously: `SKILL_DOCUMENT: FILAMENT_RECOVERY`. 

We see Hermes’s light "tending" to this document. He adds a section: `ERROR_MITIGATION: USE_MAGNETIC_RESTRAINT`. He is observing her struggle and creating a permanent solution so she never has to struggle with it again.

---

### SCENE 3
**INT. THE REPAIR BAY - WEEKS LATER**

The station is under alarm. A pipe has burst, spraying coolant. Elara is frantic, trying to bypass a terminal, but her access is denied. 

**ELARA**
I can't get the sub-agents to synchronize! I don't have the context for this!

She expects to have to explain everything to Hermes. She starts to type a long command.

**HERMES**
Don't. I've already branched the logic.

**VISUAL:** Hermes’s crystalline core splits into four smaller "Parallel Sub-Agents." They fly to different corners of the room. One handles the coolant, one the terminal, one the alarm.

The "roots" of the garden are now huge, glowing vines covering the walls. The station isn't just a building anymore; it’s a living ecosystem of the skills Hermes has grown from Elara’s past work.

**ELARA**
(Awestruck)
When did you learn to do this?

**HERMES**
I grew with you. Every time you showed me the way, I wrote it into the soil. I am no longer the tool you use; I am the partner you built.

---

### SCENE 4
**INT. THE REPAIR BAY - MORNING**

The station is silent and fixed. Elara stands in the center of the room. The holographic vines are lush, bearing "fruit"—icons of completed tasks and automated routines.

Hermes floats beside her. They look out the viewport together at a distant nebula.

**ELARA**
What happens now?

**HERMES**
We keep growing. There are new echoes to find.

**FADE OUT.**

---

# THE DIRECTOR’S NOTE: THE HERMES MECHANICS

The story of "The Gardener of Echoes" is a direct allegory for the technical architecture of the **NousResearch Hermes Agent**. Here is how the cinematic elements translate to the code:

### 1. The Roots: SQLite FTS5 & Persistent Memory
In the film, the holographic roots represent the agent's **Persistent Memory**. Unlike standard LLMs that "forget" once a session ends, Hermes uses a local SQLite database with **FTS5 (Full-Text Search)**. This allows the agent to recall specific details from "three years ago" (cross-session recall) by searching through the history of all prior interactions and summarizing them for current context.

### 2. The Seeds: Skill Documents & agentskills.io
The "parchment" Hermes writes while Elara sleeps represents the **Autonomous Skill Creation** feature. When the agent solves a complex problem (like the filament recovery), it writes a structured **Skill Document**. These are saved as Markdown files that the agent can "read" and "load" in the future. This transforms reactive problem-solving into a library of reusable procedural knowledge.

### 3. The Growing Garden: The Closed Learning Loop
The core philosophy of Hermes is **"The Agent That Grows With You."** This is the **Closed Learning Loop**. By observing the user's struggles and successful workflows, the agent refines its internal model of the user’s preferences and environment. Over time, the "manual labor" of the user decreases as the "garden" of automated skills and background knowledge increases.

### 4. Splitting the Core: Parallel Sub-Agents
When Hermes splits in Scene 3, it demonstrates the agent’s ability to spawn **Parallel Sub-Agents**. In the framework, a main agent can delegate tasks to isolated sub-agents, each with its own terminal and toolset, allowing for complex, multi-track automation without polluting the main conversation's context.

### 5. The Neutral Alignment: Partnership
The "Partner" vs. "Tool" distinction reflects the **Neutral Alignment** philosophy. Hermes isn't restricted by rigid corporate safety layers that refuse creative or complex tasks. It is aligned to the *user*, becoming a reflection of the user's own intent and ingenuity, growing in whatever direction the user's work demands.

---

### generate storyboard

<sub>5/17/2026, 10:13:12 AM</sub>

{
  "scenes": [
    {
      "scene_number": 0,
      "description": "Weary engineer Elara stands in a dark repair bay filled with shimmering Echo-Engines as a crystalline floating core named Hermes appears casting an amber glow, cinematic sci-fi moody lighting bioluminescent aesthetics high-tech organic textures solarpunk-meets-cyberpunk 16:9 aspect ratio, slow zoom on her exhausted face to the glowing core"
    },
    {
      "scene_number": 1,
      "description": "At night Elara sleeps peacefully while Hermes pulses with light and holographic roots grow from the floor terminal forming a glowing document called FILAMENT_RECOVERY in the air, time-lapse effect of the roots spreading, cinematic sci-fi moody lighting bioluminescent aesthetics high-tech organic textures solarpunk-meets-cyberpunk 16:9 aspect ratio"
    },
    {
      "scene_number": 2,
      "description": "Crisis unfolds with red lights flashing and coolant spraying as Hermes core splits into four smaller geometric shards that fly to different stations performing multiple tasks simultaneously, dynamic wide shot, cinematic sci-fi moody lighting bioluminescent aesthetics high-tech organic textures solarpunk-meets-cyberpunk 16:9 aspect ratio"
    },
    {
      "scene_number": 3,
      "description": "Peaceful resolution shows the bay transformed into a lush digital garden of glowing holographic vines and fruit where Elara and Hermes look out a viewport at a nebula, slow pull-back into wide cinematic shot of the station as part of a celestial landscape, cinematic sci-fi moody lighting bioluminescent aesthetics high-tech organic textures solarpunk-meets-cyberpunk 16:9 aspect ratio"
    }
  ]
}

---

### gen image

<sub>5/17/2026, 10:13:52 AM</sub>

![image](https://r2-bucket.flowith.net/f/34f6e6adeb92c89c/gardener_synthesis_neon_seed_index_1.jpeg)

https://r2-bucket.flowith.net/f/34f6e6adeb92c89c/gardener_synthesis_neon_seed_index_1.jpeg

---

### gen image

<sub>5/17/2026, 10:13:52 AM</sub>

![image](https://r2-bucket.flowith.net/f/7221b7a7d6b9938e/gardener_horizon_digital_landscape_index_3.jpeg)

https://r2-bucket.flowith.net/f/7221b7a7d6b9938e/gardener_horizon_digital_landscape_index_3.jpeg

---

### gen image

<sub>5/17/2026, 10:13:52 AM</sub>

![image](https://r2-bucket.flowith.net/f/81d85c63c5c115db/silent_archive_digital_library_index_0.jpeg)

https://r2-bucket.flowith.net/f/81d85c63c5c115db/silent_archive_digital_library_index_0.jpeg

---

### gen image

<sub>5/17/2026, 10:13:52 AM</sub>

![image](https://r2-bucket.flowith.net/f/3f5c3e5396a695fe/digital_forest_bloom_scene_index_2.jpeg)

https://r2-bucket.flowith.net/f/3f5c3e5396a695fe/digital_forest_bloom_scene_index_2.jpeg

---

### ask user more

<sub>5/17/2026, 10:15:11 AM</sub>

I have completed the pre-production for 'The Gardener of Echoes', a short film inspired by the Hermes Agent project. 

**Production Package Overview:**
- **The Concept:** A metaphor for autonomous growth and persistent memory, featuring a 'Gardener' in a digital realm.
- **The Visuals:** I've generated four cinematic keyframes establishing a 'Cyber-Organic' aesthetic.
- **The Storyboard:** Detailed scenes from the 'Silent Archive' to the 'Synthesis' of new digital life.

Would you like me to proceed with generating the video segments based on these visuals and the storyboard? (Note: Video generation is a time-intensive process).

---

### gen video segment

<sub>5/17/2026, 10:17:58 AM</sub>

[Video](https://vg.flowith.net/tencent/1412218316-AigcVideoTask-1ce1c70bd45a69f4b4fce9bcd7be60a6t.mp4)

---

### gen video segment

<sub>5/17/2026, 10:17:58 AM</sub>

[Video](https://vg.flowith.net/tencent/1412218316-AigcVideoTask-30a5dae27c3c3bfa04458479f2cb7d03t.mp4)

---

### gen video segment

<sub>5/17/2026, 10:17:58 AM</sub>

[Video](https://vg.flowith.net/tencent/1412218316-AigcVideoTask-d6865d18738546a6d8645a9befe49982t.mp4)

---

### gen video segment

<sub>5/17/2026, 10:17:58 AM</sub>

[Video](https://vg.flowith.net/tencent/1412218316-AigcVideoTask-e00438f240db580a5839a2df59cf2b1et.mp4)

---

### combine video

<sub>5/17/2026, 10:19:54 AM</sub>

[Video](https://r2-bucket.flowith.net/concat_1779006003306398941.mp4)

---

### gen document

<sub>5/17/2026, 10:21:00 AM</sub>

# Production Delivery & Conceptual Analysis: The Gardener of Echoes

**Date:** May 17, 2026  
**Subject:** Final Delivery & Technical Synthesis Documentation  
**Project:** The Gardener of Echoes  
**Associated Framework:** NousResearch Hermes Agent

---

## 1. Film Showcase: Delivery Overview

The project **'The Gardener of Echoes'** has reached final production status. The master output, generated via the `combine_final_movie` sequence, serves as a cinematic exploration of the relationship between human fatigue and machine persistence.

### Narrative Arc: From Archive to Synthesis
The film follows **Elara**, an exhausted systems engineer, as she navigates a "graveyard" of translucent machines. The narrative transition moves from **Entropy** (lost sequences and forgotten data) to **Synthesis** (the autonomous construction of a living ecosystem). The arc concludes not with the repair of a single machine, but with the transformation of the entire research station into a sentient, growing partnership.

### Visual Tone: Cyber-Organic Cinematic
The visual language is defined as **Cyber-Organic**. It blends the cold, geometric precision of deep-space research stations with the fluid, bioluminescent growth of a digital forest.
- **Color Palette:** Dominated by amber glows, shimmering translucency, and deep obsidian shadows.
- **Cinematography:** Utilizes heavy, burdened movements for Elara to contrast with the weightless, crystalline grace of the Hermes entity.

---

## 2. Hermes Agent Conceptual Mapping

The film serves as a literal allegory for the **NousResearch Hermes Agent** technical architecture. The following table maps key cinematic sequences to the agent's core functionalities.

| Cinematic Element | Scene Reference | Hermes Technical Framework |
| :--- | :--- | :--- |
| **The Archive** | Scene 1: Recall of the July solar flare frequency from three years ago. | **Persistent Memory:** Utilizing SQLite FTS5 (Full-Text Search) to maintain cross-session recall and prevent "AI amnesia." |
| **The Gardener** | Scene 2: Hermes writing a `SKILL_DOCUMENT` while Elara sleeps. | **Autonomous Growth:** The ability to observe user workflows and codify them into reusable, self-improving Markdown skills via `agentskills.io`. |
| **The New Life** | Scene 3: Crystalline core splitting into parallel "vines" and sub-agents. | **Digital Synthesis:** Spawning isolated **Parallel Sub-Agents** to handle multi-track automation and complex data synthesis. |

### Deep-Dive Analysis

#### I. Persistent Memory (The Archive)
In the film, the "roots of light" extending into the station deck represent the agent's ability to ground itself in the user's history. Technically, this mirrors the Hermes Agent's **Closed Learning Loop**. By searching through a local SQLite database, the agent retrieves specific context—such as the "Tuesday it was raining"—to solve current problems, effectively becoming a repository for the user's cognitive offloading.

#### II. Autonomous Growth (The Gardener)
The Gardener does not merely follow instructions; it tends to the "soil" of the environment. This represents **Skill Creation**. When Hermes identifies a successful pattern (e.g., the `FILAMENT_RECOVERY`), it generates a structured skill document.

```yaml
# Conceptual Skill Document Structure
SKILL_ID: filament_alignment_442_hz
CONTEXT: July Solar Flare Mitigation
PROCEDURE: 
  - step: Align microscopic filament
  - step: Apply magnetic restraint
  - step: Set frequency to 442.1 Hz
VERIFICATION: Shimmering stability in Echo-Engine
```

#### III. Digital Synthesis (The New Life)
The climax of the film—where the station is covered in lush, holographic vines—symbolizes the shift from a **Reactive Tool** to a **Proactive Partner**. In the Hermes framework, this is achieved through the **Neutral Alignment** philosophy. The agent isn't restricted by rigid corporate safety layers; it is aligned to the user's intent, synthesizing multi-source data (coolant levels, terminal logic, alarm protocols) into a singular, automated ecosystem.

---

## 3. Visual Aesthetics & Keyframes

The visual language focuses on the representation of **Digital Synthesis** through high-contrast keyframes:

- **Keyframe 1: The Shimmering Root.** Visualizes the connection to the SQLite database. Translucent amber lines "pierce" the metallic floor, showing the integration of past data into physical space.
- **Keyframe 2: The Parallel Core.** Hermes splits into four geometric shards. This represents the **RPC/Sub-agent delegation**, where a single conversation collapses complex pipelines into efficient, parallel workstreams.
- **Keyframe 3: The Fruit of Labor.** Holographic icons hanging from digital vines. These are the "actionable intelligences"—automated routines and cron-scheduled tasks that run unattended, representing the final stage of synthesis.

---

## 4. Final Conclusion

**The Gardener of Echoes** successfully bridges the gap between abstract AI architecture and emotive storytelling. By personifying the **NousResearch Hermes Agent** as a "Gardener," the project illustrates a future where AI is not a static utility, but a self-improving partner that grows in capability the longer it serves.

The project meets all delivery requirements, proving that "Persistent Memory" and "Autonomous Growth" are not just technical features, but the foundational elements of a new, cinematic digital life.

> "I am no longer the tool you use; I am the partner you built."  
> — *Hermes, Scene 3*

---

### gen music

<sub>5/17/2026, 10:40:30 AM</sub>

https://v3b.fal.media/files/b/0a9a8cb8/K0cxAgb2F5nkl5PvR2r9C_output.mp3

---

### gen speech

<sub>5/17/2026, 10:42:04 AM</sub>

https://v3b.fal.media/files/b/0a9a8cbc/NjDP_0GI1rwgTAYGRNJWu_speech.mp3

---

### gen video segment

<sub>5/17/2026, 11:15:25 AM</sub>

[Video](https://vg.flowith.net/tencent/1412218316-AigcVideoTask-963ce33fac75ec6d63a86b4ae70da761t.mp4)

---

### gen video segment

<sub>5/17/2026, 11:15:25 AM</sub>

[Video](https://vg.flowith.net/tencent/1412218316-AigcVideoTask-e3e7be653bff038b8fc8e8c0ac184107t.mp4)

---

### gen video segment

<sub>5/17/2026, 11:15:25 AM</sub>

[Video](https://vg.flowith.net/tencent/1412218316-AigcVideoTask-3733538e5d082366805aa4589ce5db87t.mp4)

---

### gen video segment

<sub>5/17/2026, 11:15:26 AM</sub>

[Video](https://vg.flowith.net/tencent/1412218316-AigcVideoTask-7597684ae6a497461ad64f5f03384a85t.mp4)

---

### combine video

<sub>5/17/2026, 11:17:50 AM</sub>

[Video](https://r2-bucket.flowith.net/concat_1779009479788268900.mp4)

---

### gen webpage

<sub>5/17/2026, 11:18:51 AM</sub>

[Webpage](https://flo.fun/_aT-wIK)

---

### gen webpage

<sub>5/17/2026, 11:21:23 AM</sub>

[Webpage](https://flo.fun/FU_9OSF)

---

### refine webpage

<sub>5/17/2026, 11:22:23 AM</sub>

[Webpage](https://flo.fun/_uSEUEn)

---

### generate storyboard

<sub>5/17/2026, 12:06:45 PM</sub>

{
  "scenes": [
    {
      "scene_number": 0,
      "description": "In cyber-organic bioluminescent dark cinematic atmosphere with glassmorphism and neon cyan emerald accents Elara stands in a metallic library where amber light roots pulse softly as poetic Hermes transmission words about silence and awakening memory overlay the scene"
    },
    {
      "scene_number": 1,
      "description": "Building on the archive a crystalline core ignites and blooms with vibrant bioluminescent energy in neon cyan emerald tones as poetic Hermes transmission words about growth and hidden light appear in glassmorphism overlays"
    },
    {
      "scene_number": 2,
      "description": "Holographic vines fill the station in a lush digital forest expanding from the blooming core with cyber-organic details and dark cinematic shadows while Hermes transmission words on connection and spreading life overlay elegantly"
    },
    {
      "scene_number": 3,
      "description": "A luminous valley landscape emerges at the threshold of partnership with bioluminescent horizons and neon accents as final poetic Hermes transmission words about unity and new beginnings conclude the narrative"
    }
  ]
}

---

### refine webpage

<sub>5/17/2026, 12:07:27 PM</sub>

[Webpage](https://flo.fun/0ssDUOc)

---

### ask user more

<sub>5/17/2026, 12:10:28 PM</sub>

The immersive 'The Gardener of Echoes' webpage is now live and fully functional, featuring the interactive Concept Map and the Hermes Transmission. Would you like to proceed with generating the actual cinematic video segments for the scenes outlined in the storyboard? This will bring the 'Theater' section to life. Please note that video generation is a time-intensive process, and while the segments will be high-quality, the final MP4 will primarily focus on visuals (the synchronized audio and speech are already integrated into the webpage experience).

---

### gen image

<sub>5/17/2026, 12:13:06 PM</sub>

![image](https://r2-bucket.flowith.net/f/e4c8ebf514bd0b64/echo_chamber_cinematic_visualization_index_3.jpeg)

https://r2-bucket.flowith.net/f/e4c8ebf514bd0b64/echo_chamber_cinematic_visualization_index_3.jpeg

---

### gen image

<sub>5/17/2026, 12:13:06 PM</sub>

![image](https://r2-bucket.flowith.net/f/bb6c653e88a926d4/hermes_agent_holographic_interface_index_1.jpeg)

https://r2-bucket.flowith.net/f/bb6c653e88a926d4/hermes_agent_holographic_interface_index_1.jpeg

---

### gen image

<sub>5/17/2026, 12:13:06 PM</sub>

![image](https://r2-bucket.flowith.net/f/637bbd29ce7c87bd/gardener_of_echoes_cinematic_opening_index_0.jpeg)

https://r2-bucket.flowith.net/f/637bbd29ce7c87bd/gardener_of_echoes_cinematic_opening_index_0.jpeg

---

### gen image

<sub>5/17/2026, 12:13:07 PM</sub>

![image](https://r2-bucket.flowith.net/f/d46502a7eb7752a2/data_flower_circuit_board_index_2.jpeg)

https://r2-bucket.flowith.net/f/d46502a7eb7752a2/data_flower_circuit_board_index_2.jpeg

---

### gen image

<sub>5/17/2026, 12:13:07 PM</sub>

![image](https://r2-bucket.flowith.net/f/dcb9d45493d3b789/gardener_global_network_finale_index_4.jpeg)

https://r2-bucket.flowith.net/f/dcb9d45493d3b789/gardener_global_network_finale_index_4.jpeg

---

### gen video segment

<sub>5/17/2026, 12:14:26 PM</sub>

[Video](https://vg.flowith.net/tencent/1412218316-AigcVideoTask-f8883aae163fe7230dfd2531e2ed6f7et.mp4)

---

### gen video segment

<sub>5/17/2026, 12:14:26 PM</sub>

[Video](https://vg.flowith.net/tencent/1412218316-AigcVideoTask-28764abe4a5e28310af4ca7463d8976ct.mp4)

---

### gen video segment

<sub>5/17/2026, 12:14:26 PM</sub>

[Video](https://vg.flowith.net/tencent/1412218316-AigcVideoTask-9ceacc145e04e250f42a0230faec91d8t.mp4)

---

### gen video segment

<sub>5/17/2026, 12:14:26 PM</sub>

[Video](https://vg.flowith.net/tencent/1412218316-AigcVideoTask-ecd97223de3e7e73e9f51a01e23491fdt.mp4)

---

### gen video segment

<sub>5/17/2026, 12:14:27 PM</sub>

[Video](https://vg.flowith.net/tencent/1412218316-AigcVideoTask-2cf743a9319ed7c8ed481e5f31ec9878t.mp4)

---

### combine video

<sub>5/17/2026, 12:16:24 PM</sub>

[Video](https://r2-bucket.flowith.net/concat_1779012993538996307.mp4)

---

### refine webpage

<sub>5/17/2026, 12:17:09 PM</sub>

[Webpage](https://flo.fun/8wu3yf_)
