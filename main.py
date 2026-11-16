from pathlib import Path
import shutil

SOURCE = Path("/bot/entry.png")
DESTINATION = Path("/output/entry.png")

def main():
    if not SOURCE.is_file():
        raise FileNotFoundError(SOURCE)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DESTINATION)

if __name__ == "__main__":
    main()
