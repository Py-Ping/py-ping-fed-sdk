""" Tests for api.py """

from unittest import TestCase
from api import ApiEndpoint, Operation, Parameter


class TestApiEndpoint(TestCase):
    """ Tests for the Fetch class """

    def test_api_endpoint(self):
        api_endpoint = ApiEndpoint('/test/path', [{
            "operations": [
                {
                    "type": "boolean",
                    "responseMessages": [
                        {"code": 200, "message": "test"},
                        {"code": 403, "message": "again"}
                    ],
                    "parameters": [{"name": "id", "type": "integer", "required": "true"}],
                    "nickname": "doThis", "summary": "does this", "method": "POST"
                },
                {
                    "type": "Penguin", "responseMessages": [
                        {"code": 200, "message": "one"},
                        {"code": 422, "message": "two"}
                    ],
                    "parameters": [], "nickname": "doThat", "summary": "does that", "method": "GET"
                },
                {
                    "type": "integer", "responseMessages": [
                        {"code": 200, "message": "three"},
                        {"code": 201, "message": "four"}
                    ],
                    "parameters": [
                        {"name": "id", "type": "integer", "required": "true"},
                        {"name": "choice", "type": "enum", "required": "false"}
                    ],
                    "nickname": "doThing", "summary": "does something", "method": "PUT"
                }
            ],
            "path": "/test/path/{id}"
        }])

        self.assertEqual(api_endpoint.imports, {"Penguin"})
        self.assertEqual(api_endpoint.response_codes, {200, 403, 422, 201})


class TestParameter(TestCase):
    def test_param(self):
        test = Parameter({"type": "string", "name": "testparameter", "required": "true"})
        self.assertEqual(test.get_parameter_str(), "str")
        self.assertEqual(test.json_type, "string")
        self.assertTrue(test.is_primitive_type)

        test = Parameter({"type": "TestModel", "name": "anothertestparameter", "required": "false"})
        self.assertEqual(test.get_parameter_str(), "ModelTestModel")
        self.assertEqual(test.json_type, "TestModel")
        self.assertFalse(test.is_primitive_type)


class TestOperation(TestCase):
    def setUp(self):
        self.op_test = Operation(
            parameters=[
                Parameter({"type": "string", "name": "one", "required": "true"}),
                Parameter({"type": "TestModel", "name": "two", "required": "false"}),
            ],
            response_codes=[
                {"code": 200, "message": "Operation success"},
                {"code": 422, "message": "Bad media"},
            ],
            op_type="boolean",
            nickname="TestCode",
            summary="This operation literally tests the code",
            method="GET",
            api_path="/test/code"
        )
        self.op_test_none = Operation(
            parameters=[
                Parameter({"type": "bool", "name": "three", "required": "true"}),
                Parameter({"type": "array", "name": "four", "required": "false"}),
            ],
            response_codes=[
                {"code": 200, "message": "Operation success"},
                {"code": 404, "message": "Not Found"},
            ],
            op_type="void",
            nickname="TestMore",
            summary="This operation literally tests the code",
            method="POST",
            api_path="/test/code"
        )
        self.op_test_model = Operation(
            parameters=[],
            response_codes=[
                {"code": 200, "message": "Operation success"},
                {"code": 404, "message": "Not Found"},
            ],
            op_type="TestModel",
            nickname="AnotherTest",
            summary="This operation literally tests the code",
            method="PUT",
            api_path="/test/code"
        )

    def test_get_response_str(self):
        self.assertEqual(self.op_test.get_response_str(), 'bool(response)')
        self.assertEqual(self.op_test_none.get_response_str(), 'response.json()')
        self.assertEqual(
            self.op_test_model.get_response_str(),
            "ModelTestModel.from_dict(response.json())"
        )

    def test_get_return_type_str(self):
        self.assertEqual(self.op_test.get_return_type_str(), 'bool')
        self.assertEqual(self.op_test_none.get_return_type_str(), 'dict')
        self.assertEqual(self.op_test_model.get_return_type_str(), 'ModelTestModel')
