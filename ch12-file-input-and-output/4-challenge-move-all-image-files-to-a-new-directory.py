# 12.4 Challenge: Move All Image Files To a New Directory
# Solution to Challenge

from pathlib import Path

# Change this path to match the location on your computer
documents_dir = Path.cwd() / "practice_files" / "documents"

# Create an images/ directory in your home directory
images_dir = Path.home() / "images"
images_dir.mkdir(exist_ok=True)

# Search for image files in the documents directory and move
# them to the images/ directory
for path in documents_dir.rglob("*.*"):
    if path.suffix.lower() in [".png", ".jpg", ".gif"]:
        path.replace(images_dir / path.name)
