# hello-world-posit-connect

A minimal Shiny for Python app used to smoke-test a Posit Connect deployment. It takes a name, greets
you, and reports the hostname and Python version of the pod that served the request, so you can confirm
content is actually running on Connect rather than being cached.

## Run locally

Requires Python 3.12.

```bash
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -r requirements.txt
shiny run app.py
```

Open http://127.0.0.1:8000 in a browser.

## Deploying to Posit Connect

Deployment uses [rsconnect-python](https://docs.posit.co/rsconnect-python/), with the app bundle
described by the committed `manifest.json`.

### One-time setup

```bash
uv pip install rsconnect-python
rsconnect add --server "$CONNECT_SERVER" --api-key "$CONNECT_API_KEY" --name posit
```

### Regenerating the manifest

Run this after changing `app.py` or `requirements.txt`, and commit the result:

```bash
rsconnect write-manifest shiny . --overwrite \
  --exclude ".venv" --exclude ".idea" \
  --exclude ".editorconfig" --exclude ".gitignore" --exclude ".python-version" --exclude "README.md"
```

### Deploy

```bash
rsconnect deploy manifest manifest.json --title "Hello World"
```

Connect rebuilds the Python environment described in `manifest.json` and `requirements.txt`, so no
local virtual environment is uploaded.
