import os
import shutil
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import sys


def copy_file(file_path, dest_dir):
    ext = file_path.suffix[1:]
    if not ext:
        ext = 'no_extension'

    ext_dir = dest_dir / ext
    ext_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy(file_path, ext_dir / file_path.name)


def process_directory(src_dir, dest_dir):
    with ThreadPoolExecutor() as executor:
        for root, _, files in os.walk(src_dir):
            for file in files:
                file_path = Path(root) / file
                executor.submit(copy_file, file_path, dest_dir)


def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до джерельної директорії.")
        return

    src_dir = Path(sys.argv[1])
    dest_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not src_dir.is_dir():
        print("Джерельна директорія не існує.")
        return

    dest_dir.mkdir(parents=True, exist_ok=True)

    process_directory(src_dir, dest_dir)
    print(f"Файли скопійовані у {dest_dir}")


if __name__ == "__main__":
    main()
