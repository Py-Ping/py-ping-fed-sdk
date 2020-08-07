class LdapDataStoreConfig():
    """LDAP data store configuration.

    Attributes
    ----------
    baseDn : string
 The base DN to search from. If not specified, the search will start at the LDAP's root.
    createPattern : string
 The Relative DN Pattern that will be used to create objects in the directory.
    dataStoreMapping : str
 The data store mapping.
    dataStoreRef : str
 Reference to the associated data store.
    objectClass : string
 The Object Class used by the new objects stored in the LDAP data store.
    type : str
 The data store config type.

    """

    def __init__(self, var_type, dataStoreRef, baseDn, createPattern, objectClass, dataStoreMapping) -> None:
        self.baseDn = baseDn
        self.createPattern = createPattern
        self.dataStoreMapping = dataStoreMapping
        self.dataStoreRef = dataStoreRef
        self.objectClass = objectClass
        self.var_type = var_type

    def _validate(self) -> bool:
        return any(x for x in ["var_type", "dataStoreRef", "baseDn", "createPattern", "objectClass", "dataStoreMapping"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, LdapDataStoreConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.baseDn, self.createPattern, self.dataStoreMapping, self.dataStoreRef, self.objectClass, self.var_type))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["baseDn", "createPattern", "dataStoreMapping", "dataStoreRef", "objectClass", "var_type"]}

        return cls(**valid_data)