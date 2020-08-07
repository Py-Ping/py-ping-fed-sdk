class ConfigOperation():
    """Model describing a list of configuration operations for a given resource type.

    Attributes
    ----------
    itemIds : array
 The item ID's for the operation. This field only applies to the DELETE operation type.
    items : array
 The configuration items for the operation. This field only applies to the SAVE operation type.
    operationType : str
 The type of operation to be performed.
    resourceType : string
 The identifier for the resource type the operation applies to.
    subResource : string
 The subresource for the operation.

    """

    def __init__(self, resourceType, operationType, itemIds=None, items=None, subResource=None) -> None:
        self.itemIds = itemIds
        self.items = items
        self.operationType = operationType
        self.resourceType = resourceType
        self.subResource = subResource

    def _validate(self) -> bool:
        return any(x for x in ["resourceType", "operationType"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, ConfigOperation):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.itemIds, self.items, self.operationType, self.resourceType, self.subResource))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["itemIds", "items", "operationType", "resourceType", "subResource"]}

        return cls(**valid_data)