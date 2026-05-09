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
        print(f"  Skipped (empty): {txt_file.name}")
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
        print(f"No .txt files found in '{INPUT_DIR}'.")
        sys.exit(0)

    print(f"Voice: {VOICE}\n{len(txt_files)} file(s) found:\n")
    for txt_file in txt_files:
        await process_file(txt_file)

    print(f"\nDone. Audio files saved to '{OUTPUT_DIR}'.")


if __name__ == "__main__":
    asyncio.run(main())
