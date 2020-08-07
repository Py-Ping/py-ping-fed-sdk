class NotificationPublisherDescriptor():
    """A notification publisher plugin descriptor.

    Attributes
    ----------
    attributeContract : array
 The attribute contract for this plugin.
    className : string
 Full class name of the class that implements this plugin.
    configDescriptor : str
 The descriptor which defines the configuration fields available for this plugin.
    id : string
 Unique ID of the plugin.
    name : string
 Friendly name for the plugin.
    supportsExtendedContract : boolean
 Determines whether this plugin supports extending the attribute contract.

    """

<<<<<<< HEAD
    def __init__(self, attributeContract=None, className=None, configDescriptor=None, var_id=None, name=None, supportsExtendedContract=None) -> None:
        self.attributeContract = attributeContract
        self.className = className
        self.configDescriptor = configDescriptor
        self.var_id = var_id
        self.name = name
        self.supportsExtendedContract = supportsExtendedContract
=======
    def __init__(self, attributeContract=None, className=None, configDescriptor=None, id=None, name=None, supportsExtendedContract=None):
        self.attributeContract: list = attributeContract
        self.className: str = className
        self.configDescriptor: str = configDescriptor
        self.id: str = id
        self.name: str = name
        self.supportsExtendedContract: bool = supportsExtendedContract
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, NotificationPublisherDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.attributeContract, self.className, self.configDescriptor, self.var_id, self.name, self.supportsExtendedContract))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContract", "className", "configDescriptor", "var_id", "name", "supportsExtendedContract"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
