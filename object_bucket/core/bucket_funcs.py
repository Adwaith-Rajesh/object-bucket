from appdirs import user_data_dir
from contextlib import suppress
import os


def remove_bucket(bucket_name: str, bucket_file_path:str = None) -> None:
    """Tries to remove the bucket with given name"""
    if not bucket_file_path:
        bucket_file = os.path.join(user_data_dir("buckets", "Object-Bucket"), bucket_name)
    else:
        bucket_file = bucket_file_path
    with suppress(FileNotFoundError):
        os.remove(bucket_file)