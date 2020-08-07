class AccessTokenAttributeContract():
    """A set of attributes exposed by an Access Token Manager.

    Attributes
    ----------
    coreAttributes : array
 A list of core token attributes that are associated with the access token management plugin type. This field is read-only and is ignored on POST/PUT.
    defaultSubjectAttribute : string
 Default subject attribute to use for audit logging when validating the access token. Blank value means to use USER_KEY attribute value after grant lookup.
    extendedAttributes : array
 A list of additional token attributes that are associated with this access token management plugin instance.
    inherited : boolean
 Whether this attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false.

    """

<<<<<<< HEAD
    def __init__(self, coreAttributes=None, defaultSubjectAttribute=None, extendedAttributes=None, inherited=None) -> None:
        self.coreAttributes = coreAttributes
        self.defaultSubjectAttribute = defaultSubjectAttribute
        self.extendedAttributes = extendedAttributes
        self.inherited = inherited
=======
    def __init__(self, coreAttributes=None, defaultSubjectAttribute=None, extendedAttributes=None, inherited=None):
        self.coreAttributes: list = coreAttributes
        self.defaultSubjectAttribute: str = defaultSubjectAttribute
        self.extendedAttributes: list = extendedAttributes
        self.inherited: bool = inherited
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AccessTokenAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.coreAttributes, self.defaultSubjectAttribute, self.extendedAttributes, self.inherited))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["coreAttributes", "defaultSubjectAttribute", "extendedAttributes", "inherited"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
