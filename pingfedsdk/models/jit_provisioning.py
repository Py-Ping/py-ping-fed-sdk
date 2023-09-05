from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.jit_provisioning_user_attributes import JitProvisioningUserAttributes
from pingfedsdk.models.data_store_repository import DataStoreRepository
from pingfedsdk.enums import EventTrigger
from pingfedsdk.enums import ErrorHandling


class JitProvisioning(Model):
    """The settings used to specify how and when to provision user accounts.

    Attributes
    ----------
    userAttributes: JitProvisioningUserAttributes
        Attributes from the SAML Assertion.

    userRepository: DataStoreRepository
        The data store used as the local repository for user provisioning.

    eventTrigger: EventTrigger
        Specify when provisioning occurs during assertion processing. The default is 'NEW_USER_ONLY'.

    errorHandling: ErrorHandling
        Specify behavior when provisioning request fails. The default is 'CONTINUE_SSO'.

    """

    def __init__(self, userAttributes: JitProvisioningUserAttributes, userRepository: DataStoreRepository, eventTrigger: EventTrigger = None, errorHandling: ErrorHandling = None) -> None:
        self.userAttributes = userAttributes
        self.userRepository = userRepository
        self.eventTrigger = eventTrigger
        self.errorHandling = errorHandling

    def _validate(self) -> bool:
        return any(x for x in ["userAttributes", "userRepository"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, JitProvisioning):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.userAttributes, self.userRepository, self.eventTrigger, self.errorHandling]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["userAttributes", "userRepository", "eventTrigger", "errorHandling"] and v is not None:
                if k == "userAttributes":
                    valid_data[k] = JitProvisioningUserAttributes(**v)
                if k == "userRepository":
                    valid_data[k] = DataStoreRepository(**v)
                if k == "eventTrigger":
                    valid_data[k] = EventTrigger[v]
                if k == "errorHandling":
                    valid_data[k] = ErrorHandling[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["userAttributes", "userRepository", "eventTrigger", "errorHandling"]:
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
