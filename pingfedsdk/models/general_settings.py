from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.enums import IdpConnectionTransactionLoggingOverride
from pingfedsdk.enums import SpConnectionTransactionLoggingOverride


class GeneralSettings(Model):
    """General settings.

    Attributes
    ----------
    disableAutomaticConnectionValidation: bool
        Boolean that disables automatic connection validation when set to true. The default is false.

    idpConnectionTransactionLoggingOverride: IdpConnectionTransactionLoggingOverride
        Determines the level of transaction logging for all identity provider connections. The default is DONT_OVERRIDE, in which case the logging level will be determined by each individual IdP connection

    spConnectionTransactionLoggingOverride: SpConnectionTransactionLoggingOverride
        Determines the level of transaction logging for all service provider connections. The default is DONT_OVERRIDE, in which case the logging level will be determined by each individual SP connection

    datastoreValidationIntervalSecs: int
        Determines how long (in seconds) the result of testing a datastore connection is cached. The default is 300.

    requestHeaderForCorrelationId: str
        HTTP request header for retrieving correlation ID.

    """

    def __init__(self, disableAutomaticConnectionValidation: bool = None, idpConnectionTransactionLoggingOverride: IdpConnectionTransactionLoggingOverride = None, spConnectionTransactionLoggingOverride: SpConnectionTransactionLoggingOverride = None, datastoreValidationIntervalSecs: int = None, requestHeaderForCorrelationId: str = None) -> None:
        self.disableAutomaticConnectionValidation = disableAutomaticConnectionValidation
        self.idpConnectionTransactionLoggingOverride = idpConnectionTransactionLoggingOverride
        self.spConnectionTransactionLoggingOverride = spConnectionTransactionLoggingOverride
        self.datastoreValidationIntervalSecs = datastoreValidationIntervalSecs
        self.requestHeaderForCorrelationId = requestHeaderForCorrelationId

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, GeneralSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.disableAutomaticConnectionValidation, self.idpConnectionTransactionLoggingOverride, self.spConnectionTransactionLoggingOverride, self.datastoreValidationIntervalSecs, self.requestHeaderForCorrelationId]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["disableAutomaticConnectionValidation", "idpConnectionTransactionLoggingOverride", "spConnectionTransactionLoggingOverride", "datastoreValidationIntervalSecs", "requestHeaderForCorrelationId"] and v is not None:
                if k == "disableAutomaticConnectionValidation":
                    valid_data[k] = bool(v)
                if k == "idpConnectionTransactionLoggingOverride":
                    valid_data[k] = IdpConnectionTransactionLoggingOverride[v]
                if k == "spConnectionTransactionLoggingOverride":
                    valid_data[k] = SpConnectionTransactionLoggingOverride[v]
                if k == "datastoreValidationIntervalSecs":
                    valid_data[k] = int(v)
                if k == "requestHeaderForCorrelationId":
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
            if k in ["disableAutomaticConnectionValidation", "idpConnectionTransactionLoggingOverride", "spConnectionTransactionLoggingOverride", "datastoreValidationIntervalSecs", "requestHeaderForCorrelationId"]:
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
