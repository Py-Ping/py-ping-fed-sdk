class LocalIdentityMappingPolicyAction():
    """ A local identity profile selection action.

    Attributes
    ----------
    context : string
        The result context.
    inboundMapping : str
        Inbound mappings into the local identity profile fields.
    localIdentityRef : str
        Reference to the associated local identity profile.
    outboundAttributeMapping : str
        Authentication policy contract mappings associated with this local Identity profile.
    type : str
        The authentication selection type.

    """

    __slots__ = ["context", "inboundMapping", "localIdentityRef", "outboundAttributeMapping", "type"]
    def __init__(self, type, localIdentityRef, outboundAttributeMapping, context=None, inboundMapping=None):
            self.context = context
            self.inboundMapping = inboundMapping
            self.localIdentityRef = localIdentityRef
            self.outboundAttributeMapping = outboundAttributeMapping
            self.type = type
    
    def _validate(self):
        return any(x for x in ['type', 'localIdentityRef', 'outboundAttributeMapping'] if __dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, LocalIdentityMappingPolicyAction):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((context, inboundMapping, localIdentityRef, outboundAttributeMapping, type))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in __slots__}
        
        return cls(**valid_data)
