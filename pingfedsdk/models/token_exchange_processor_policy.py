from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.token_exchange_processor_attribute_contract import TokenExchangeProcessorAttributeContract
from pingfedsdk.models.token_exchange_processor_mapping import TokenExchangeProcessorMapping


class TokenExchangeProcessorPolicy(Model):
    """The set of attributes used to configure a OAuth 2.0 Token Exchange processor policy.

    Attributes
    ----------
    id: str
        The Token Exchange processor policy ID. ID is unique.

    name: str
        The Token Exchange processor policy name. Name is unique.

    actorTokenRequired: bool
        Require an Actor token on a OAuth 2.0 Token Exchange request.

    attributeContract: TokenExchangeProcessorAttributeContract
        A set of attributes exposed by an OAuth 2.0 Token Exchange Processor policy.

    processorMappings: list
        A list of Token Processor(s) mappings into an OAuth 2.0 Token Exchange Processor policy.

    """

    def __init__(self, attributeContract: TokenExchangeProcessorAttributeContract, id: str, name: str, processorMappings: list, actorTokenRequired: bool = None) -> None:
        self.id = id
        self.name = name
        self.actorTokenRequired = actorTokenRequired
        self.attributeContract = attributeContract
        self.processorMappings = processorMappings

    def _validate(self) -> bool:
        return any(x for x in ["attributeContract", "id", "name", "processorMappings"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, TokenExchangeProcessorPolicy):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.actorTokenRequired, self.attributeContract, self.processorMappings]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "actorTokenRequired", "attributeContract", "processorMappings"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "actorTokenRequired":
                    valid_data[k] = bool(v)
                if k == "attributeContract":
                    valid_data[k] = TokenExchangeProcessorAttributeContract(**v)
                if k == "processorMappings":
                    valid_data[k] = [TokenExchangeProcessorMapping(**x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "name", "actorTokenRequired", "attributeContract", "processorMappings"]:
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
