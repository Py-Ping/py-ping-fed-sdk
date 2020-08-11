class AttributeQueryNameMapping():
    """The attribute query name mappings between the SP and the IdP.

    Attributes
    ----------
    localName : string
 The local attribute name.
    remoteName : string
 The remote attribute name as defined by the attribute authority.

    """

    def __init__(self, localName:str, remoteName:str) -> None:
        self.localName = localName
        self.remoteName = remoteName

    def _validate(self) -> bool:
        return any(x for x in ["localName", "remoteName"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AttributeQueryNameMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.localName, self.remoteName))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["localName", "remoteName"]}

        return cls(**valid_data)