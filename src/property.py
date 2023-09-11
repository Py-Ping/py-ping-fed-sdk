from helpers import get_py_type, strip_ref


class Property:
    """
    A Property of a model object.

    Each property section of a model defines details of the variable it represents, including:
     - it's type
     - if it is a data structure, what subtypes it has
     - if the type is another model which model it is
     - if it is an enum what domain does it have
    """

    # Sometimes enums have the same name as a model and if the enum is imported
    # by the model there would be a name conflict whereby the imported enum is
    # overshadowed by the model class. In such cases we import the enum under a
    # different name (in the scope of the model class) by appending the suffix
    # given by $CONFLICT_SUFFIX to the enum name, thereby making it different
    # from the model name.
    CONFLICT_SUFFIX = 'Enum'

    def __init__(self, raw_property: dict, model_name=None, property_name=None):
        self.raw_property_dict = raw_property
        self.sub_type = None
        self.enum_domain = None
        self.json_type = None
        self.type = None
        self.json_sub_type = None
        self.model_name = model_name
        self.name = property_name
        self.description = None
        self._process()

    def _process(self):
        """
         This method loads all values from the dictionary into the class so type information can
         be queried when we generate the package. This includes:
          - determing what models to import
          - determining the enum classes to import
          - generating the type marshalling string for the `from_dict` method
          - providing more type hint details
        """
        type_class = strip_ref(self.raw_property_dict.get("$ref", ""))

        self.description = self.raw_property_dict.get(
            "description", ""
        ).replace("\n", "").replace("<br>", "\n        ").replace(" \n", "\n").strip()

        if type_class and "enum" in self.raw_property_dict:
            self.enum_domain = self.raw_property_dict["enum"]
            self.json_type = "enum"
            self.type = type_class

        elif "type" in self.raw_property_dict and "enum" in self.raw_property_dict:
            self.enum_domain = self.raw_property_dict["enum"]
            self.json_type = "enum"
            self.type = self.get_enums_class(self.model_name, self.name)

        elif "type" in self.raw_property_dict and self.raw_property_dict["type"] == "array":
            self.json_type = "array"
            self.type = "list"

            items = self.raw_property_dict["items"]
            if "enum" in items:
                self.json_sub_type = "enum"
                if "type" in items:
                    if items["type"] == "string":
                        self.json_type = self.raw_property_dict["type"]
                        self.type = self.raw_property_dict["type"]
                        if get_py_type(self.raw_property_dict["type"]):
                            self.type = get_py_type(self.raw_property_dict["type"])
                        if "type" in items:
                            self.sub_type = get_py_type(items["type"])
                            self.json_sub_type = items["type"]
                    else:
                        self.enum_domain = strip_ref(items["type"])
                        self.sub_type = strip_ref(items["type"])
                else:
                    self.enum_domain = strip_ref(items["$ref"])
                    self.sub_type = strip_ref(items["$ref"])
                self.enum_domain = items["enum"]
            elif "$ref" in items and not get_py_type(items["$ref"]):
                self.json_sub_type = strip_ref(items["$ref"])
                self.sub_type = strip_ref(items["$ref"])
            else:
                self.json_sub_type = items["type"]
                self.sub_type = get_py_type(items["type"])

        elif type_class and type_class.startswith("Map"):
            self.json_type = "Map"
            self.type = "dict"
            key_label, value_label = type_class.replace("Map[", "").replace("]", "").split(",")
            self.json_sub_type = key_label, value_label

            if get_py_type(key_label):
                key_label = get_py_type(key_label)
            if get_py_type(value_label):
                value_label = get_py_type(value_label)

            self.sub_type = key_label, value_label

        elif type_class == "File":
            self.type = "file"
            self.json_type = "File"

        elif type_class == "Set" and "items" in self.raw_property_dict:
            items = self.raw_property_dict["items"]
            self.type = "set"
            self.json_type = "Set"
            if "enum" in items:
                self.json_sub_type = "enum"
                self.sub_type = strip_ref(items["$ref"])
                self.enum_domain = items["enum"]
            elif "$ref" in items and get_py_type(items["$ref"]):
                self.sub_type = get_py_type(items["$ref"])
                self.json_sub_type = items["$ref"]
            elif "$ref" in items:
                self.sub_type = strip_ref(items["$ref"])
                self.json_sub_type = strip_ref(items["$ref"])
            elif "type" in items:
                self.sub_type = get_py_type(items["type"])
                self.json_sub_type = items["type"]

        elif "type" in self.raw_property_dict:
            self.json_type = self.raw_property_dict["type"]
            self.type = self.raw_property_dict["type"]
            if get_py_type(self.raw_property_dict["type"]):
                self.type = get_py_type(self.raw_property_dict["type"])

        elif "$ref" in self.raw_property_dict and not get_py_type(self.raw_property_dict["$ref"]):
            self.json_type = strip_ref(self.raw_property_dict["$ref"])
            self.type = strip_ref(self.raw_property_dict["$ref"])

    def get_model_import(self):
        """
        Return the model import for this property
        """
        if self.type == self.model_name or self.json_sub_type == self.model_name:
            return None
        elif self.type == "object":
            return None
        elif self.type == "dict":
            if not get_py_type(self.json_sub_type[1]) and \
               self.json_sub_type[1] != self.model_name and \
               self.json_sub_type[1] != "Object":
                return self.json_sub_type[1]
        elif self.type in ("list", "set"):
            if not get_py_type(self.json_sub_type) and self.json_sub_type not in ("enum", "Object"):
                return self.sub_type
        elif get_py_type(self.json_type):
            return None
        elif self.json_type != "enum" and not get_py_type(self.json_sub_type):
            return self.type

    def get_enum_import(self):
        """
        Return the enum import for this property
        """

        if self.json_type == "enum":
            return self.type
        elif self.type in ("list", "set") and self.json_sub_type == "enum":
            return self.sub_type
        elif get_py_type(self.json_type):
            return None

    def get_enums(self):
        """
        If this property references an enum, return the name and enum domain.
        """
        enum_name = self.get_enum_import()
        if not enum_name:
            return None
        return enum_name, self.enum_domain

    def get_enums_class(self, model_name, type):
        """
        As of V11, the construct of Enums has changed.
        This class updates the Enum type in order
        to generate generic classes as found in
        pingfedsdk/enums.py
        """
        if 'BackChannelAuth' == model_name:
            return 'BackChannelAuthType'
        elif 'Connection' == model_name and type == 'type':
            return 'ConnectionType'
        elif 'IdpConnection' == model_name and type == 'type':
            return 'IdpConnection'
        elif 'SpConnection' == model_name and type == 'type':
            return 'SpConnection'
        elif ('DataStore' == model_name and type != 'ldapType') or ('AttributeSource' == model_name and type == 'type'):
            return 'DataStoreType'
        elif 'DisplayUnit' == type or 'TimeUnit' in type or 'persistentGrantLifetimeUnit' == type:
            return 'TimeUnit'
        elif 'FieldDescriptor' == model_name:
            return 'FieldDescriptor'
        elif 'IdentityField' == model_name:
            return 'LocalIdentityFieldType'
        elif 'PolicyAction' == model_name:
            return 'AuthenticationPolicySelectionActionType'
        elif 'ObjectSigningAlgorithm' == type or 'AuthSigningAlgorithm' == type:
            return 'ObjectSigningAlgorithm'
        elif type == 'idTokenSigningAlgorithm' or type == 'requestSigningAlgorithm' \
                or type == 'authenticationSigningAlgorithm':
            return 'SigningAlgorithm'
        elif type == 'idTokenEncryptionAlgorithm':
            return 'EncryptionAlgorithm'
        elif type == 'idTokenContentEncryptionAlgorithm':
            return 'ContentEncryptionAlgorithm'
        elif type == 'persistentGrantExpirationType' or type == 'persistentGrantIdleTimeoutType':
            return 'PersistentGrantLifetimeType'
        elif type == 'refreshTokenRollingIntervalType' or type == 'persistentGrantReuseType' \
                or type == 'deviceFlowSettingType':
            return 'DeviceFlowSettingType'
        elif type == 'type':
            return f"{model_name}Type"
        elif model_name == 'IncomingProxySettings':
            return 'ForwardedHeaderIndex'
        elif 'Resource' in model_name:
            return 'ResourceCategory'
        else:
            return f"{type[0].upper()}{type[1:]}"

    def get_from_dict_str(self):
        """
        Used to convert a JSON dictionary into its object component
        different types are processed in their own way

        - dictionaries
        - lists/sets
        - enums
        - models
        - primitive types
        """
        if self.type == "DataStore":
            return """if x["type"] == "JDBC":
                    valid_data[k] = [JdbcDataStore(**x) for x in v]
                elif x["type"] == "LDAP":
                    valid_data[k] = [LdapDataStore(**x) for x in v]
                elif x["type"] == "CUSTOM":
                    valid_data[k] = [CustomDataStore(**x) for x in v]
                else:
                    valid_data[k] = [DataStore(**x) for x in v]
            """
        elif self.type == "dict":
            if get_py_type(self.json_sub_type[0]) and self.json_sub_type[0] != "void":
                key_assign = f"{self.sub_type[0]}(x)"
            else:
                key_assign = f"{self.sub_type[0]}(**x)"
            if get_py_type(self.json_sub_type[1]) and self.json_sub_type[1] != "void":
                val_assign = f"{self.sub_type[1]}(y)"
            else:
                val_assign = f"{self.sub_type[1]}(**y)"
            return f"valid_data[k] = {{{key_assign}: {val_assign} for x, y in v.items()}}"

        elif self.type in ("set", "list"):
            if self.type == "set":
                start_bracket = "set({"
                end_bracket = "})"
            else:
                start_bracket = "["
                end_bracket = "]"

            if self.sub_type == "DataStore":
                return """temp_list = []
                    for x in v:
                        if x["type"] == "JDBC":
                            temp_list.append(JdbcDataStore(**x))
                        elif x["type"] == "LDAP":
                            temp_list.append(LdapDataStore(**x))
                        elif x["type"] == "CUSTOM":
                            temp_list.append(CustomDataStore(**x))
                        else:
                            temp_list.append(DataStore(**x))
                    valid_data[k] = temp_list
                """
            elif self.json_sub_type == "enum":
                return f"valid_data[k] = {start_bracket}{self.sub_type}[x] for x in v{end_bracket}"
            elif get_py_type(self.json_sub_type):
                return f"valid_data[k] = {start_bracket}{self.sub_type}(x) for x in v{end_bracket}"
            elif self.json_sub_type == "Object" or self.json_sub_type == "object":
                return "valid_data[k] = v"
            else:
                return f"valid_data[k] = {start_bracket}{self.sub_type}(**x) for x in v{end_bracket}"

        elif self.json_type == "enum":
            if self.type == self.model_name:
                return f"valid_data[k] = {self.type}{self.CONFLICT_SUFFIX}[v]"
            else:
                return f"valid_data[k] = {self.type}[v]"

        elif not get_py_type(self.json_type):
            return f"valid_data[k] = {self.type}(**v)"

        elif self.type == "None":
            return "valid_data[k] = None"
        else:
            return f"valid_data[k] = {self.type}(v)"
