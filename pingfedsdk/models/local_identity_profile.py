from enum import Enum

from pingfedsdk.model import Model
from pingfedsdk.models.data_store_config import DataStoreConfig
from pingfedsdk.models.email_verification_config import EmailVerificationConfig
from pingfedsdk.models.field_config import FieldConfig
from pingfedsdk.models.local_identity_auth_source import LocalIdentityAuthSource
from pingfedsdk.models.local_identity_auth_source_update_policy import LocalIdentityAuthSourceUpdatePolicy
from pingfedsdk.models.profile_config import ProfileConfig
from pingfedsdk.models.registration_config import RegistrationConfig
from pingfedsdk.models.resource_link import ResourceLink


class LocalIdentityProfile(Model):
    """A local identity profile.

    Attributes
    ----------
    id: str
        The persistent, unique ID for the local identity profile. It can be any combination of [a-zA-Z0-9._-]. This property is system-assigned if not specified.

    name: str
        The local identity profile name. Name is unique.

    apcId: ResourceLink
        The reference to the authentication policy contract to use for this local identity profile.

    authSources: list
        The local identity authentication sources. Sources are unique.

    authSourceUpdatePolicy: LocalIdentityAuthSourceUpdatePolicy
        The attribute update policy for authentication sources.

    registrationEnabled: bool
        Whether the registration configuration is enabled or not.

    registrationConfig: RegistrationConfig
        The local identity profile registration configuration.

    profileConfig: ProfileConfig
        The local identity profile management configuration.

    fieldConfig: FieldConfig
        The local identity profile field configuration.

    emailVerificationConfig: EmailVerificationConfig
        The local identity email verification configuration.

    dataStoreConfig: DataStoreConfig
        The local identity profile data store configuration.

    profileEnabled: bool
        Whether the profile configuration is enabled or not.

    """
    def __init__(self, name: str, apcId: ResourceLink, id: str = None, authSources: list = None, authSourceUpdatePolicy: LocalIdentityAuthSourceUpdatePolicy = None, registrationEnabled: bool = None, registrationConfig: RegistrationConfig = None, profileConfig: ProfileConfig = None, fieldConfig: FieldConfig = None, emailVerificationConfig: EmailVerificationConfig = None, dataStoreConfig: DataStoreConfig = None, profileEnabled: bool = None) -> None:
        self.id = id
        self.name = name
        self.apcId = apcId
        self.authSources = authSources
        self.authSourceUpdatePolicy = authSourceUpdatePolicy
        self.registrationEnabled = registrationEnabled
        self.registrationConfig = registrationConfig
        self.profileConfig = profileConfig
        self.fieldConfig = fieldConfig
        self.emailVerificationConfig = emailVerificationConfig
        self.dataStoreConfig = dataStoreConfig
        self.profileEnabled = profileEnabled

    def _validate(self) -> bool:
        return any(x for x in ["apcId", "name"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, LocalIdentityProfile):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.id, self.name, self.apcId, self.authSources, self.authSourceUpdatePolicy, self.registrationEnabled, self.registrationConfig, self.profileConfig, self.fieldConfig, self.emailVerificationConfig, self.dataStoreConfig, self.profileEnabled]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["id", "name", "apcId", "authSources", "authSourceUpdatePolicy", "registrationEnabled", "registrationConfig", "profileConfig", "fieldConfig", "emailVerificationConfig", "dataStoreConfig", "profileEnabled"] and v is not None:
                if k == "id":
                    valid_data[k] = str(v)
                if k == "name":
                    valid_data[k] = str(v)
                if k == "apcId":
                    valid_data[k] = ResourceLink.from_dict(v)
                if k == "authSources":
                    valid_data[k] = [LocalIdentityAuthSource.from_dict(x) for x in v]
                if k == "authSourceUpdatePolicy":
                    valid_data[k] = LocalIdentityAuthSourceUpdatePolicy.from_dict(v)
                if k == "registrationEnabled":
                    valid_data[k] = bool(v)
                if k == "registrationConfig":
                    valid_data[k] = RegistrationConfig.from_dict(v)
                if k == "profileConfig":
                    valid_data[k] = ProfileConfig.from_dict(v)
                if k == "fieldConfig":
                    valid_data[k] = FieldConfig.from_dict(v)
                if k == "emailVerificationConfig":
                    valid_data[k] = EmailVerificationConfig.from_dict(v)
                if k == "dataStoreConfig":
                    valid_data[k] = DataStoreConfig.from_dict(v)
                if k == "profileEnabled":
                    valid_data[k] = bool(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["id", "name", "apcId", "authSources", "authSourceUpdatePolicy", "registrationEnabled", "registrationConfig", "profileConfig", "fieldConfig", "emailVerificationConfig", "dataStoreConfig", "profileEnabled"]:
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
