from object_bucket import Bucket
from appdirs import user_data_dir  # To get the path to the file
from pathlib import Path
import pytest
import os

@pytest.fixture()
def bucket_to_test():
    bucket = Bucket("pytest-bucket")
    yield bucket
    bucket.delete_bucket()


def test_bucket_file_creation(bucket_to_test: Bucket):
    file_dir = os.path.join(user_data_dir("buckets", "Object-Bucket"), "pytest-bucket")
    bucket_to_test.save_bucket()
    assert Path(file_dir).is_file() == True

def test_bucket_droplet_addition(bucket_to_test: Bucket) -> None:
    demo_droplet = [1, 2, 3]
    bucket_to_test.add_droplet("demo", demo_droplet)
    assert bucket_to_test.check_droplet_exists("demo") == True

def test_bucket_get(bucket_to_test: Bucket) -> None:
    demo_droplet = {1: "a", 2: "b"}
    bucket_to_test.add_droplet("demo", demo_droplet)
    assert bucket_to_test.get_droplet("demo") == {1: "a", 2: "b"}

def test_bucket_modification(bucket_to_test: Bucket) -> None:
    demo_droplet = [20, 30, 40]
    replace_droplet = ["a", "b", "c"]
    bucket_to_test.add_droplet("demo", demo_droplet)
    bucket_to_test.modify_droplet("demo", replace_droplet)
    assert bucket_to_test.get_droplet("demo") == ["a", "b", "c"]


def test_remove_droplet(bucket_to_test: Bucket) -> None:
    demo_droplet = [10, 20, 30]
    bucket_to_test.add_droplet("demo", demo_droplet)
    assert bucket_to_test.check_droplet_exists("demo") == True
    bucket_to_test.remove_droplet("demo")
    assert bucket_to_test.check_droplet_exists("demo") == False


def test_get_all_droplets(bucket_to_test: Bucket) -> None:
    drop1 = [1, 2, 3, 4]
    drop2 = "Hello"
    drop3 = {1: "a", 2: "b"}
    bucket_to_test.add_droplet("drop1", drop1)
    bucket_to_test.add_droplet("drop2", drop2)
    bucket_to_test.add_droplet("drop3", drop3)

    rv = bucket_to_test.get_all_droplets()
    assert rv == {
        "drop1": [1, 2, 3, 4],
        "drop2": "Hello",
        "drop3": {
            1: "a",
            2: "b"
        }
    }


def test_bucket_add_droplets(bucket_to_test: Bucket) -> None:
    droplets = {
        "one": 1,
        "two": 2,
        "three": [2, 3, 4]
    }

    bucket_to_test.add_droplets(droplets)
    assert bucket_to_test.check_droplet_exists("one") == True
    assert bucket_to_test.check_droplet_exists("two") == True
    assert bucket_to_test.check_droplet_exists("three") == True
    assert bucket_to_test.get_droplet("one") == 1
    assert bucket_to_test.get_droplet("two") == 2
    assert bucket_to_test.get_droplet("three") == [2, 3, 4]
    

def test_if_stmt(bucket_to_test: Bucket) -> None:
    bucket_to_test.add_droplet("demo", 1)
    w = False
    if bucket_to_test:
        w = True
    assert w == True

    bucket_to_test.remove_droplet("demo")
    n = False
    if bucket_to_test:
        n = True

    assert n == False

def test_bucket_len(bucket_to_test: Bucket) -> None:
    assert len(bucket_to_test) == 0
    for i in range(10):
        bucket_to_test.add_droplet(str(i), i)

    assert len(bucket_to_test) == 10
