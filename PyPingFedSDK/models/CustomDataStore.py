class CustomDataStore():
    """A custom data store.

    Attributes
    ----------
    configuration : str
 Plugin instance configuration.
    id : string
 The persistent, unique ID for the data store. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.
    maskAttributeValues : boolean
 Whether attribute values should be masked in the log.
    name : string
 The plugin instance name.
    parentRef : str
 The reference to this plugin's parent instance. The parent reference is only accepted if the plugin type supports parent instances.<br>Note: This parent reference is required if this plugin instance is used as an overriding plugin (e.g. connection adapter overrides)
    pluginDescriptorRef : str
 Reference to the plugin descriptor for this instance. The plugin descriptor cannot be modified once the instance is created.<br>Note: Ignored when specifying a connection's adapter override.
    type : str
 The data store type.

    """

    def __init__(self, var_type, name, pluginDescriptorRef, configuration, var_id=None, maskAttributeValues=None, parentRef=None) -> None:
        self.configuration = configuration
        self.var_id = var_id
        self.maskAttributeValues = maskAttributeValues
        self.name = name
        self.parentRef = parentRef
        self.pluginDescriptorRef = pluginDescriptorRef
        self.var_type = var_type

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "name", "pluginDescriptorRef", "configuration"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, CustomDataStore):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.configuration, self.var_id, self.maskAttributeValues, self.name, self.parentRef, self.pluginDescriptorRef, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["configuration", "var_id", "maskAttributeValues", "name", "parentRef", "pluginDescriptorRef", "var_type"]}

        return cls(**valid_data)