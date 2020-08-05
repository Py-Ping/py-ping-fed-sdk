class SpBrowserSsoAttributeContract():
    """A set of user attributes that the IdP sends in the SAML assertion.

    Attributes
    ----------
    coreAttributes : array
        A list of read-only assertion attributes (for example, SAML_SUBJECT) that are automatically populated by PingFederate.    extendedAttributes : array
        A list of additional attributes that are added to the outgoing assertion.
    """

    __slots__ = ["coreAttributes", "extendedAttributes"]

    def __init__(self, coreAttributes=None, extendedAttributes=None):
        self.coreAttributes = coreAttributes
        self.extendedAttributes = extendedAttributes

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SpBrowserSsoAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.coreAttributes, self.extendedAttributes))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["coreAttributes", "extendedAttributes"]}

        return cls(**valid_data)
