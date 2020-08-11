class OutboundProvision():
    """Outbound Provisioning allows an IdP to create and maintain user accounts at standards-based partner sites using SCIM as well as select-proprietary provisioning partner sites that are protocol-enabled.

    Attributes
    ----------
    channels : array
        Includes settings of a source data store, managing provisioning threads and mapping of attributes.
    customSchema : str
        Custom SCIM attribute configuration.
    targetSettings : array
        Configuration fields that includes credentials to target SaaS application.
    type : string
        The SaaS plugin type.

    """

    def __init__(self, var_type:str, targetSettings:list, channels:list, customSchema=None) -> None:
        self.channels = channels
        self.customSchema = customSchema
        self.targetSettings = targetSettings
        self.var_type = var_type

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "targetSettings", "channels"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, OutboundProvision):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.channels, self.customSchema, self.targetSettings, self.var_type]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["channels", "customSchema", "targetSettings", "var_type"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__