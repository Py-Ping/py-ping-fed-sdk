from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.idp_ws_trust_attribute_contract import IdpWsTrustAttributeContract
from pingfedsdk.models.sp_token_generator_mapping import SpTokenGeneratorMapping


class IdpWsTrust(Model):
    """Ws-Trust STS provides validation of incoming tokens which enable SSO access to Web Services. It also allows generation of local tokens for Web Services.

    Attributes
    ----------
    attributeContract: IdpWsTrustAttributeContract
        A set of user attributes that the SP receives in the incoming token.

    generateLocalToken: bool
        Indicates whether a local token needs to be generated. The default value is false.

    tokenGeneratorMappings: list
        A list of token generators to generate local tokens. Required if a local token needs to be generated.

    """
    def __init__(self, attributeContract: IdpWsTrustAttributeContract, generateLocalToken: bool, tokenGeneratorMappings: list = None) -> None:
        self.attributeContract = attributeContract
        self.generateLocalToken = generateLocalToken
        self.tokenGeneratorMappings = tokenGeneratorMappings

    def _validate(self) -> bool:
        return any(x for x in ["attributeContract", "generateLocalToken"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, IdpWsTrust):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.attributeContract, self.generateLocalToken, self.tokenGeneratorMappings]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["attributeContract", "generateLocalToken", "tokenGeneratorMappings"] and v is not None:
                if k == "attributeContract":
                    valid_data[k] = IdpWsTrustAttributeContract.from_dict(v)
                if k == "generateLocalToken":
                    valid_data[k] = bool(v)
                if k == "tokenGeneratorMappings":
                    valid_data[k] = [SpTokenGeneratorMapping.from_dict(x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["attributeContract", "generateLocalToken", "tokenGeneratorMappings"]:
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
