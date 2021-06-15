import os
from pathlib import Path

from appdirs import user_data_dir

from object_bucket import Bucket
from object_bucket import remove_bucket


def test_sd_remove_bucket():
    """Tests whether the function ```remove_bucket``` is able to delete the bucket file."""
    with Bucket("py-del-bk") as _:
        ...

    bucket_file = os.path.join(user_data_dir(
        "buckets", "Object-Bucket"), "py-del-bk")
    assert Path(bucket_file).is_file() is True

    remove_bucket("py-del-bk")
    bucket_file = os.path.join(user_data_dir(
        "buckets", "Object-Bucket"), "py-del-bk")
    assert Path(bucket_file).is_file() is False
