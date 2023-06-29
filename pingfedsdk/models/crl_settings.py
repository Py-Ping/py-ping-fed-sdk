from pingfedsdk.model import Model
from enum import Enum


class CrlSettings(Model):
    """CRL settings.

    Attributes
    ----------
    treatNonRetrievableCrlAsRevoked: bool
        Treat non retrievable CRL as revoked. This setting defaults to disabled.

    verifyCrlSignature: bool
        Verify CRL signature. This setting defaults to enabled.

    nextRetryMinsWhenResolveFailed: int
        Next retry on resolution failure in minutes. This value defaults to "1440".

    nextRetryMinsWhenNextUpdateInPast: int
        Next retry on next update expiration in minutes. This value defaults to "60".

    """

    def __init__(self, treatNonRetrievableCrlAsRevoked: bool = None, verifyCrlSignature: bool = None, nextRetryMinsWhenResolveFailed: int = None, nextRetryMinsWhenNextUpdateInPast: int = None) -> None:
        self.treatNonRetrievableCrlAsRevoked = treatNonRetrievableCrlAsRevoked
        self.verifyCrlSignature = verifyCrlSignature
        self.nextRetryMinsWhenResolveFailed = nextRetryMinsWhenResolveFailed
        self.nextRetryMinsWhenNextUpdateInPast = nextRetryMinsWhenNextUpdateInPast

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, CrlSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.treatNonRetrievableCrlAsRevoked, self.verifyCrlSignature, self.nextRetryMinsWhenResolveFailed, self.nextRetryMinsWhenNextUpdateInPast]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["treatNonRetrievableCrlAsRevoked", "verifyCrlSignature", "nextRetryMinsWhenResolveFailed", "nextRetryMinsWhenNextUpdateInPast"] and v is not None:
                if k == "treatNonRetrievableCrlAsRevoked":
                    valid_data[k] = bool(v)
                if k == "verifyCrlSignature":
                    valid_data[k] = bool(v)
                if k == "nextRetryMinsWhenResolveFailed":
                    valid_data[k] = int(v)
                if k == "nextRetryMinsWhenNextUpdateInPast":
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
            if k in ["treatNonRetrievableCrlAsRevoked", "verifyCrlSignature", "nextRetryMinsWhenResolveFailed", "nextRetryMinsWhenNextUpdateInPast"]:
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
