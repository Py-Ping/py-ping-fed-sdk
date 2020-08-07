class RedirectValidationPartnerSettings():
    """Settings for redirection at a partner site.

    Attributes
    ----------
    enableWreplyValidationSLO : boolean
        Enable wreply validation for SLO.
    """

    __slots__ = ["enableWreplyValidationSLO"]

    def __init__(self, enableWreplyValidationSLO=None):
        self.enableWreplyValidationSLO: bool = enableWreplyValidationSLO

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, RedirectValidationPartnerSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.enableWreplyValidationSLO))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["enableWreplyValidationSLO"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__