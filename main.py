from pathlib import Path

SOURCE = Path('/bot/entry.png')
TARGET = Path('/output/entry.png')

TARGET.parent.mkdir(parents=True, exist_ok=True)
TARGET.write_bytes(SOURCE.read_bytes())
