import os
from pathlib import Path

SUBDIRECTORIES = {
  "documents": ['.pdf', '.rtf', '.txt'],
  "audio": ['.m4a', '.m4b', '.mp3'],
  "vidoes": ['.mov', '.avi', '.mp4'],
  "images": ['.jpg', '.jpeg', '.png']
}


def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    # Fallback dir
    return 'misc'


def organizeDirectory():
    for item in os.scandir():
        # Skip - No need to organize directories
        if item.is_dir():
            continue

        filePath = Path(item)
        filetype = filePath.suffix.lower()

        if filetype == '.py':
            # Skip - keep python files at root
            continue

        directory = pickDirectory(filetype)
        directoryPath = Path(directory)

        if not directoryPath.is_dir():
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))


organizeDirectory()
