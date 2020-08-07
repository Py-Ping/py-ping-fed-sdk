class OIDCRequestParameter():
    """An OIDC custom request parameter.

    Attributes
    ----------
    applicationEndpointOverride : boolean
 Indicates whether the parameter values can be overriden by the Application Endpoint parameters
    name : string
 A List of parameter value. If more than one value is provided, the parameter is treated as a multi-valued parameter.
    value : string
 A List of parameter value. If more than one value is provided, the parameter is treated as a multi-valued parameter.

    """

    def __init__(self, name, value, applicationEndpointOverride) -> None:
        self.applicationEndpointOverride = applicationEndpointOverride
        self.name = name
        self.value = value

    def _validate(self) -> bool:
        return any(x for x in ["name", "value", "applicationEndpointOverride"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, OIDCRequestParameter):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.applicationEndpointOverride, self.name, self.value))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["applicationEndpointOverride", "name", "value"]}

        return cls(**valid_data)