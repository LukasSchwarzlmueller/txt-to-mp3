import tempfile
from pathlib import Path

import edge_tts
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.background import BackgroundTask

app = FastAPI()

VOICES = [
    "de-DE-KatjaNeural",
    "de-DE-ConradNeural",
    "de-AT-IngridNeural",
    "de-AT-JonasNeural",
    "de-CH-LeniNeural",
    "de-CH-JanNeural",
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
        raise HTTPException(400, "Datei muss UTF-8 kodiert sein")

    if not text:
        raise HTTPException(400, "Datei ist leer")

    if voice not in VOICES:
        raise HTTPException(400, "Unbekannte Stimme")

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
