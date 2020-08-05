class LicenseFile():
    """ License to import.

    Attributes
    ----------
    fileData : string
        The base64-encoded license file.

    """

    __slots__ = ["fileData"]
    def __init__(self, fileData):
            self.fileData = fileData
    
    def _validate(self):
        return any(x for x in ['fileData'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, LicenseFile):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((fileData))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
