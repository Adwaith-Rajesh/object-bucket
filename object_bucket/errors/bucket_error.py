
class DropletDoesNotExistsError(Exception):
    """Raised when a non defined droplet is modified"""

    def __init__(self, name: str) -> None:
        """
        :param name: name of the droplet
        :type name: str
        :returns: nothing
        :rtype: None
        """
        self.name = name
        self.msg = f"Droplet {self.name} does not exists..."

    def __str__(self) -> str:
        return self.msg


class DropletExistsError(Exception):
    """Raises when the droplet that already exists in a bucket is re initialized."""
    
    def __init__(self, droplet_name: str) -> None:
        self.name = droplet_name
        self.message = f"The droplet {self.name} already exists'..."

    def __str__(self) -> str:
        return self.message


class DropletTypeError(Exception):
    """Raised when the object type cannot be pickled"""

    def __init__(self, droplet_name: str, obj: object) -> None:
        self.droplet_name = droplet_name
        self.message = f"Droplet of type '{type(obj)}' cannot be saved..."

    def __str__(self) -> str:
        return self.message