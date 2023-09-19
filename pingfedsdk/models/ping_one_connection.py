from enum import Enum

from pingfedsdk.model import Model


class PingOneConnection(Model):
    """PingOne connection.

    Attributes
    ----------
    id: str
        The persistent, unique ID of the connection. This property is system-assigned if not specified.

    name: str
        The name of the PingOne connection.

    description: str
        A description for the PingOne connection.

    active: bool
        Whether or not this connection is active. Defaults to true.

    credential: str
        The credential for the PingOne connection. To update the credential, specify the plaintext value of the credential in this field. This field will not be populated for GET requests.

    encryptedCredential: str
        The encrypted credential for the PingOne connection. For POST and PUT requests, if you wish to keep the existing credential, this field should be passed back unchanged.

    credentialId: str
        The ID of the PingOne credential. This field is read only.

    pingOneConnectionId: str
        The ID of the PingOne connection. This field is read only.

    environmentId: str
        The ID of the environment of the PingOne credential. This field is read only.

    creationDate: str
        The creation date of the PingOne connection. This field is read only.

    organizationName: str
        The name of the organization associated with this PingOne connection. This field is read only.

    region: str
        The region of the PingOne connection. This field is read only.

    pingOneManagementApiEndpoint: str
        The PingOne management API endpoint. This field is read only.

    pingOneAuthenticationApiEndpoint: str
        The PingOne authentication API endpoint. This field is read only.

    """
    def __init__(self, name: str, id: str = None, description: str = None, active: bool = None, credential: str = None, encryptedCredential: str = None, credentialId: str = None, pingOneConnectionId: str = None, environmentId: str = None, creationDate: str = None, organizationName: str = None, region: str = None, pingOneManagementApiEndpoint: str = None, pingOneAuthenticationApiEndpoint: str = None) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.active = active
        self.credential = credential
        self.encryptedCredential = encryptedCredential
        self.credentialId = credentialId
        self.pingOneConnectionId = pingOneConnectionId
        self.environmentId = environmentId
        self.creationDate = creationDate
        self.organizationName = organizationName
        self.region = region
        self.pingOneManagementApiEndpoint = pingOneManagementApiEndpoint
        self.pingOneAuthenticationApiEndpoint = pingOneAuthenticationApiEndpoint

    def _validate(self) -> bool:
        return any(x for x in ["name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, PingOneConnection):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.description, self.active, self.credential, self.encryptedCredential, self.credentialId, self.pingOneConnectionId, self.environmentId, self.creationDate, self.organizationName, self.region, self.pingOneManagementApiEndpoint, self.pingOneAuthenticationApiEndpoint]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "description", "active", "credential", "encryptedCredential", "credentialId", "pingOneConnectionId", "environmentId", "creationDate", "organizationName", "region", "pingOneManagementApiEndpoint", "pingOneAuthenticationApiEndpoint"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "description":
                    valid_data[k] = str(v)
                if k == "active":
                    valid_data[k] = bool(v)
                if k == "credential":
                    valid_data[k] = str(v)
                if k == "encryptedCredential":
                    valid_data[k] = str(v)
                if k == "credentialId":
                    valid_data[k] = str(v)
                if k == "pingOneConnectionId":
                    valid_data[k] = str(v)
                if k == "environmentId":
                    valid_data[k] = str(v)
                if k == "creationDate":
                    valid_data[k] = str(v)
                if k == "organizationName":
                    valid_data[k] = str(v)
                if k == "region":
                    valid_data[k] = str(v)
                if k == "pingOneManagementApiEndpoint":
                    valid_data[k] = str(v)
                if k == "pingOneAuthenticationApiEndpoint":
                    valid_data[k] = str(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "name", "description", "active", "credential", "encryptedCredential", "credentialId", "pingOneConnectionId", "environmentId", "creationDate", "organizationName", "region", "pingOneManagementApiEndpoint", "pingOneAuthenticationApiEndpoint"]:
                if isinstance(v, Model):
                    body[k] = v.to_dict(remove_nonetypes)
                elif isinstance(v, list):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, dict):
                    vals = {}
                    for x, y in v.items():
                        if isinstance(y, Model):
                            vals[x] = y.to_dict(remove_nonetypes)
                        elif not remove_nonetypes or (remove_nonetypes and y is not None):
                            vals[x] = y
                    body[k] = vals
                elif isinstance(v, set):
                    vals = []
                    for x in v:
                        if isinstance(x, Model):
                            vals.append(x.to_dict(remove_nonetypes))
                        elif not remove_nonetypes or (remove_nonetypes and x is not None):
                            vals.append(x)
                    body[k] = vals
                elif isinstance(v, Enum):
                    body[k] = str(v).split('.')[-1]
                elif not remove_nonetypes or (remove_nonetypes and v is not None):
                    body[k] = v
        return body
