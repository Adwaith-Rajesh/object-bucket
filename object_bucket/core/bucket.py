from contextlib import suppress
from pathlib import Path

from typing import Any
import os


from appdirs import user_data_dir
import dill


from object_bucket.errors.bucket_error import DropletDoesNotExistsError, DropletExistsError
from object_bucket.errors.bucket_error import DropletTypeError


class Bucket:
    """Load, save and modify buckets"""

    def __init__(self, bucket: str) -> None:

        self.bucket_name = bucket

        self.__object_bucket_path = user_data_dir("buckets", "Object-Bucket")
        self.__bucket_file_path = os.path.join(self.__object_bucket_path, self.bucket_name)
        

        # A dict to store a retrieve data during runtime
        self.__temp_bucket = {}

        self.__make_required_directories()
        self.__load_bucket()

    def __repr__(self) -> str:
        return str(self.__temp_bucket)


    def __make_required_directories(self):
        Path(self.__object_bucket_path).mkdir(parents=True, exist_ok=True)

    def __load_bucket(self):
        b_file = Path(self.__bucket_file_path)
        if b_file.is_file():
            with open(self.__bucket_file_path, "rb") as f:
                self.__temp_bucket = dill.load(f)

    def get_droplet(self, droplet_name:str) -> Any:
        """Gets the droplet the given name, raises error when the
             droplet does not exists"""
        try:
            obj = self.__temp_bucket[droplet_name]
            return obj

        except KeyError:
            raise DropletDoesNotExistsError(droplet_name)


    def add_droplet(self, droplet_name: str, obj: object) -> None:
        """Adds a new droplet to the bucket and raises an error if 
        the droplet with the same name already exists."""

        if self.check_droplet_exists(droplet_name):
            raise DropletExistsError(droplet_name)

        if not dill.pickles(obj):
            raise DropletTypeError(droplet_name, obj)
        
        self.__temp_bucket[droplet_name] = obj

    def modify_droplet(self, droplet_name: str, obj) -> None:
        """Modifies the given droplet raises an error if the droplet
             does not exists"""
        self.__temp_bucket[droplet_name] = obj

    def remove_droplet(self, droplet_name: str) -> None:
        if droplet_name in self.__temp_bucket:
            del self.__temp_bucket[droplet_name]

        else:
            raise DropletDoesNotExistsError(droplet_name)

    def save_bucket(self):
        """Save the current changes and modification to the bucket.
        Should be called at the end of all the modification and addition
         in order to save the droplets permanently.
        """

        with open(self.__bucket_file_path, "wb") as f:
            dill.dump(self.__temp_bucket, f)

    def delete_bucket(self):
        """deletes all the permanently stored droplets from a bucket,
        and remove all the droplets from the runtime storage.
        """

        self.__temp_bucket.clear()
        with suppress(FileNotFoundError):
            os.remove(self.__bucket_file_path)

    def check_droplet_exists(self, droplet_name: str) -> bool:
        return True if droplet_name in self.__temp_bucket else False

