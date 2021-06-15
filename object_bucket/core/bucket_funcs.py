import os
from contextlib import suppress


def remove_bucket(bucket_path: str) -> None:
    """Tries to remove the bucket with given name"""
    with suppress(FileNotFoundError):
        os.remove(bucket_path)
