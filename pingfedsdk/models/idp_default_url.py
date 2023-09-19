from enum import Enum

from pingfedsdk.model import Model


class IdpDefaultUrl(Model):
    """IDP Default URL settings.

    Attributes
    ----------
    confirmIdpSlo: bool
        Prompt user to confirm Single Logout (SLO).

    idpSloSuccessUrl: str
        Provide the default URL you would like to send the user to when Single Logout has succeeded.

    idpErrorMsg: str
        Provide the error text displayed in a user's browser when an SSO operation fails.

    """
    def __init__(self, idpErrorMsg: str, confirmIdpSlo: bool = None, idpSloSuccessUrl: str = None) -> None:
        self.confirmIdpSlo = confirmIdpSlo
        self.idpSloSuccessUrl = idpSloSuccessUrl
        self.idpErrorMsg = idpErrorMsg

    def _validate(self) -> bool:
        return any(x for x in ["idpErrorMsg"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpDefaultUrl):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.confirmIdpSlo, self.idpSloSuccessUrl, self.idpErrorMsg]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["confirmIdpSlo", "idpSloSuccessUrl", "idpErrorMsg"] and v is not None:
                if k == "confirmIdpSlo":
                    valid_data[k] = bool(v)
                if k == "idpSloSuccessUrl":
                    valid_data[k] = str(v)
                if k == "idpErrorMsg":
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
            if k in ["confirmIdpSlo", "idpSloSuccessUrl", "idpErrorMsg"]:
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
