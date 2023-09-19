from enum import Enum

from pingfedsdk.enums import ExecuteWorkflow
from pingfedsdk.model import Model
from pingfedsdk.models.resource_link import ResourceLink


class RegistrationConfig(Model):
    """A local identity profile registration configuration.

    Attributes
    ----------
    captchaEnabled: bool
        Whether CAPTCHA is enabled or not in the registration configuration.

    templateName: str
        The template name for the registration configuration.

    createAuthnSessionAfterRegistration: bool
        Whether to create an Authentication Session when registering a local account. Default is true.

    usernameField: str
        When creating an Authentication Session after registering a local account, PingFederate will pass the Unique ID field's value as the username. If the Unique ID value is not the username, then override which field's value will be used as the username.

    thisIsMyDeviceEnabled: bool
        Allows users to indicate whether their device is shared or private. In this mode, PingFederate Authentication Sessions will not be stored unless the user indicates the device is private.

    registrationWorkflow: ResourceLink
        The policy fragment to be executed as part of the registration workflow.

    executeWorkflow: ExecuteWorkflow
        This setting indicates whether PingFederate should execute the workflow before or after account creation. The default is to run the registration workflow after account creation.

    """
    def __init__(self, templateName: str, captchaEnabled: bool = None, createAuthnSessionAfterRegistration: bool = None, usernameField: str = None, thisIsMyDeviceEnabled: bool = None, registrationWorkflow: ResourceLink = None, executeWorkflow: ExecuteWorkflow = None) -> None:
        self.captchaEnabled = captchaEnabled
        self.templateName = templateName
        self.createAuthnSessionAfterRegistration = createAuthnSessionAfterRegistration
        self.usernameField = usernameField
        self.thisIsMyDeviceEnabled = thisIsMyDeviceEnabled
        self.registrationWorkflow = registrationWorkflow
        self.executeWorkflow = executeWorkflow

    def _validate(self) -> bool:
        return any(x for x in ["templateName"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, RegistrationConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.captchaEnabled, self.templateName, self.createAuthnSessionAfterRegistration, self.usernameField, self.thisIsMyDeviceEnabled, self.registrationWorkflow, self.executeWorkflow]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["captchaEnabled", "templateName", "createAuthnSessionAfterRegistration", "usernameField", "thisIsMyDeviceEnabled", "registrationWorkflow", "executeWorkflow"] and v is not None:
                if k == "captchaEnabled":
                    valid_data[k] = bool(v)
                if k == "templateName":
                    valid_data[k] = str(v)
                if k == "createAuthnSessionAfterRegistration":
                    valid_data[k] = bool(v)
                if k == "usernameField":
                    valid_data[k] = str(v)
                if k == "thisIsMyDeviceEnabled":
                    valid_data[k] = bool(v)
                if k == "registrationWorkflow":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "executeWorkflow":
                    valid_data[k] = ExecuteWorkflow[v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["captchaEnabled", "templateName", "createAuthnSessionAfterRegistration", "usernameField", "thisIsMyDeviceEnabled", "registrationWorkflow", "executeWorkflow"]:
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
