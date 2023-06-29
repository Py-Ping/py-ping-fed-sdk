from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.access_token_attribute import AccessTokenAttribute


class AccessTokenAttributeContract(Model):
    """A set of attributes exposed by an Access Token Manager.

    Attributes
    ----------
    coreAttributes: list
        A list of core token attributes that are associated with the access token management plugin type. This field is read-only and is ignored on POST/PUT.

    extendedAttributes: list
        A list of additional token attributes that are associated with this access token management plugin instance.

    inherited: bool
        Whether this attribute contract is inherited from its parent instance. If true, the rest of the properties in this model become read-only. The default value is false.

    defaultSubjectAttribute: str
        Default subject attribute to use for audit logging when validating the access token. Blank value means to use USER_KEY attribute value after grant lookup.

    """

    def __init__(self, coreAttributes: list = None, extendedAttributes: list = None, inherited: bool = None, defaultSubjectAttribute: str = None) -> None:
        self.coreAttributes = coreAttributes
        self.extendedAttributes = extendedAttributes
        self.inherited = inherited
        self.defaultSubjectAttribute = defaultSubjectAttribute

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AccessTokenAttributeContract):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.coreAttributes, self.extendedAttributes, self.inherited, self.defaultSubjectAttribute]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["coreAttributes", "extendedAttributes", "inherited", "defaultSubjectAttribute"] and v is not None:
                if k == "coreAttributes":
                    valid_data[k] = [AccessTokenAttribute(**x) for x in v]
                if k == "extendedAttributes":
                    valid_data[k] = [AccessTokenAttribute(**x) for x in v]
                if k == "inherited":
                    valid_data[k] = bool(v)
                if k == "defaultSubjectAttribute":
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
            if k in ["coreAttributes", "extendedAttributes", "inherited", "defaultSubjectAttribute"]:
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
