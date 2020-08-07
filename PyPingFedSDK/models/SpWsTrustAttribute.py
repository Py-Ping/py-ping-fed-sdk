class SpWsTrustAttribute():
    """An attribute for the Ws-Trust attribute contract.

    Attributes
    ----------
    name : string
 The name of this attribute.
    namespace : string
 The attribute namespace.  This required when the Default Token Type is SAML1.1 or SAML1.1 for Office 365.

    """

    def __init__(self, namespace, name) -> None:
        self.name = name
        self.namespace = namespace

    def _validate(self) -> bool:
        return any(x for x in ["namespace", "name"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SpWsTrustAttribute):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.name, self.namespace))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["name", "namespace"]}

        return cls(**valid_data)