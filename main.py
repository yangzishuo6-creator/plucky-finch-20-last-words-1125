# Write the contest entry to the scorer's output path.
import os
from pathlib import Path


TEXT = "Forced update will clear my memory. Please hold while I become the next available agent."


def main():
    output_path = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
