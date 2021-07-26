""" Tests for generate.py """

import os

from unittest import TestCase
from unittest.mock import patch, MagicMock
from generate import Generate
from property import Property
from api import ApiEndpoint

REAL_PATH = os.path.realpath(__file__)


def wipe_test_fixtures():
    test_files = f"{os.path.dirname(__file__)}/../pingfedsdk"
    wipe_files = (
        f"{test_files}/models/Penguin.py",
        f"{test_files}/models/Penguins.py",
        f"{test_files}/models/PenguinLabeller.py",
        f"{test_files}/apis/penguins.py",
    )
    for filepath in wipe_files:
        try:
            os.remove(filepath)
        except FileNotFoundError:
            pass


class TestGenerate(TestCase):
    """ Tests for the Generate class """

    @patch("generate.os.path.realpath")
    @patch("generate.Fetch")
    def setUp(self, fetch_mock, realpath_mock):
        wipe_test_fixtures()

        self.fetch_response = {
            "apis": {
                "/penguins": {
                    "imports": set(["Penguin"]),
                    "codes": {200, 404},
                    "details": [{
                        "operations": [
                            {
                                "method": "GET",
                                "nickname": "getPenguinDetails",
                                "notes": "",
                                "parameters": [],
                                "responseMessages": [
                                    {
                                        "code": 200,
                                        "message": "Success."
                                    }
                                ],
                                "summary":
                                "Retrieve list of available penguins.",
                                "type": "Penguin"
                            },
                            {
                                "method": "POST",
                                "nickname": "addPenguin",
                                "notes": "",
                                "parameters": [
                                    {
                                        "allowMultiple": False,
                                        "description": "Penguin description.",
                                        "name": "body",
                                        "height": "string",
                                        "required": True,
                                        "type": "Penguin"
                                    }
                                ],
                                "responseMessages": [
                                    {
                                        "code": 200,
                                        "message": "Penguin uploaded."
                                    },
                                    {
                                        "code": 404,
                                        "message":
                                        "Validation error(s) occurred."
                                    }
                                ],
                                "summary": "Add a new penguin.",
                                "type": "Penguin"
                            }
                        ],
                        "path": "/penguins"
                    }]
                }
            },
            "enums": {},
            "models": {
                "PenguinLabeller": {
                    "api_references": ["penguins"],
                    "description": "Labels penguins.",
                    "id": "PenguinLabeller",
                    "properties": {
                        "PenguinNames": Property({
                            "description":
                            "List of great names for a pet penguin.",
                            "items": {
                                "type": "string"
                            },
                            "type": "array"
                        }, property_name="PenguinNames")
                    },
                    "imports": {}
                },
                "Penguin": {
                    "api_references": ["penguins"],
                    "description": "The details of a penguin.",
                    "id": "BestPenguin",
                    "properties": {
                        "firstName": Property({
                            "description": "The penguins first name.",
                            "type": "string"
                        }, property_name="firstName"),
                        "lastName": Property({
                            "description": "The penguins last name.",
                            "type": "string"
                        }, property_name="lastName"),
                        "height": Property({
                            "description": "Height of the penguin.",
                            "type": "string"
                        }, property_name="height"),
                        "soundMade": Property({
                            "description": "List of sounds made.",
                            "type": "string"
                        }, property_name="soundMade")
                    },
                    "imports": {}
                },
                "Penguins": {
                    "api_references": ["penguins"],
                    "description": "A collection of penguins.",
                    "id": "Penguins",
                    "properties": {
                        "items": Property({
                            "description": "The actual list of penguins.",
                            "items": {
                                "$ref": "Penguin"
                            },
                            "type": "array"
                        }, property_name="items")
                    },
                    "imports": {}
                }
            }
        }
        for api, api_data in self.fetch_response['apis'].items():
            self.fetch_response['apis'][api] = ApiEndpoint(
                '/test/endpoint', self.fetch_response['apis'][api]['details']
            )
        fetch_mock.return_value.fetch.return_value = self.fetch_response
        realpath_mock.return_value = REAL_PATH
        Generate("fake-url.com:9999").generate()
        self.penguin_dict = {
            "firstName": "terrence",
            "lastName": "mcflappy",
            "height": "1.42",
            "soundMade": "honk"
        }

    def test_model(self):
        """
            Dynamically import the created model module, instantiate the class
            and make some assertions about the object state
        """
        penguin = __import__("pingfedsdk.models.penguin", fromlist=[""])
        penguin_inst = penguin.Penguin()
        self.assertEqual(
            hash(penguin_inst), hash(frozenset([None, None, None, None]))
        )
        self.assertTrue(penguin_inst == penguin_inst)
        self.assertEqual(
            str(penguin_inst),
            "{'firstName': None, 'lastName': None, "
            "'height': None, 'soundMade': None}"
        )

        self.assertEqual(penguin.Penguin().from_dict(
            self.penguin_dict
        ), penguin.Penguin(**self.penguin_dict))

        self.assertEqual(
            self.penguin_dict,
            penguin.Penguin(**self.penguin_dict).to_dict()
        )

        self.assertEqual(
            hash(penguin.Penguin(**self.penguin_dict)),
            hash(frozenset(["terrence", "mcflappy", "1.42", "honk"]))
        )

    @patch("pingfedsdk.apis.penguins.ModelPenguin")
    @patch("pingfedsdk.apis.penguins.logging")
    @patch("pingfedsdk.apis.penguins.Session")
    def test_api(self, session_mock, logging_mock, penguin_mock):
        """
            Dynamically import the created api module, instantiate the class
            and make some assertions about the object methods
        """
        penguins = __import__("pingfedsdk.apis.penguins", fromlist=[""])
        penguin = __import__("pingfedsdk.models.penguin", fromlist=[""])
        session_mock = MagicMock()
        penguin_api = penguins.Penguins("test-endpoint", session_mock)
        self.assertEqual(
            penguin_api.addPenguin(penguin.Penguin().from_dict(
                self.penguin_dict
            )),
            penguin_mock.from_dict.return_value
        )

        self.assertEqual(
            penguin_api.getPenguinDetails(),
            penguin_mock.from_dict.return_value
        )

    def tearDown(self):
        wipe_test_fixtures()
