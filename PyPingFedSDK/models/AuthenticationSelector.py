class AuthenticationSelector():
    """ An Authentication Selector instance.

    Attributes
    ----------
    attributeContract : str
        The list of attributes that the Authentication Selector provides.
    configuration : str
        Plugin instance configuration.
    id : string
        The ID of the plugin instance. The ID cannot be modified once the instance is created.<br>Note: Ignored when specifying a connection's adapter override.
    name : string
        The plugin instance name. The name cannot be modified once the instance is created.<br>Note: Ignored when specifying a connection's adapter override.
    pluginDescriptorRef : str
        Reference to the plugin descriptor for this instance. The plugin descriptor cannot be modified once the instance is created.<br>Note: Ignored when specifying a connection's adapter override.

    """

    __slots__ = ["attributeContract", "configuration", "id", "name", "pluginDescriptorRef"]
    def __init__(self, id, name, pluginDescriptorRef, configuration, attributeContract=None):
            self.attributeContract = attributeContract
            self.configuration = configuration
            self.id = id
            self.name = name
            self.pluginDescriptorRef = pluginDescriptorRef
    
    def _validate(self):
        return any(x for x in ['id', 'name', 'pluginDescriptorRef', 'configuration'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, AuthenticationSelector):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((attributeContract, configuration, id, name, pluginDescriptorRef))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
