from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.access_token_manager_mapping import AccessTokenManagerMapping
from pingfedsdk.models.idp_o_auth_attribute_contract import IdpOAuthAttributeContract


class IdpOAuthGrantAttributeMapping(Model):
    """The OAuth Assertion Grant settings used to map from your IdP.

    Attributes
    ----------
    accessTokenManagerMappings: list
        A mapping in a connection that defines how access tokens are created.

    idpOAuthAttributeContract: IdpOAuthAttributeContract
        A set of user attributes that the IdP sends in the OAuth Assertion Grant.

    """

    def __init__(self, accessTokenManagerMappings: list = None, idpOAuthAttributeContract: IdpOAuthAttributeContract = None) -> None:
        self.accessTokenManagerMappings = accessTokenManagerMappings
        self.idpOAuthAttributeContract = idpOAuthAttributeContract

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpOAuthGrantAttributeMapping):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.accessTokenManagerMappings, self.idpOAuthAttributeContract]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["accessTokenManagerMappings", "idpOAuthAttributeContract"] and v is not None:
                if k == "accessTokenManagerMappings":
                    valid_data[k] = [AccessTokenManagerMapping(**x) for x in v]
                if k == "idpOAuthAttributeContract":
                    valid_data[k] = IdpOAuthAttributeContract(**v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["accessTokenManagerMappings", "idpOAuthAttributeContract"]:
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
