class SaasPluginDescriptor():
    """A SaaS Plugin.

    Attributes
    ----------
    configDescriptor : str
 The plugin configuration that includes information to access the target service provider.
    description : string
 The SaaS plugin description.
    id : string
 The SaaS plugin type.
    saasPluginFieldInfoDescriptors : array
 The SaaS plugin attribute list for mapping from the local data store into Fields specified by the service provide.

    """

    def __init__(self, configDescriptor=None, description=None, var_id=None, saasPluginFieldInfoDescriptors=None) -> None:
        self.configDescriptor = configDescriptor
        self.description = description
        self.var_id = var_id
        self.saasPluginFieldInfoDescriptors = saasPluginFieldInfoDescriptors

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, SaasPluginDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.configDescriptor, self.description, self.var_id, self.saasPluginFieldInfoDescriptors))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["configDescriptor", "description", "var_id", "saasPluginFieldInfoDescriptors"]}

        return cls(**valid_data)