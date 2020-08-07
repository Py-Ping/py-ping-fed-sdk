class OIDCRequestParameter():
    """An OIDC custom request parameter.

    Attributes
    ----------
    applicationEndpointOverride : boolean
        Indicates whether the parameter values can be overriden by the Application Endpoint parameters    name : string
        A List of parameter value. If more than one value is provided, the parameter is treated as a multi-valued parameter.    value : string
        A List of parameter value. If more than one value is provided, the parameter is treated as a multi-valued parameter.
    """

    __slots__ = ["applicationEndpointOverride", "name", "value"]

    def __init__(self, name, value, applicationEndpointOverride):
        self.applicationEndpointOverride: bool = applicationEndpointOverride
        self.name: str = name
        self.value: str = value

    def _validate(self):
        return any(x for x in ['name', 'value', 'applicationEndpointOverride'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, OIDCRequestParameter):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.applicationEndpointOverride, self.name, self.value))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["applicationEndpointOverride", "name", "value"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__