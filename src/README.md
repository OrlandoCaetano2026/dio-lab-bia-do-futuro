# Step by step to execute the system

## Setup to Ollama
```
- 1 Install Ollama.ai
- 2 download a model fast (Example GPT-OSS) to run in laptop local
- 3 Execut a test of work
  ollama run gpt-oss "Olá""
```

## Complet code

Complete code in file `agente.py`


## How to run

```bash
# 1. Install librarys
pip install streamlit pandas requests

# 2. Ensure that Ollama are working
ollama serve

# 3. Run the app
streamlit run agente.py
```
