class AttributeSource():
    """The configured settings to look up attributes from an associated data store.

    Attributes
    ----------
    attributeContractFulfillment : str
 A list of mappings from attribute names to their fulfillment values. This field is only valid for the SP Connection's Browser SSO mappings
    dataStoreRef : str
 Reference to the associated data store.
    description : string
 The description of this attribute source. The description needs to be unique amongst the attribute sources for the mapping.<br>Note: Required for APC-to-SP Adapter Mappings
    id : string
 The ID that defines this attribute source. Only alphanumeric characters allowed.<br>Note: Required for OpenID Connect policy attribute sources, OAuth IdP adapter mappings, OAuth access token mappings and APC-to-SP Adapter Mappings. IdP Connections will ignore this property since it only allows one attribute source to be defined per mapping. IdP-to-SP Adapter Mappings can contain multiple attribute sources.
    type : str
 The data store type of this attribute source.

    """

    def __init__(self, var_type, dataStoreRef, attributeContractFulfillment=None, description=None, var_id=None) -> None:
        self.attributeContractFulfillment = attributeContractFulfillment
        self.dataStoreRef = dataStoreRef
        self.description = description
        self.var_id = var_id
        self.var_type = var_type

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "dataStoreRef"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, AttributeSource):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.attributeContractFulfillment, self.dataStoreRef, self.description, self.var_id, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeContractFulfillment", "dataStoreRef", "description", "var_id", "var_type"]}

        return cls(**valid_data)