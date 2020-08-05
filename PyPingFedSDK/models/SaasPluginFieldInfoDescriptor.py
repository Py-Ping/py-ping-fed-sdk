class SaasPluginFieldInfoDescriptor():
    """A Saas Plugin Field configuration.

    Attributes
    ----------
    attributeGroup : boolean
        Indicates whether this field belongs to group of attribute such as multivalued or sub-type custom attributes.    code : string
        The name or code that represents a field.    defaultValue : string
        Default value for the field.    dsLdapMap : boolean
        Indicates whether the field can be mapped raw to an LDAP attribute.    label : string
        The label for a field.    maxLength : integer
        Maximum character length for a value.    minLength : integer
        Minimum character length for a value.    multiValue : boolean
        Whether the field can have multiple values.    notes : array
        Description or notes for the field.    options : array
        List of Option values available for this field.    pattern : str
        Pattern used to validate values of this field.    persistForMembership : boolean
        The code that represents the field.    required : boolean
        Indicates whether a value is required for this field.    unique : boolean
        indicates whether the value of this field is unique.
    """

    __slots__ = ["attributeGroup", "code", "defaultValue", "dsLdapMap", "label", "maxLength", "minLength", "multiValue", "notes", "options", "pattern", "persistForMembership", "required", "unique"]

    def __init__(self, code, label, attributeGroup=None, defaultValue=None, dsLdapMap=None, maxLength=None, minLength=None, multiValue=None, notes=None, options=None, pattern=None, persistForMembership=None, required=None, unique=None):
        self.attributeGroup = attributeGroup
        self.code = code
        self.defaultValue = defaultValue
        self.dsLdapMap = dsLdapMap
        self.label = label
        self.maxLength = maxLength
        self.minLength = minLength
        self.multiValue = multiValue
        self.notes = notes
        self.options = options
        self.pattern = pattern
        self.persistForMembership = persistForMembership
        self.required = required
        self.unique = unique

    def _validate(self):
        return any(x for x in ['code', 'label'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, SaasPluginFieldInfoDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.attributeGroup, self.code, self.defaultValue, self.dsLdapMap, self.label, self.maxLength, self.minLength, self.multiValue, self.notes, self.options, self.pattern, self.persistForMembership, self.required, self.unique))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["attributeGroup", "code", "defaultValue", "dsLdapMap", "label", "maxLength", "minLength", "multiValue", "notes", "options", "pattern", "persistForMembership", "required", "unique"]}

        return cls(**valid_data)
