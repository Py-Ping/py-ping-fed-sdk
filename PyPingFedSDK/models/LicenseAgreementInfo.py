class LicenseAgreementInfo():
    """PingFederate License Agreement information.

    Attributes
    ----------
    accepted : boolean
        Indicates whether license agreement has been accepted. The default value is false.    licenseAgreementUrl : string
        URL to license agreement.
    """

    __slots__ = ["accepted", "licenseAgreementUrl"]

    def __init__(self, accepted=None, licenseAgreementUrl=None):
        self.accepted: bool = accepted
        self.licenseAgreementUrl: str = licenseAgreementUrl

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, LicenseAgreementInfo):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.accepted, self.licenseAgreementUrl))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["accepted", "licenseAgreementUrl"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__