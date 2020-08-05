class ProtocolMessageCustomization():
    """ The message customization that will be executed on outgoing PingFederate messages.

    Attributes
    ----------
    contextName : string
        The context in which the customization will be applied. Depending on the connection type and protocol, this can either be 'assertion', 'authn-response' or 'authn-request'.
    messageExpression : string
        The OGNL expression that will be executed. Refer to the Admin Manual for a list of variables provided by PingFederate.

    """

    __slots__ = ["contextName", "messageExpression"]
    def __init__(self, contextName=None, messageExpression=None):
            self.contextName = contextName
            self.messageExpression = messageExpression
    
    def _validate(self):
        return any(x for x in [] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, ProtocolMessageCustomization):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((contextName, messageExpression))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
