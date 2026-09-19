---
title: First Agent Template
emoji: ⚡
colorFrom: pink
colorTo: yellow
sdk: gradio
sdk_version: 5.23.1
app_file: app.py
pinned: false
tags:
- smolagents
- agent
- smolagent
- tool
- agent-course
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

## Run with Ollama

Install Ollama, pull a model, and make sure the Ollama server is running:

```powershell
ollama pull qwen2:7b
ollama serve
```

Then start the app in the project virtual environment:

```powershell
python app.py
```

The app uses `http://localhost:11434/v1` and `qwen2:7b` by default. To use a different local model or endpoint, set `OLLAMA_MODEL` and `OLLAMA_BASE_URL` before starting the app.
