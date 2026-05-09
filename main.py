import asyncio
import sys
from pathlib import Path

import edge_tts

INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")
VOICE = "de-DE-KatjaNeural"


async def process_file(txt_file: Path) -> None:
    text = txt_file.read_text(encoding="utf-8").strip()
    if not text:
        print(f"  Übersprungen (leer): {txt_file.name}")
        return

    out_file = OUTPUT_DIR / txt_file.with_suffix(".mp3").name
    print(f"  {txt_file.name} -> {out_file.name}")
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(str(out_file))


async def main() -> None:
    INPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)

    txt_files = sorted(INPUT_DIR.glob("*.txt"))
    if not txt_files:
        print(f"Keine .txt-Dateien in '{INPUT_DIR}' gefunden.")
        sys.exit(0)

    print(f"Stimme: {VOICE}\n{len(txt_files)} Datei(en) gefunden:\n")
    for txt_file in txt_files:
        await process_file(txt_file)

    print(f"\nFertig. Audio-Dateien in '{OUTPUT_DIR}'.")


if __name__ == "__main__":
    asyncio.run(main())
