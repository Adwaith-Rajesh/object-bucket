import pytest

from object_bucket import Bucket
from object_bucket.errors import DropletDoesNotExistsError
from object_bucket.errors import DropletExistsError
from object_bucket.errors import DropletTypeError


@pytest.fixture()
def bucket_to_test():
    bucket = Bucket("pytest-bucket")
    yield bucket
    bucket.delete_bucket()


def test_droplet_does_not_exists_error(bucket_to_test: Bucket) -> None:
    """raised when trying to get, or modify a droplet that does not exists """

    with pytest.raises(DropletDoesNotExistsError):
        bucket_to_test.get_droplet("test")

    with pytest.raises(DropletDoesNotExistsError):
        bucket_to_test.modify_droplet("test", 2)


def test_droplet_exists_error(bucket_to_test: Bucket) -> None:
    """Raised when trying to add a droplet that already exists"""
    demo_droplet = [1, 2, 3]
    bucket_to_test.add_droplet("demo", demo_droplet)

    with pytest.raises(DropletExistsError):
        bucket_to_test.add_droplet("demo", 2)


def test_droplet_type_error(bucket_to_test: Bucket) -> None:
    """Raised when an object that cannot be saved is added or modified into the bucket"""
    # one example, generators cannot be saved
    def foo():
        yield 1
        yield 2

    # adding droplet
    with pytest.raises(DropletTypeError):
        f = foo()
        bucket_to_test.add_droplet("demo", f)

    # modifying a droplet
    with pytest.raises(DropletTypeError):
        f = foo()
        bucket_to_test.add_droplet("demo", 1)
        bucket_to_test.modify_droplet("demo", f)
