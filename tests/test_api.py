""" Tests for api.py """

from unittest import TestCase
from api import ApiEndpoint


class TestApi(TestCase):
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
                    "parameters": [{"name": "id", "type": "integer"}],
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
                        {"name": "id", "type": "integer"},
                        {"name": "choice", "type": "enum"}
                    ],
                    "nickname": "doThing", "summary": "does something", "method": "PUT"
                }
            ],
            "path": "/test/path/{id}"
        }])

        self.assertEqual(api_endpoint.imports, {"Penguin"})
        self.assertEqual(api_endpoint.response_codes, {200, 403, 422, 201})
