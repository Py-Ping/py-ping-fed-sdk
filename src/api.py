
from helpers import json_type_convert, safe_name


class ApiEndpoint:
    """
    Manages data and logic for working with an Api class
    This was created to take out as much logic as possible from
    the Jinja template and make it compatible with Python native
    Dynamic classes.
    """

    def __init__(self, api_path, api_data):
        self.api_data = api_data
        self.safe_api_path = safe_name(api_path)
        self.path = api_path
        self.response_codes = set()
        self.imports = set()
        self.operations = []
        self._process()

    def _process(self):
        for data in self.api_data:
            for op in data["operations"]:
                params = []
                for param in op["parameters"]:
                    param_obj = Parameter(param)
                    params.append(param_obj)
                    if not param_obj.is_primitive_type and param_obj.type not in self.imports:
                        self.imports.add(param_obj.type)

                op_response_codes = []
                for response_code in op["responseMessages"]:
                    op_code = {"code": response_code["code"], "message": response_code["message"]}
                    op_response_codes.append(op_code)
                    if response_code["code"] not in self.response_codes:
                        self.response_codes.add(response_code["code"])

                if not json_type_convert(op["type"]) and op["type"] not in self.imports:
                    self.imports.add(op["type"])
                self.operations.append(
                    Operation(
                        params, op_response_codes, op["type"],
                        op["nickname"], op["summary"], op["method"], data["path"])
                )


class Operation:
    def __init__(self, parameters=[], response_codes=[], op_type=None, nickname='', summary='', method='', api_path=''):
        self.parameters = parameters
        self.response_codes = response_codes
        self.json_type = op_type
        self.type = op_type
        if json_type_convert(op_type):
            self.type = json_type_convert(op_type)
        self.is_primitive_type = bool(json_type_convert(op_type))
        self.nickname = nickname
        self.summary = summary
        self.method = method
        self.api_path = api_path

    def get_response_str(self):
        if json_type_convert(self.json_type) not in ("", "None") and self.is_primitive_type:
            return f"{self.type}(response)"
        elif json_type_convert(self.json_type) == "None":
            return "response.json()"
        else:
            return f"Model{self.type}.from_dict(response.json())"

    def get_return_type_str(self):
        if self.type not in ("", "None") and self.is_primitive_type:
            return self.type
        elif self.type == "None":
            return "dict"
        return f"Model{self.json_type}"


class Parameter:
    def __init__(self, param):
        self._raw_param = param
        self.json_type = self._raw_param["type"]
        self.type = self._raw_param["type"]
        self.required = self._raw_param["required"]
        if json_type_convert(self._raw_param["type"]):
            self.type = json_type_convert(self._raw_param["type"])
        self.name = self._raw_param["name"]
        self.safe_name = safe_name(self._raw_param["name"])
        self.is_primitive_type = bool(json_type_convert(self._raw_param["type"]))

    def get_parameter_str(self):
        if self.is_primitive_type:
            return self.type
        return f"Model{self.json_type}"
