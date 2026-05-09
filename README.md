# txt-to-mp3

Konvertiert `.txt`-Dateien in MP3-Audiodateien mit deutschen Stimmen via [edge-tts](https://github.com/rany2/edge-tts).

## Features

- **CLI** (`main.py`): Verarbeitet alle `.txt`-Dateien im `input/`-Ordner und speichert die MP3s in `output/`
- **Web-API** (`server.py`): FastAPI-Server mit Upload-Endpunkt und Stimmauswahl
- **Docker**: Fertige `docker-compose.yml` für einfaches Deployment

## Verfügbare Stimmen

| Stimme | Region |
|--------|--------|
| de-DE-KatjaNeural | Deutschland (weiblich) |
| de-DE-ConradNeural | Deutschland (männlich) |
| de-AT-IngridNeural | Österreich (weiblich) |
| de-AT-JonasNeural | Österreich (männlich) |
| de-CH-LeniNeural | Schweiz (weiblich) |
| de-CH-JanNeural | Schweiz (männlich) |

## Verwendung

### CLI

```bash
# Abhängigkeiten installieren (uv)
uv sync

# .txt-Dateien in input/ legen, dann:
uv run python main.py
```

### Web-Server

```bash
uv run uvicorn server:app --reload
```

API läuft dann auf `http://localhost:8000`.

### Docker

```bash
docker compose up
```

## API

| Endpunkt | Methode | Beschreibung |
|----------|---------|--------------|
| `/voices` | GET | Liste der verfügbaren Stimmen |
| `/tts` | POST | `.txt`-Datei hochladen, MP3 zurückbekommen |
