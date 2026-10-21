# Sovereign Agent Setup And Deployment

Docker image:

```bash
docker pull sovereignai/sovereign-agent
docker run -p 50001:80 sovereignai/sovereign-agent
```

Persist user data by mounting `/a0/usr`:

```bash
docker run -p 50001:80 -v /path/on/host:/a0/usr sovereignai/sovereign-agent
```

After first start, configure API keys, chat model, utility model, and embedding model in Settings. Embeddings are required for memory and knowledge recall.

For local development:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run_ui.py
```

Typical troubleshooting:
- Web UI unreachable: check `docker ps`, port mapping, and startup logs.
- Model errors: verify provider, model name, and API key.
- Memory/knowledge not recalling: verify embedding config and reindex if needed.
- Host-local access: use A0 CLI connector tools, not Docker tools.
