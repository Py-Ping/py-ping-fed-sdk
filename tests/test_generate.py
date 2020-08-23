""" Tests for generate.py """

import os

from unittest import TestCase
from unittest.mock import patch, MagicMock
from generate import Generate


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
                "_penguins": {
                    "imports": set(["Penguin"]),
                    "codes": {200, 422},
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
                                        "name": "firstName",
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
                                        "code": 422,
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
                    "description": "Labels penguins.",
                    "id": "PenguinLabeller",
                    "properties": {
                        "PenguinNames": {
                            "description":
                            "List of great names for a pet penguin.",
                            "items": {
                                "type": "string"
                            },
                            "type": "array"
                        }
                    },
                    "imports": {}
                },
                "Penguin": {
                    "description": "The details of a penguin.",
                    "id": "BestPenguin",
                    "properties": {
                        "firstName": {
                            "description": "The penguins first name.",
                            "type": "string"
                        },
                        "lastName": {
                            "description": "The penguins last name.",
                            "type": "string"
                        },
                        "height": {
                            "description": "Height of the penguin.",
                            "type": "string"
                        },
                        "soundMade": {
                            "description": "List of sounds made.",
                            "type": "string"
                        }
                    },
                    "imports": {}
                },
                "Penguins": {
                    "description": "A collection of penguins.",
                    "id": "Penguins",
                    "properties": {
                        "items": {
                            "description": "The actual list of penguins.",
                            "items": {
                                "$ref": "Penguin"
                            },
                            "type": "array"
                        }
                    },
                    "imports": {}
                }
            }
        }
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
        Penguin = __import__("pingfedsdk.models.Penguin", fromlist=[""])
        penguin_inst = Penguin.Penguin()
        self.assertEqual(
            hash(penguin_inst), hash(frozenset([None, None, None, None]))
        )
        self.assertTrue(penguin_inst == penguin_inst)
        self.assertEqual(
            str(penguin_inst),
            "{'firstName': None, 'lastName': None, "
            "'height': None, 'soundMade': None}"
        )

        self.assertEqual(Penguin.Penguin().from_dict(
            self.penguin_dict
        ), Penguin.Penguin(**self.penguin_dict))

        self.assertEqual(
            self.penguin_dict,
            Penguin.Penguin(**self.penguin_dict).to_dict()
        )

        self.assertEqual(
            hash(Penguin.Penguin(**self.penguin_dict)),
            hash(frozenset(["terrence", "mcflappy", "1.42", "honk"]))
        )

    @patch("pingfedsdk.apis.penguins.Penguin")
    @patch("pingfedsdk.apis.penguins.logging")
    @patch("pingfedsdk.apis.penguins.Session")
    def test_api(self, session_mock, logging_mock, penguin_mock):
        """
            Dynamically import the created api module, instantiate the class
            and make some assertions about the object methods
        """
        penguins = __import__("pingfedsdk.apis.penguins", fromlist=[""])
        Penguin = __import__("pingfedsdk.models.Penguin", fromlist=[""])
        session_mock = MagicMock()
        penguin_api = penguins.penguins("test-endpoint", session_mock)
        self.assertEqual(
            penguin_api.addPenguin(Penguin.Penguin().from_dict(
                self.penguin_dict
            )),
            penguin_mock.return_value
        )

        self.assertEqual(
            penguin_api.getPenguinDetails(),
            penguin_mock.return_value
        )

    def tearDown(self):
        wipe_test_fixtures()
