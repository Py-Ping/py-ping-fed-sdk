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

    def __init__(self, coreAttributes:list=None, extendedAttributes:list=None, var_id:str=None, name:str=None) -> None:
        self.coreAttributes = coreAttributes
        self.extendedAttributes = extendedAttributes
        self.var_id = var_id
        self.name = name

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
        return hash(frozenset([self.coreAttributes, self.extendedAttributes, self.var_id, self.name]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["coreAttributes", "extendedAttributes", "var_id", "name"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__