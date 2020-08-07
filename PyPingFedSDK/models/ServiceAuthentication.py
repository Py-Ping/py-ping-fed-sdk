class ServiceAuthentication():
    """Service Authentication Settings.

    Attributes
    ----------
    attributeQuery : str
<<<<<<< HEAD
 SAML2.0 attribute query service. Remove the JSON field to deactivate the attribute query service.
    connectionManagement : str
 Connection management service. Remove the JSON field to deactivate the connection management service.
    jmx : str
 JMX application management and monitoring service. Remove the JSON field to deactivate the JMX service.
    ssoDirectoryService : str
 SSO directory service. Remove the JSON field to deactivate the SSO Directory service.

    """

    def __init__(self, attributeQuery=None, connectionManagement=None, jmx=None, ssoDirectoryService=None) -> None:
        self.attributeQuery = attributeQuery
        self.connectionManagement = connectionManagement
        self.jmx = jmx
        self.ssoDirectoryService = ssoDirectoryService

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
=======
        SAML2.0 attribute query service. Remove the JSON field to deactivate the attribute query service.    connectionManagement : str
        Connection management service. Remove the JSON field to deactivate the connection management service.    jmx : str
        JMX application management and monitoring service. Remove the JSON field to deactivate the JMX service.    ssoDirectoryService : str
        SSO directory service. Remove the JSON field to deactivate the SSO Directory service.
    """

    __slots__ = ["attributeQuery", "connectionManagement", "jmx", "ssoDirectoryService"]

    def __init__(self, attributeQuery=None, connectionManagement=None, jmx=None, ssoDirectoryService=None):
        self.attributeQuery: str = attributeQuery
        self.connectionManagement: str = connectionManagement
        self.jmx: str = jmx
        self.ssoDirectoryService: str = ssoDirectoryService

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
>>>>>>> Baseline Sphinx generation
        if isinstance(other, ServiceAuthentication):
            return self.__dict__ == other.__dict__
        return NotImplemented

<<<<<<< HEAD
    def __hash__(self) -> int:
        return hash((self.attributeQuery, self.connectionManagement, self.jmx, self.ssoDirectoryService))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeQuery", "connectionManagement", "jmx", "ssoDirectoryService"]}

        return cls(**valid_data)
=======
    def __hash__(self):
        return hash((self.attributeQuery, self.connectionManagement, self.jmx, self.ssoDirectoryService))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeQuery", "connectionManagement", "jmx", "ssoDirectoryService"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
