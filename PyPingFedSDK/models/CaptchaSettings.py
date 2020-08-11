class CaptchaSettings():
    """Settings for CAPTCHA.

    Attributes
    ----------
    encryptedSecretKey : string
 The encrypted secret key for reCAPTCHA. If you do not want to update the stored value, this attribute should be passed back unchanged.
    secretKey : string
 Secret key for reCAPTCHA. GETs will not return this attribute. To update this field, specify the new value in this attribute.
    siteKey : string
 Site key for reCAPTCHA.

    """

    def __init__(self, encryptedSecretKey:str=None, secretKey:str=None, siteKey:str=None) -> None:
        self.encryptedSecretKey = encryptedSecretKey
        self.secretKey = secretKey
        self.siteKey = siteKey

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, CaptchaSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.encryptedSecretKey, self.secretKey, self.siteKey))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["encryptedSecretKey", "secretKey", "siteKey"]}

        return cls(**valid_data)