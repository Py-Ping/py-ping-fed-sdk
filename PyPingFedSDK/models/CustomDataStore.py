class CustomDataStore():
    """ A custom data store.

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

    __slots__ = ["configuration", "id", "maskAttributeValues", "name", "parentRef", "pluginDescriptorRef", "type"]
    def __init__(self, type, name, pluginDescriptorRef, configuration, id=None, maskAttributeValues=None, parentRef=None):
            self.configuration = configuration
            self.id = id
            self.maskAttributeValues = maskAttributeValues
            self.name = name
            self.parentRef = parentRef
            self.pluginDescriptorRef = pluginDescriptorRef
            self.type = type
    
    def _validate(self):
        return any(x for x in ['type', 'name', 'pluginDescriptorRef', 'configuration'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, CustomDataStore):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((configuration, id, maskAttributeValues, name, parentRef, pluginDescriptorRef, type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
