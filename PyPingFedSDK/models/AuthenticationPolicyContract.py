class AuthenticationPolicyContract():
    """Authentication Policy Contracts carry user attributes from the identity provider to the service provider.

    Attributes
    ----------
    coreAttributes : array
 A list of read-only assertion attributes (for example, subject) that are automatically populated by PingFederate.
    extendedAttributes : array
 A list of additional attributes as needed.
    id : string
 The persistent, unique ID for the authentication policy contract. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.
    name : string
 The Authentication Policy Contract Name. Name is unique.

    """

<<<<<<< HEAD
    def __init__(self, coreAttributes=None, extendedAttributes=None, var_id=None, name=None) -> None:
        self.coreAttributes = coreAttributes
        self.extendedAttributes = extendedAttributes
        self.var_id = var_id
        self.name = name
=======
    def __init__(self, coreAttributes=None, extendedAttributes=None, id=None, name=None):
        self.coreAttributes: list = coreAttributes
        self.extendedAttributes: list = extendedAttributes
        self.id: str = id
        self.name: str = name
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthenticationPolicyContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.coreAttributes, self.extendedAttributes, self.var_id, self.name))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["coreAttributes", "extendedAttributes", "var_id", "name"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
