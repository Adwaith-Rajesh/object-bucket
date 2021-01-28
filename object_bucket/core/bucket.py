from contextlib import suppress
from pathlib import Path

from typing import Any
import os


from appdirs import user_data_dir
import dill


from object_bucket.errors.bucket_error import DropletDoesNotExistsError




class Bucket:
    """Load, save and modify buckets"""

    def __init__(self, bucket: str) -> None:
        self.__object_bucket_path = user_data_dir("buckets", "Object-Bucket")
        print(self.__object_bucket_path)

        # A dict to store a retrieve data during runtime
        self.__temp_bucket = {}

        self.__make_required_directories()

    def get_droplet(self, droplet_name:str) -> Any:
        """Gets the droplet the given name, raises error when the droplet does not exists"""
        try:
            obj = self.__temp_bucket[droplet_name]
            return obj

        except KeyError:
            raise DropletDoesNotExistsError(droplet_name)


    def add_droplet(self, droplet_name: str, obj: object) -> None:
        """Adds a new droplet to the bucket and raises an error if the droplet with the same name already exists."""
        pass

    def modify_droplet(self, droplet_name: str, obj) -> None:
        """Modifies the given droplet raises an error if the droplet does not exists"""
        pass

    def save_bucket(self):
        """Save the current changes and modification to the bucket.
        Should be called at the end of all the modification and addition in order to save the droplets permanently.
        """

    def __make_required_directories(self):
       Path(self.__object_bucket_path).mkdir(parents=True, exist_ok=True)