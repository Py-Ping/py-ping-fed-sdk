class ProtocolMessageCustomization():
    """The message customization that will be executed on outgoing PingFederate messages.

    Attributes
    ----------
    contextName : string
        The context in which the customization will be applied. Depending on the connection type and protocol, this can either be 'assertion', 'authn-response' or 'authn-request'.
    messageExpression : string
        The OGNL expression that will be executed. Refer to the Admin Manual for a list of variables provided by PingFederate.

    """

    def __init__(self, contextName:str=None, messageExpression:str=None) -> None:
        self.contextName = contextName
        self.messageExpression = messageExpression

    def _validate(self) -> bool:
        return any(x for x in [] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ProtocolMessageCustomization):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.contextName, self.messageExpression))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["contextName", "messageExpression"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__