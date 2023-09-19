from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.access_token_attribute_contract import AccessTokenAttributeContract
from pingfedsdk.models.atm_access_control_settings import AtmAccessControlSettings
from pingfedsdk.models.atm_selection_settings import AtmSelectionSettings
from pingfedsdk.models.plugin_configuration import PluginConfiguration
from pingfedsdk.models.resource_link import ResourceLink
from pingfedsdk.models.session_validation_settings import SessionValidationSettings


class AccessTokenManager(Model):
    """An OAuth access token management plugin instance.

    Attributes
    ----------
    id: str
        The ID of the plugin instance. The ID cannot be modified once the instance is created.
        Note: Ignored when specifying a connection's adapter override.

    name: str
        The plugin instance name. The name cannot be modified once the instance is created.
        Note: Ignored when specifying a connection's adapter override.

    pluginDescriptorRef: ResourceLink
        Reference to the plugin descriptor for this instance. The plugin descriptor cannot be modified once the instance is created.
        Note: Ignored when specifying a connection's adapter override.

    parentRef: ResourceLink
        The reference to this plugin's parent instance. The parent reference is only accepted if the plugin type supports parent instances.
        Note: This parent reference is required if this plugin instance is used as an overriding plugin (e.g. connection adapter overrides)

    configuration: PluginConfiguration
        Plugin instance configuration.

    attributeContract: AccessTokenAttributeContract
        The list of attributes that will be added to an access token.

    selectionSettings: AtmSelectionSettings
        Settings which determine how this token manager can be selected for use by an OAuth request.

    accessControlSettings: AtmAccessControlSettings
        Settings which determine which clients may access this token manager.

    sessionValidationSettings: SessionValidationSettings
        Settings which determine how the user session is associated with the access token.

    sequenceNumber: int
        Number added to an access token to identify which Access Token Manager issued the token.

    """
    def __init__(self, id: str, name: str, pluginDescriptorRef: ResourceLink, configuration: PluginConfiguration, parentRef: ResourceLink = None, attributeContract: AccessTokenAttributeContract = None, selectionSettings: AtmSelectionSettings = None, accessControlSettings: AtmAccessControlSettings = None, sessionValidationSettings: SessionValidationSettings = None, sequenceNumber: int = None) -> None:
        self.id = id
        self.name = name
        self.pluginDescriptorRef = pluginDescriptorRef
        self.parentRef = parentRef
        self.configuration = configuration
        self.attributeContract = attributeContract
        self.selectionSettings = selectionSettings
        self.accessControlSettings = accessControlSettings
        self.sessionValidationSettings = sessionValidationSettings
        self.sequenceNumber = sequenceNumber

    def _validate(self) -> bool:
        return any(x for x in ["configuration", "id", "name", "pluginDescriptorRef"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, AccessTokenManager):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.pluginDescriptorRef, self.parentRef, self.configuration, self.attributeContract, self.selectionSettings, self.accessControlSettings, self.sessionValidationSettings, self.sequenceNumber]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "pluginDescriptorRef", "parentRef", "configuration", "attributeContract", "selectionSettings", "accessControlSettings", "sessionValidationSettings", "sequenceNumber"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "pluginDescriptorRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "parentRef":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "configuration":
                    valid_data[k] = PluginConfiguration.from_dict(v)
                if k == "attributeContract":
                    valid_data[k] = AccessTokenAttributeContract.from_dict(v)
                if k == "selectionSettings":
                    valid_data[k] = AtmSelectionSettings.from_dict(v)
                if k == "accessControlSettings":
                    valid_data[k] = AtmAccessControlSettings.from_dict(v)
                if k == "sessionValidationSettings":
                    valid_data[k] = SessionValidationSettings.from_dict(v)
                if k == "sequenceNumber":
                    valid_data[k] = int(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "name", "pluginDescriptorRef", "parentRef", "configuration", "attributeContract", "selectionSettings", "accessControlSettings", "sessionValidationSettings", "sequenceNumber"]:
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
