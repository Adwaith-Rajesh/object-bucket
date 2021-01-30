from appdirs import user_data_dir
from object_bucket import remove_bucket, Bucket
from pathlib import Path
import os

def test_sd_remove_bucket():
    """Tests whether the function ```remove_bucket``` is able to delete the bucket file."""
    with Bucket("py-del-bk") as _: ...

    bucket_file = os.path.join(user_data_dir("buckets", "Object-Bucket"), "py-del-bk")
    assert Path(bucket_file).is_file() == True

    remove_bucket("py-del-bk")
    bucket_file = os.path.join(user_data_dir("buckets", "Object-Bucket"), "py-del-bk")
    assert Path(bucket_file).is_file() == False