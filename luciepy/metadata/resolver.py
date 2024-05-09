import exiftool


def get_metadata(path: str):
    with exiftool.ExifToolHelper() as et:
        return et.get_metadata(path)

