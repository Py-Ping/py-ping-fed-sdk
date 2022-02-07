
from helpers import get_py_type, safe_name


class ApiEndpoint:
    """
    Manages data and logic for working with an API class.

    This was created to take out as much logic as possible from
    the Jinja template and make it compatible with Python native
    Dynamic classes.

    - v11 boolean: If this is true the dictionary will be parsed
        following a swagger 2.0 format. Response codes can have
        different return types.
    """

    def __init__(self, api_path, api_data, v11=False):
        self.api_data = api_data
        self.safe_api_path = safe_name(api_path)
        self.path = api_path
        self.response_codes = set()
        self.imports = set()
        self.operations = []
        if v11:
            self._process_v11()
        else:
            self._process()

    def _process_v11(self):
        """
        Process for how to interpret an API endpoint in Ping Fed v11+
        1. get the dict and read the rest method/method data
        2. extract method input parameters and determine if their type will need to be imported
        3. construct the method response types by HTTP response code (responses may have different schemas)
        4. build out the operation object
        """
        for rest_method, rest_data in self.api_data.items():
            params = []
            for param in rest_data["parameters"]:
                param_obj = Parameter(param)
                params.append(param_obj)
                if not param_obj.is_primitive_type and param_obj.type not in self.imports:
                    self.imports.add(param_obj.type)

            op_response_codes = []
            for response_code, response_data in rest_data["responses"].items():
                op_code = {"code": response_code, "message": response_data["description"]}
                if "schema" in response_data and "$ref" in response_data["schema"]:
                    op_code["type"] = response_data["schema"]["$ref"].split("/")[-1]
                op_response_codes.append(op_code)
                if response_code not in self.response_codes:
                    self.response_codes.add(response_code)

                if "type" in op_code and not get_py_type(op_code["type"]) and op_code["type"] not in self.imports:
                    self.imports.add(op_code["type"])

            self.operations.append(
                Operation(
                    params, op_response_codes, None,
                    rest_data["operationId"], rest_data["summary"], rest_method,
                    self.path, rest_data.get("produces", []))
            )

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

    def get_exception_imports(self):
        exception_import_block = ""
        for response_code in self.response_codes:
            if self.get_exception_by_code(response_code) and response_code not in (204, 403):
                if exception_import_block:
                    exception_import_block += "\n"
                exception_type = self.get_exception_by_code(response_code)
                exception_import_block += f"from pingfedsdk.exceptions import {exception_type}"

        if 'ApiResult' not in self.imports and 422 in self.response_codes:
            exception_import_block += "\nfrom pingfedsdk.models.api_result import ApiResult as ModelApiResult"
        return exception_import_block

    def get_exception_by_code(self, http_response_code):
        if http_response_code == 204:
            return "ObjectDeleted"
        elif http_response_code == 400:
            return "BadRequest"
        elif http_response_code == 403:
            return "NotImplementedError"
        elif http_response_code == 404:
            return "NotFound"
        elif http_response_code == 422:
            return "ValidationError"
        elif http_response_code == 500:
            return "ServerError"


class Operation:
    """
    An operation contains all metadata for an API classes method.
    For example if the API endpoint defines a POST an Operation will track
    parameters it requires, response codes to expect, the method name,
    the type of return value etc.
    """

    def __init__(self, parameters=[], response_codes=[], op_type=None, nickname='',
                 summary='', method='', api_path='', produces=[]):
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

    def get_response_str(self, code=None):

        # case to handle v11 Ping Fed, operations can return different response objects
        # dependent on the HTTP response code
        if code is not None and self.json_type is None:
            for response_code in self.response_codes:
                if response_code["code"] == code and "type" in response_code:
                    return f"Model{response_code['type']}.from_dict(response.json())"

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
        if "schema" in self._raw_param:
            self.json_type = self._raw_param["schema"]["$ref"].split("/")[-1]
            self.type = self.json_type
            self.is_primitive_type = False
        elif "type" in self._raw_param:
            self.json_type = self._raw_param["type"]
            self.type = self._raw_param["type"]
            self.is_primitive_type = bool(get_py_type(self._raw_param["type"]))

        if get_py_type(self.type):
            self.type = get_py_type(self.type)

        self.required = self._raw_param["required"]
        self.name = self._raw_param["name"]
        self.safe_name = safe_name(self._raw_param["name"])

    def get_parameter_str(self):
        if self.is_primitive_type:
            return self.type
        return f"Model{self.json_type}"
