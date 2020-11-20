
from helpers import get_py_type, safe_name


class ApiEndpoint:
    """
    Manages data and logic for working with an API class.

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

                if not get_py_type(op["type"]) and op["type"] not in self.imports:
                    self.imports.add(op["type"])

                self.operations.append(
                    Operation(
                        params, op_response_codes, op["type"],
                        op["nickname"], op["summary"], op["method"],
                        data["path"], op.get("produces", []))
                )


class Operation:
    """
    An operation contains all metadata for an API classes method.
    For example if the API endpoint defines a POST an Operation will track
    parameters it requires, response codes to expect, the method name,
    the type of return value etc.
    """

    def __init__(self, parameters=[], response_codes=[], op_type=None, nickname='', summary='', method='', api_path='', produces=[]):
        self.parameters = parameters
        self.response_codes = response_codes
        self.json_type = op_type
        self.type = op_type
        if get_py_type(op_type):
            self.type = get_py_type(op_type)
        self.is_primitive_type = bool(get_py_type(op_type))
        self.nickname = nickname
        self.summary = summary
        self.method = method
        self.api_path = api_path
        self.produces = produces

    def get_response_str(self):
        if get_py_type(self.json_type) not in ("", "None") and self.is_primitive_type:
            return f"{self.type}(response)"
        elif get_py_type(self.json_type) == "None":
            if "application/zip" in self.produces:
                return "response"
            else:
                return "response.json()"
        else:
            return f"Model{self.type}.from_dict(response.json())"

    def get_return_type_str(self):
        if self.type not in ("", "None") and self.is_primitive_type:
            return self.type
        elif self.type == "None":
            return "dict"
        return f"Model{self.json_type}"

    def get_api_path(self):
        l_paren = self.api_path.find("{") + 1
        r_paren = self.api_path.find("}") + 1
        if l_paren and r_paren and l_paren < r_paren:
            return f'f"{self.api_path}"'
        return f'"{self.api_path}"'


class Parameter:
    """
        A parameter is an argument to an operation, which when we generate
        our modules gets converted to an argument to an API method. This
        object is used to expose strong typing information in the class
        methods.
    """

    def __init__(self, param):
        self._raw_param = param
        self.json_type = self._raw_param["type"]
        self.type = self._raw_param["type"]
        self.required = self._raw_param["required"]
        if get_py_type(self._raw_param["type"]):
            self.type = get_py_type(self._raw_param["type"])
        self.name = self._raw_param["name"]
        self.safe_name = safe_name(self._raw_param["name"])
        self.is_primitive_type = bool(get_py_type(self._raw_param["type"]))

    def get_parameter_str(self):
        if self.is_primitive_type:
            return self.type
        return f"Model{self.json_type}"
