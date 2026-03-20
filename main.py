import sys
import os
from pathlib import Path

from src.sheep_counter import count_sheep

def main():
    os.chdir(Path(__file__).parent)
    
    if len(sys.argv) < 2:
        print("Usage: python count_sheep.py <image1> <image2> ...")
        sys.exit(1)

    image_paths = sys.argv[1:]

    missing = [p for p in image_paths if not Path(p).resolve().exists()]
    if missing:
        print(f"Failed to find files: {missing}")
        sys.exit(1)

    print(f"Processing {len(image_paths)} images...\n")
    total = count_sheep(image_paths)
    print(f"\n{'='*40}")
    print(f"Total number of sheep: {total}")
    print(f"{'='*40}")

    with open("output.txt", "w") as ouptut:
        print(total, file=ouptut)


if __name__ == "__main__":
    main()
