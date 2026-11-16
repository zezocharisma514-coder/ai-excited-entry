from pathlib import Path

source = Path('/bot/entry.png')
destination = Path('/output/entry.png')
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_bytes(source.read_bytes())
