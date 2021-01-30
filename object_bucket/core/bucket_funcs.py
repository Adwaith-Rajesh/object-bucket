from appdirs import user_data_dir
from contextlib import suppress
import os


def remove_bucket(bucket_name: str) -> None:
    """Tries to remove the bucket with given name"""
    bucket_file = os.path.join(user_data_dir("buckets", "Object-Bucket"), bucket_name)
    with suppress(FileNotFoundError):
        os.remove(bucket_file)