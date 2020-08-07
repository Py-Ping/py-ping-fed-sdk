class CrlSettings():
    """CRL settings.

    Attributes
    ----------
    nextRetryMinsWhenNextUpdateInPast : integer
 Next retry on next update expiration in minutes. This value defaults to "60".
    nextRetryMinsWhenResolveFailed : integer
 Next retry on resolution failure in minutes. This value defaults to "1440".
    treatNonRetrievableCrlAsRevoked : boolean
 Treat non retrievable CRL as revoked. This setting defaults to disabled.
    verifyCrlSignature : boolean
 Verify CRL signature. This setting defaults to enabled.

    """

<<<<<<< HEAD
    def __init__(self, nextRetryMinsWhenNextUpdateInPast=None, nextRetryMinsWhenResolveFailed=None, treatNonRetrievableCrlAsRevoked=None, verifyCrlSignature=None) -> None:
        self.nextRetryMinsWhenNextUpdateInPast = nextRetryMinsWhenNextUpdateInPast
        self.nextRetryMinsWhenResolveFailed = nextRetryMinsWhenResolveFailed
        self.treatNonRetrievableCrlAsRevoked = treatNonRetrievableCrlAsRevoked
        self.verifyCrlSignature = verifyCrlSignature
=======
    def __init__(self, nextRetryMinsWhenNextUpdateInPast=None, nextRetryMinsWhenResolveFailed=None, treatNonRetrievableCrlAsRevoked=None, verifyCrlSignature=None):
        self.nextRetryMinsWhenNextUpdateInPast: str = nextRetryMinsWhenNextUpdateInPast
        self.nextRetryMinsWhenResolveFailed: str = nextRetryMinsWhenResolveFailed
        self.treatNonRetrievableCrlAsRevoked: bool = treatNonRetrievableCrlAsRevoked
        self.verifyCrlSignature: bool = verifyCrlSignature
>>>>>>> Baseline Sphinx generation

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, CrlSettings):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.nextRetryMinsWhenNextUpdateInPast, self.nextRetryMinsWhenResolveFailed, self.treatNonRetrievableCrlAsRevoked, self.verifyCrlSignature))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["nextRetryMinsWhenNextUpdateInPast", "nextRetryMinsWhenResolveFailed", "treatNonRetrievableCrlAsRevoked", "verifyCrlSignature"]}

<<<<<<< HEAD
        return cls(**valid_data)
=======
        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__
>>>>>>> Baseline Sphinx generation
