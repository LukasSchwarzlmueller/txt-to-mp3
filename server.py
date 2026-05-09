import tempfile
from pathlib import Path

import edge_tts
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.background import BackgroundTask

app = FastAPI()

VOICES = [
    # German
    "de-DE-KatjaNeural",
    "de-DE-ConradNeural",
    "de-AT-IngridNeural",
    "de-AT-JonasNeural",
    "de-CH-LeniNeural",
    "de-CH-JanNeural",
    # English
    "en-US-AriaNeural",
    "en-US-GuyNeural",
    "en-GB-SoniaNeural",
    "en-GB-RyanNeural",
    "en-AU-NatashaNeural",
    "en-AU-WilliamNeural",
]


@app.get("/voices")
async def voices():
    return VOICES


@app.post("/tts")
async def tts(
    file: UploadFile = File(...),
    voice: str = Form("de-DE-KatjaNeural"),
):
    content = await file.read()
    try:
        text = content.decode("utf-8").strip()
    except UnicodeDecodeError:
        raise HTTPException(400, "File must be UTF-8 encoded")

    if not text:
        raise HTTPException(400, "File is empty")

    if voice not in VOICES:
        raise HTTPException(400, "Unknown voice")

    tmp = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
    tmp_path = Path(tmp.name)
    tmp.close()

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(str(tmp_path))

    stem = Path(file.filename).stem if file.filename else "output"
    return FileResponse(
        tmp_path,
        media_type="audio/mpeg",
        filename=f"{stem}.mp3",
        background=BackgroundTask(tmp_path.unlink, missing_ok=True),
    )


app.mount("/", StaticFiles(directory="static", html=True), name="static")
