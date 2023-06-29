from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.attribute_rules import AttributeRules
from pingfedsdk.models.attribute_fulfillment_value import AttributeFulfillmentValue
from pingfedsdk.models.authentication_source import AuthenticationSource
from pingfedsdk.enums import AuthenticationPolicySelectionActionType


class AuthnSourcePolicyAction(Model):
    """An authentication source selection action.

    Attributes
    ----------
    type: AuthenticationPolicySelectionActionType
        The authentication selection type.

    context: str
        The result context.

    attributeRules: AttributeRules
        The authentication policy rules.

    authenticationSource: AuthenticationSource
        The associated authentication source.

    inputUserIdMapping: AttributeFulfillmentValue
        The input user ID mapping.

    userIdAuthenticated: bool
        Indicates whether the user ID obtained by the user ID mapping is authenticated.

    """

    def __init__(self, authenticationSource: AuthenticationSource, type: AuthenticationPolicySelectionActionType = None, context: str = None, attributeRules: AttributeRules = None, inputUserIdMapping: AttributeFulfillmentValue = None, userIdAuthenticated: bool = None) -> None:
        self.type = type
        self.context = context
        self.attributeRules = attributeRules
        self.authenticationSource = authenticationSource
        self.inputUserIdMapping = inputUserIdMapping
        self.userIdAuthenticated = userIdAuthenticated

    def _validate(self) -> bool:
        return any(x for x in ["authenticationSource"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AuthnSourcePolicyAction):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.context, self.attributeRules, self.authenticationSource, self.inputUserIdMapping, self.userIdAuthenticated]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "context", "attributeRules", "authenticationSource", "inputUserIdMapping", "userIdAuthenticated"] and v is not None:
                if k == "type":
                    valid_data[k] = AuthenticationPolicySelectionActionType[v]
                if k == "context":
                    valid_data[k] = str(v)
                if k == "attributeRules":
                    valid_data[k] = AttributeRules(**v)
                if k == "authenticationSource":
                    valid_data[k] = AuthenticationSource(**v)
                if k == "inputUserIdMapping":
                    valid_data[k] = AttributeFulfillmentValue(**v)
                if k == "userIdAuthenticated":
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
            if k in ["type", "context", "attributeRules", "authenticationSource", "inputUserIdMapping", "userIdAuthenticated"]:
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
