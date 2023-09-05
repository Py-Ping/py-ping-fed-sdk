from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.channel import Channel
from pingfedsdk.models.schema import Schema
from pingfedsdk.models.config_field import ConfigField


class OutboundProvision(Model):
    """Outbound Provisioning allows an IdP to create and maintain user accounts at standards-based partner sites using SCIM as well as select-proprietary provisioning partner sites that are protocol-enabled.

    Attributes
    ----------
    type: str
        The SaaS plugin type.

    targetSettings: list
        Configuration fields that includes credentials to target SaaS application.

    customSchema: Schema
        Custom SCIM attribute configuration.

    channels: list
        Includes settings of a source data store, managing provisioning threads and mapping of attributes.

    """

    def __init__(self, channels: list, targetSettings: list, type: str, customSchema: Schema = None) -> None:
        self.type = type
        self.targetSettings = targetSettings
        self.customSchema = customSchema
        self.channels = channels

    def _validate(self) -> bool:
        return any(x for x in ["channels", "targetSettings", "type"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, OutboundProvision):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.type, self.targetSettings, self.customSchema, self.channels]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["type", "targetSettings", "customSchema", "channels"] and v is not None:
                if k == "type":
                    valid_data[k] = str(v)
                if k == "targetSettings":
                    valid_data[k] = [ConfigField(**x) for x in v]
                if k == "customSchema":
                    valid_data[k] = Schema(**v)
                if k == "channels":
                    valid_data[k] = [Channel(**x) for x in v]

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["type", "targetSettings", "customSchema", "channels"]:
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
