from typing import List, Dict, Any

from exiftool import ExifToolHelper


def get_metadata(path: str) -> List[Dict[str, Any]]:
    with ExifToolHelper() as et:
        return et.get_metadata(path)  # type: ignore[no-any-return]
