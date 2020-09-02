from helpers import json_type_convert


class Property:
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
        Each property section of a model defines details of the variable it represents, including:
         - it's type
         - if it is a data structure, what subtypes it has
         - if the type is another model which model it is
         - if it is an enum what domain does it have

         This method loads all values from the dictionary into the class so type information can
         be queried when we generate the package. This includes:
          - determing what models to import
          - determining the enum classes to import
          - generating the type marshalling string for the `from_dict` method
          - providing more type hint details
        """
        type_class = self.raw_property_dict.get("$ref")
        self.description = self.raw_property_dict.get(
            "description", ""
        ).replace("\n", "").replace("<br>", "\n        ").replace(" \n", "\n").strip()

        if type_class and "enum" in self.raw_property_dict:
            self.enum_domain = self.raw_property_dict["enum"]
            self.json_type = "enum"
            self.type = type_class

        elif "type" in self.raw_property_dict and self.raw_property_dict["type"] == "array":
            self.json_type = "array"
            self.type = "list"

            items = self.raw_property_dict["items"]
            if "enum" in items:
                self.json_sub_type = "enum"
                self.enum_domain = items["$ref"]
                self.sub_type = items["$ref"]
                self.enum_domain = items["enum"]
            elif "$ref" in items and not json_type_convert(items["$ref"]):
                self.json_sub_type = items["$ref"]
                self.sub_type = items["$ref"]
            else:
                self.json_sub_type = items["type"]
                self.sub_type = json_type_convert(items["type"])

        elif type_class and type_class.startswith("Map"):
            self.json_type = "Map"
            self.type = "dict"
            key_label, value_label = type_class.replace("Map[", "").replace("]", "").split(",")
            self.json_sub_type = key_label, value_label

            if json_type_convert(key_label):
                key_label = json_type_convert(key_label)
            if json_type_convert(value_label):
                value_label = json_type_convert(value_label)

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
                self.sub_type = items["$ref"]
                self.enum_domain = items["enum"]
            elif "$ref" in items and json_type_convert(items["$ref"]):
                self.sub_type = json_type_convert(items["$ref"])
                self.json_sub_type = items["$ref"]
            elif "$ref" in items:
                self.sub_type = items["$ref"]
                self.json_sub_type = items["$ref"]
            elif "type" in items:
                self.sub_type = json_type_convert(items["type"])
                self.json_sub_type = items["type"]

        elif "type" in self.raw_property_dict:
            self.json_type = self.raw_property_dict["type"]
            self.type = self.raw_property_dict["type"]
            if json_type_convert(self.raw_property_dict["type"]):
                self.type = json_type_convert(self.raw_property_dict["type"])

        elif "$ref" in self.raw_property_dict and not json_type_convert(self.raw_property_dict["$ref"]):
            self.json_type = self.raw_property_dict["$ref"]
            self.type = self.raw_property_dict["$ref"]

    def get_model_import(self):
        """
        Return the model import for this property
        """
        if self.type == self.model_name or self.json_sub_type == self.model_name:
            return None
        elif self.type == "dict":
            if not json_type_convert(self.json_sub_type[1]) and \
               self.json_sub_type[1] != self.model_name and \
               self.json_sub_type[1] != "Object":
                return self.json_sub_type[1]
        elif self.type in ("list", "set"):
            if not json_type_convert(self.json_sub_type) and self.json_sub_type not in ("enum", "Object"):
                return self.sub_type
        elif json_type_convert(self.json_type):
            return None
        elif self.json_type != "enum" and not json_type_convert(self.json_sub_type):
            return self.type

    def get_enum_import(self):
        """
        Return the enum import for this property
        """

        if self.json_type == "enum":
            return self.type
        elif self.type in ("list", "set") and self.json_sub_type == "enum":
            return self.sub_type
        elif json_type_convert(self.json_type):
            return None

    def get_enums(self):
        enum_name = self.get_enum_import()
        if not enum_name:
            return None
        return enum_name, self.enum_domain

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

        if self.type == "dict":
            if json_type_convert(self.json_sub_type[0]) and self.json_sub_type[0] != "void":
                key_assign = f"{self.sub_type[0]}(x)"
            else:
                key_assign = f"{self.sub_type[0]}(**x)"
            if json_type_convert(self.json_sub_type[1]) and self.json_sub_type[1] != "void":
                val_assign = f"{self.sub_type[1]}(y)"
            else:
                val_assign = f"{self.sub_type[1]}(**y)"
            return f"{{{key_assign}: {val_assign} for x, y in v.items()}}"

        elif self.type in ("set", "list"):
            if self.type == "set":
                start_bracket = "set({"
                end_bracket = "})"
            else:
                start_bracket = "["
                end_bracket = "]"
            if self.json_sub_type == "enum":
                return f'{start_bracket}{self.sub_type}[x] for x in v{end_bracket}'
            elif json_type_convert(self.json_sub_type):
                return f"{start_bracket}{self.sub_type}(x) for x in v{end_bracket}"
            elif self.json_sub_type == "Object":
                return "v"
            else:
                return f"{start_bracket}{self.sub_type}(**x) for x in v{end_bracket}"

        elif self.json_type == "enum":
            return f'{self.type}[v]'

        elif not json_type_convert(self.json_type):
            return f"{self.type}(**v)"

        elif self.type == "None":
            return "None"

        else:
            return f"{self.type}(v)"
