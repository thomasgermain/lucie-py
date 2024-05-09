import sys

from luciepy.metadata import resolver

if __name__ == "__main__":
    directory = sys.argv[1]
    metadata = resolver.get_metadata(directory)
    for m in metadata:
        print(f"Metadata for file {m['File:FileName']}")
        print(f"FileSize: {m['File:FileSize']}")
        print(f"Creation time: {m['EXIF:DateTimeOriginal']}")
        print("---")
