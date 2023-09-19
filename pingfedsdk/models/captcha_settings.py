from enum import Enum

from pingfedsdk.model import Model


class CaptchaSettings(Model):
    """Settings for CAPTCHA.

    Attributes
    ----------
    siteKey: str
        Site key for reCAPTCHA.

    secretKey: str
        Secret key for reCAPTCHA. GETs will not return this attribute. To update this field, specify the new value in this attribute.

    encryptedSecretKey: str
        The encrypted secret key for reCAPTCHA. If you do not want to update the stored value, this attribute should be passed back unchanged.

    """
    def __init__(self, siteKey: str = None, secretKey: str = None, encryptedSecretKey: str = None) -> None:
        self.siteKey = siteKey
        self.secretKey = secretKey
        self.encryptedSecretKey = encryptedSecretKey

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, CaptchaSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.siteKey, self.secretKey, self.encryptedSecretKey]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["siteKey", "secretKey", "encryptedSecretKey"] and v is not None:
                if k == "siteKey":
                    valid_data[k] = str(v)
                if k == "secretKey":
                    valid_data[k] = str(v)
                if k == "encryptedSecretKey":
                    valid_data[k] = str(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["siteKey", "secretKey", "encryptedSecretKey"]:
                if isinstance(v, Model):
                    body[k] = v.to_dict(remove_nonetypes)
                elif isinstance(v, list):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, dict):
                    vals = {}
                    for x, y in v.items():
                        if isinstance(y, Model):
                            vals[x] = y.to_dict(remove_nonetypes)
                        elif not remove_nonetypes or (remove_nonetypes and y is not None):
                            vals[x] = y
                    body[k] = vals
                elif isinstance(v, set):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, Enum):
                    body[k] = str(v).split('.')[-1]
                elif not remove_nonetypes or (remove_nonetypes and v is not None):
                    body[k] = v
        return body
