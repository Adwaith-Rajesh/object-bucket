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