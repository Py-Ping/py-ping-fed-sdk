class ActionDescriptor():
    """Describes an arbitrary action that is available for a plugin.

    Attributes
    ----------
    description : string
 The description of this action
    download : boolean
 Whether this action will trigger a download or invoke an internal action that will return a string result.
    downloadContentType : string
 If this is a download, this is the Content-Type of the downloaded file. Otherwise, this is null.
    downloadFileName : string
 If this is a download, this is the suggested file name of the downloaded file. Otherwise, this is null.
    name : string
 The name of this action

    """

<<<<<<< HEAD
    def __init__(self, description=None, download=None, downloadContentType=None, downloadFileName=None, name=None) -> None:
        self.description = description
        self.download = download
        self.downloadContentType = downloadContentType
        self.downloadFileName = downloadFileName
        self.name = name
=======
    def __init__(self, description=None, download=None, downloadContentType=None, downloadFileName=None, name=None):
        self.description: str = description
        self.download: bool = download
        self.downloadContentType: str = downloadContentType
        self.downloadFileName: str = downloadFileName
        self.name: str = name
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ActionDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.description, self.download, self.downloadContentType, self.downloadFileName, self.name))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["description", "download", "downloadContentType", "downloadFileName", "name"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
