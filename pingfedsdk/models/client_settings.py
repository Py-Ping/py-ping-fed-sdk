from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.client_metadata import ClientMetadata
from pingfedsdk.models.dynamic_client_registration import DynamicClientRegistration


class ClientSettings(Model):
    """The client settings.

    Attributes
    ----------
    clientMetadata: list
        The client metadata.

    dynamicClientRegistration: DynamicClientRegistration
        Dynamic client registration settings.

    """
    def __init__(self, clientMetadata: list = None, dynamicClientRegistration: DynamicClientRegistration = None) -> None:
        self.clientMetadata = clientMetadata
        self.dynamicClientRegistration = dynamicClientRegistration

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, ClientSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.clientMetadata, self.dynamicClientRegistration]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["clientMetadata", "dynamicClientRegistration"] and v is not None:
                if k == "clientMetadata":
                    valid_data[k] = [ClientMetadata.from_dict(x) for x in v]
                if k == "dynamicClientRegistration":
                    valid_data[k] = DynamicClientRegistration.from_dict(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["clientMetadata", "dynamicClientRegistration"]:
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
