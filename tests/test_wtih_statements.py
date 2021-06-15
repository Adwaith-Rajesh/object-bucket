import os
from pathlib import Path

import pytest

from object_bucket import Bucket


@pytest.fixture()
def file_():
    file_name = "py-test-with"
    yield file_name
    os.remove(os.path.join(".", file_name))


def test_with_stmt_file_creation_on_exit(file_) -> None:
    """tests whether the file is made during exit"""
    with Bucket(file_) as _:
        pass

    file_dir = os.path.join(".", "py-test-with")
    assert Path(file_dir).is_file() is True


def test_with_stmt_add_droplet(file_) -> None:
    """test whether the droplet can be added using a context manager"""
    with Bucket(file_) as b:
        demo_drop = [1, 2, 3]
        b.add_droplet("demo", demo_drop)

        assert b.check_droplet_exists("demo")


def test_with_stmt_get_droplet(file_) -> None:
    """test whether the droplet can be added using a context manager"""
    with Bucket(file_) as b:
        b.add_droplet("demo", 1)
        a = b.get_droplet("demo")

        assert a == 1


def test_with_stmt_modify_droplet(file_) -> None:
    """test whether the droplet can be added using a context manager"""
    with Bucket(file_) as b:
        b.add_droplet("demo", 1)
        b.modify_droplet("demo", [1, 2, 3])
        assert b.get_droplet("demo") == [1, 2, 3]


def test_with_stmt_remove_droplet(file_) -> None:
    """test whether the droplet can be added using a context manager"""
    with Bucket(file_) as b:
        b.add_droplet("demo", 1)
        assert b.check_droplet_exists("demo") is True
        b.remove_droplet("demo")
        assert b.check_droplet_exists("demo") is False
