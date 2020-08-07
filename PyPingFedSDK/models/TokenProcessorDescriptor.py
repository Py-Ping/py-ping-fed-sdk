class TokenProcessorDescriptor():
    """A token processor descriptor.

    Attributes
    ----------
    attributeContract : array
        The attribute contract for this plugin.    className : string
        Full class name of the class that implements this plugin.    configDescriptor : str
        The descriptor which defines the configuration fields available for this plugin.    id : string
        Unique ID of the plugin.    name : string
        Friendly name for the plugin.    supportsExtendedContract : boolean
        Determines whether this plugin supports extending the attribute contract.
    """

    __slots__ = ["attributeContract", "className", "configDescriptor", "id", "name", "supportsExtendedContract"]

    def __init__(self, attributeContract=None, className=None, configDescriptor=None, id=None, name=None, supportsExtendedContract=None):
        self.attributeContract: list = attributeContract
        self.className: str = className
        self.configDescriptor: str = configDescriptor
        self.id: str = id
        self.name: str = name
        self.supportsExtendedContract: bool = supportsExtendedContract

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, TokenProcessorDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.attributeContract, self.className, self.configDescriptor, self.id, self.name, self.supportsExtendedContract))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContract", "className", "configDescriptor", "id", "name", "supportsExtendedContract"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__