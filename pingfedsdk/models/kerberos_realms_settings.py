from pingfedsdk.model import Model
from enum import Enum


class KerberosRealmsSettings(Model):
    """Settings for all of the Kerberos Realms.

    Attributes
    ----------
    forceTcp: bool
        Reference to the default security.

    kdcRetries: str
        Reference to the default Key Distribution Center Retries.

    debugLogOutput: bool
        Reference to the default logging.

    kdcTimeout: str
        Reference to the default Key Distribution Center Timeout (in seconds).

    keySetRetentionPeriodMins: int
        The key set retention period in minutes. When 'retainPreviousKeysOnPasswordChange' is set to true for a realm, this setting determines how long keys will be retained after a password change occurs. If this field is omitted in a PUT request, the default of 610 minutes is applied.

    """

    def __init__(self, kdcRetries: str = None, kdcTimeout: str = None, forceTcp: bool = None, debugLogOutput: bool = None, keySetRetentionPeriodMins: int = None) -> None:
        self.forceTcp = forceTcp
        self.kdcRetries = kdcRetries
        self.debugLogOutput = debugLogOutput
        self.kdcTimeout = kdcTimeout
        self.keySetRetentionPeriodMins = keySetRetentionPeriodMins

    def _validate(self) -> bool:
        return any(x for x in ["kdcRetries", "kdcTimeout"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, KerberosRealmsSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.forceTcp, self.kdcRetries, self.debugLogOutput, self.kdcTimeout, self.keySetRetentionPeriodMins]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["forceTcp", "kdcRetries", "debugLogOutput", "kdcTimeout", "keySetRetentionPeriodMins"] and v is not None:
                if k == "forceTcp":
                    valid_data[k] = bool(v)
                if k == "kdcRetries":
                    valid_data[k] = str(v)
                if k == "debugLogOutput":
                    valid_data[k] = bool(v)
                if k == "kdcTimeout":
                    valid_data[k] = str(v)
                if k == "keySetRetentionPeriodMins":
                    valid_data[k] = int(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["forceTcp", "kdcRetries", "debugLogOutput", "kdcTimeout", "keySetRetentionPeriodMins"]:
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
