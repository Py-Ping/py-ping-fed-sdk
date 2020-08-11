class RedirectValidationLocalSettings():
    """Settings for local redirect validation.

    Attributes
    ----------
    enableInErrorResourceValidation : boolean
        Enable validation for error resource.
    enableTargetResourceValidationForIdpDiscovery : boolean
        Enable target resource validation for IdP discovery.
    enableTargetResourceValidationForSLO : boolean
        Enable target resource validation for SLO.
    enableTargetResourceValidationForSSO : boolean
        Enable target resource validation for SSO.
    whiteList : array
        List of URLs that are designated as valid target resources.

    """

    def __init__(self, enableInErrorResourceValidation:bool=None, enableTargetResourceValidationForIdpDiscovery:bool=None, enableTargetResourceValidationForSLO:bool=None, enableTargetResourceValidationForSSO:bool=None, whiteList:list=None) -> None:
        self.enableInErrorResourceValidation = enableInErrorResourceValidation
        self.enableTargetResourceValidationForIdpDiscovery = enableTargetResourceValidationForIdpDiscovery
        self.enableTargetResourceValidationForSLO = enableTargetResourceValidationForSLO
        self.enableTargetResourceValidationForSSO = enableTargetResourceValidationForSSO
        self.whiteList = whiteList

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, RedirectValidationLocalSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.enableInErrorResourceValidation, self.enableTargetResourceValidationForIdpDiscovery, self.enableTargetResourceValidationForSLO, self.enableTargetResourceValidationForSSO, self.whiteList]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["enableInErrorResourceValidation", "enableTargetResourceValidationForIdpDiscovery", "enableTargetResourceValidationForSLO", "enableTargetResourceValidationForSSO", "whiteList"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__