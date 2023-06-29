from pingfedsdk.model import Model
from enum import Enum
from pingfedsdk.models.saas_plugin_field_option import SaasPluginFieldOption


class SaasPluginFieldInfoDescriptor(Model):
    """A Saas Plugin Field configuration.

    Attributes
    ----------
    code: str
        The name or code that represents a field.

    label: str
        The label for a field.

    required: bool
        Indicates whether a value is required for this field.

    unique: bool
        indicates whether the value of this field is unique.

    multiValue: bool
        Whether the field can have multiple values.

    options: list
        List of Option values available for this field.

    minLength: int
        Minimum character length for a value.

    maxLength: int
        Maximum character length for a value.

    pattern: str
        Pattern used to validate values of this field.

    notes: list
        Description or notes for the field.

    defaultValue: str
        Default value for the field.

    dsLdapMap: bool
        Indicates whether the field can be mapped raw to an LDAP attribute.

    persistForMembership: bool
        The code that represents the field.

    attributeGroup: bool
        Indicates whether this field belongs to group of attribute such as multivalued or sub-type custom attributes.

    """

    def __init__(self, code: str, label: str, required: bool = None, unique: bool = None, multiValue: bool = None, options: list = None, minLength: int = None, maxLength: int = None, pattern: str = None, notes: list = None, defaultValue: str = None, dsLdapMap: bool = None, persistForMembership: bool = None, attributeGroup: bool = None) -> None:
        self.code = code
        self.label = label
        self.required = required
        self.unique = unique
        self.multiValue = multiValue
        self.options = options
        self.minLength = minLength
        self.maxLength = maxLength
        self.pattern = pattern
        self.notes = notes
        self.defaultValue = defaultValue
        self.dsLdapMap = dsLdapMap
        self.persistForMembership = persistForMembership
        self.attributeGroup = attributeGroup

    def _validate(self) -> bool:
        return any(x for x in ["code", "label"] if self.__dict__[x] is not None)

    def __eq__(self, other) -> bool:
        if isinstance(other, SaasPluginFieldInfoDescriptor):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset([self.code, self.label, self.required, self.unique, self.multiValue, self.options, self.minLength, self.maxLength, self.pattern, self.notes, self.defaultValue, self.dsLdapMap, self.persistForMembership, self.attributeGroup]))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {}
        for k, v in python_dict.items():
            if k in ["code", "label", "required", "unique", "multiValue", "options", "minLength", "maxLength", "pattern", "notes", "defaultValue", "dsLdapMap", "persistForMembership", "attributeGroup"] and v is not None:
                if k == "code":
                    valid_data[k] = str(v)
                if k == "label":
                    valid_data[k] = str(v)
                if k == "required":
                    valid_data[k] = bool(v)
                if k == "unique":
                    valid_data[k] = bool(v)
                if k == "multiValue":
                    valid_data[k] = bool(v)
                if k == "options":
                    valid_data[k] = [SaasPluginFieldOption(**x) for x in v]
                if k == "minLength":
                    valid_data[k] = int(v)
                if k == "maxLength":
                    valid_data[k] = int(v)
                if k == "pattern":
                    valid_data[k] = str(v)
                if k == "notes":
                    valid_data[k] = [str(x) for x in v]
                if k == "defaultValue":
                    valid_data[k] = str(v)
                if k == "dsLdapMap":
                    valid_data[k] = bool(v)
                if k == "persistForMembership":
                    valid_data[k] = bool(v)
                if k == "attributeGroup":
                    valid_data[k] = bool(v)

        return cls(**valid_data)

    def to_dict(self, remove_nonetypes=False):
        """
        Naive dictionary serialiser. Recursively handles most types in this
        module. If you make your own class you need to inherit from model
        and implement to_dict.
        """
        body = {}
        for k, v in self.__dict__.items():
            if k in ["code", "label", "required", "unique", "multiValue", "options", "minLength", "maxLength", "pattern", "notes", "defaultValue", "dsLdapMap", "persistForMembership", "attributeGroup"]:
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
