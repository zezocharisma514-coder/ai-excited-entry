from pathlib import Path


SOURCE = Path("/bot/entry.png")
TARGET = Path("/output/entry.png")


def main():
    image_bytes = SOURCE.read_bytes()
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(image_bytes)


if __name__ == "__main__":
    main()
