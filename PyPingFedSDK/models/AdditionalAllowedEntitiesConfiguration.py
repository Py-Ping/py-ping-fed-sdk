class AdditionalAllowedEntitiesConfiguration():
    """Additional allowed entities or issuers configuration. Currently only used in OIDC IdP (RP) connection.

    Attributes
    ----------
    additionalAllowedEntities : array
        An array of additional allowed entities or issuers to be accepted during entity or issuer validation.    allowAdditionalEntities : boolean
        Set to true to configure additional entities or issuers to be accepted during entity or issuer validation.    allowAllEntities : boolean
        Set to true to accept any entity or issuer during entity or issuer validation. (Not Recommended)
    """

    __slots__ = ["additionalAllowedEntities", "allowAdditionalEntities", "allowAllEntities"]

    def __init__(self, additionalAllowedEntities=None, allowAdditionalEntities=None, allowAllEntities=None):
        self.additionalAllowedEntities = additionalAllowedEntities
        self.allowAdditionalEntities = allowAdditionalEntities
        self.allowAllEntities = allowAllEntities

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AdditionalAllowedEntitiesConfiguration):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.additionalAllowedEntities, self.allowAdditionalEntities, self.allowAllEntities))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["additionalAllowedEntities", "allowAdditionalEntities", "allowAllEntities"]}

        return cls(**valid_data)
