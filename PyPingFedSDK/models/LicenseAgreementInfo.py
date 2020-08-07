class LicenseAgreementInfo():
    """PingFederate License Agreement information.

    Attributes
    ----------
    accepted : boolean
 Indicates whether license agreement has been accepted. The default value is false.
    licenseAgreementUrl : string
 URL to license agreement.

    """

    def __init__(self, accepted=None, licenseAgreementUrl=None) -> None:
        self.accepted = accepted
        self.licenseAgreementUrl = licenseAgreementUrl

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, LicenseAgreementInfo):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.accepted, self.licenseAgreementUrl))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["accepted", "licenseAgreementUrl"]}

        return cls(**valid_data)