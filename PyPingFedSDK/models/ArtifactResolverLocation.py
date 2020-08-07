class ArtifactResolverLocation():
    """The remote party URLs to resolve the artifact.

    Attributes
    ----------
    index : integer
 The priority of the endpoint.
    url : string
 Remote party URLs that you will use to resolve/translate the artifact and get the actual protocol message

    """

<<<<<<< HEAD
    def __init__(self, index, url) -> None:
        self.index = index
        self.url = url
=======
    def __init__(self, index, url):
        self.index: str = index
        self.url: str = url
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in ["index", "url"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ArtifactResolverLocation):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.index, self.url))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["index", "url"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
