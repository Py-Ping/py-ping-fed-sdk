class CrlSettings():
    """CRL settings.

    Attributes
    ----------
    nextRetryMinsWhenNextUpdateInPast : integer
        Next retry on next update expiration in minutes. This value defaults to "60".    nextRetryMinsWhenResolveFailed : integer
        Next retry on resolution failure in minutes. This value defaults to "1440".    treatNonRetrievableCrlAsRevoked : boolean
        Treat non retrievable CRL as revoked. This setting defaults to disabled.    verifyCrlSignature : boolean
        Verify CRL signature. This setting defaults to enabled.
    """

    __slots__ = ["nextRetryMinsWhenNextUpdateInPast", "nextRetryMinsWhenResolveFailed", "treatNonRetrievableCrlAsRevoked", "verifyCrlSignature"]

    def __init__(self, nextRetryMinsWhenNextUpdateInPast=None, nextRetryMinsWhenResolveFailed=None, treatNonRetrievableCrlAsRevoked=None, verifyCrlSignature=None):
        self.nextRetryMinsWhenNextUpdateInPast: str = nextRetryMinsWhenNextUpdateInPast
        self.nextRetryMinsWhenResolveFailed: str = nextRetryMinsWhenResolveFailed
        self.treatNonRetrievableCrlAsRevoked: bool = treatNonRetrievableCrlAsRevoked
        self.verifyCrlSignature: bool = verifyCrlSignature

    def _validate(self):
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, CrlSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.nextRetryMinsWhenNextUpdateInPast, self.nextRetryMinsWhenResolveFailed, self.treatNonRetrievableCrlAsRevoked, self.verifyCrlSignature))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["nextRetryMinsWhenNextUpdateInPast", "nextRetryMinsWhenResolveFailed", "treatNonRetrievableCrlAsRevoked", "verifyCrlSignature"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__