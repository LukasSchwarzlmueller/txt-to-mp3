# txt-to-mp3

Converts `.txt` files to MP3 audio using neural voices via [edge-tts](https://github.com/rany2/edge-tts). Supports German and English voices.

## Features

- **CLI** (`main.py`): Batch-converts all `.txt` files in the `input/` folder and saves MP3s to `output/`
- **Web API** (`server.py`): FastAPI server with file upload endpoint and voice selection
- **Docker**: Ready-to-use `docker-compose.yml` for easy deployment

## Available Voices

### German

| Voice | Region | Gender |
|-------|--------|--------|
| de-DE-KatjaNeural | Germany | Female |
| de-DE-ConradNeural | Germany | Male |
| de-AT-IngridNeural | Austria | Female |
| de-AT-JonasNeural | Austria | Male |
| de-CH-LeniNeural | Switzerland | Female |
| de-CH-JanNeural | Switzerland | Male |

### English

| Voice | Region | Gender |
|-------|--------|--------|
| en-US-AriaNeural | US | Female |
| en-US-GuyNeural | US | Male |
| en-GB-SoniaNeural | UK | Female |
| en-GB-RyanNeural | UK | Male |
| en-AU-NatashaNeural | Australia | Female |
| en-AU-WilliamNeural | Australia | Male |

## Usage

### CLI

```bash
# Install dependencies (requires uv)
uv sync

# Place .txt files in input/, then run:
uv run python main.py
```

To change the voice, edit the `VOICE` constant in [main.py](main.py).

### Web Server

```bash
uv run uvicorn server:app --reload
```

API available at `http://localhost:8000`.

### Docker

```bash
docker compose up
```

## API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/voices` | GET | List all available voices |
| `/tts` | POST | Upload a `.txt` file, receive an MP3 |

### Example

```bash
curl -X POST http://localhost:8000/tts \
  -F "file=@mytext.txt" \
  -F "voice=en-US-AriaNeural" \
  -o output.mp3
```

## License

[MIT](LICENSE)
