from enum import Enum

from pingfedsdk.model import Model


class IdpAttributeQueryPolicy(Model):
    """The attribute query profile's security policy.

    Attributes
    ----------
    requireSignedResponse: bool
        Require signed response.

    requireSignedAssertion: bool
        Require signed assertion.

    requireEncryptedAssertion: bool
        Require encrypted assertion.

    signAttributeQuery: bool
        Sign the attribute query.

    encryptNameId: bool
        Encrypt the name identifier.

    maskAttributeValues: bool
        Mask attributes in log files.

    """
    def __init__(self, requireSignedResponse: bool = None, requireSignedAssertion: bool = None, requireEncryptedAssertion: bool = None, signAttributeQuery: bool = None, encryptNameId: bool = None, maskAttributeValues: bool = None) -> None:
        self.requireSignedResponse = requireSignedResponse
        self.requireSignedAssertion = requireSignedAssertion
        self.requireEncryptedAssertion = requireEncryptedAssertion
        self.signAttributeQuery = signAttributeQuery
        self.encryptNameId = encryptNameId
        self.maskAttributeValues = maskAttributeValues

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpAttributeQueryPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.requireSignedResponse, self.requireSignedAssertion, self.requireEncryptedAssertion, self.signAttributeQuery, self.encryptNameId, self.maskAttributeValues]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["requireSignedResponse", "requireSignedAssertion", "requireEncryptedAssertion", "signAttributeQuery", "encryptNameId", "maskAttributeValues"] and v is not None:
                if k == "requireSignedResponse":
                    valid_data[k] = bool(v)
                if k == "requireSignedAssertion":
                    valid_data[k] = bool(v)
                if k == "requireEncryptedAssertion":
                    valid_data[k] = bool(v)
                if k == "signAttributeQuery":
                    valid_data[k] = bool(v)
                if k == "encryptNameId":
                    valid_data[k] = bool(v)
                if k == "maskAttributeValues":
                    valid_data[k] = bool(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["requireSignedResponse", "requireSignedAssertion", "requireEncryptedAssertion", "signAttributeQuery", "encryptNameId", "maskAttributeValues"]:
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
