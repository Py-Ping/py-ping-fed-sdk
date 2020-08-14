""" Tests for generate.py """

import os
import shutil

from unittest import TestCase
from unittest.mock import patch, Mock, MagicMock
from generate import Generate

REAL_PATH = os.path.realpath(__file__)


class TestGenerate(TestCase):
    """ Tests for the Generate class """

    @patch("generate.os.path.realpath")
    @patch("generate.Fetch")
    def setUp(self, fetch_mock, realpath_mock):
        test_directory = os.path.dirname(__file__)

        try:
            shutil.rmtree(f"{test_directory}/apis")
        except FileNotFoundError:
            pass
        try:
            shutil.rmtree(f"{test_directory}/models")
        except FileNotFoundError:
            pass

        self.fetch_response = {
            "apis": {
                "_penguins": [{
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
                            "summary": "Retrieve list of available penguins.",
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
                                    "message": "Validation error(s) occurred."
                                }
                            ],
                            "summary": "Add a new penguin.",
                            "type": "Penguin"
                        }
                    ],
                    "path": "/penguins"
                }],
                
            },
            "models": {
                "PenguinLabeller": {
                    "description": "Labels penguins.",
                    "id": "PenguinLabeller",
                    "properties": {
                        "PenguinNames": {
                            "description": "List of great names for a pet penguin.",
                            "items": {
                                "type": "string"
                            },
                            "type": "array"
                        }
                    }
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
                    }
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
                    }
                }
            }
        }
        fetch_mock.return_value.fetch.return_value = self.fetch_response

        realpath_mock.return_value = REAL_PATH
        Generate("fake-url.com:9999").generate()

    def test_model(self):
        """
            Dynamically import the created model module, instantiate the class
            and make some assertions about the object state
        """
        Penguin = __import__("models.Penguin", fromlist=[""])
        penguin_inst = Penguin.Penguin()
        self.assertEqual(
            hash(penguin_inst), hash(frozenset([None, None, None, None]))
        )
        self.assertTrue(penguin_inst == penguin_inst)
        self.assertEqual(
            str(penguin_inst),
            "{'firstName': None, 'lastName': None, 'height': None, 'soundMade': None}"
        )

        penguin_dict = {
            "firstName": "terrence",
            "lastName": "mcflappy",
            "height": "1.42",
            "soundMade": "honk"
        }
        self.assertEqual(Penguin.Penguin().from_dict(
            penguin_dict
        ), Penguin.Penguin(**penguin_dict))
        self.assertEqual(
            hash(Penguin.Penguin(**penguin_dict)), hash(frozenset(["terrence", "mcflappy", "1.42", "honk"]))
        )

    @patch("apis._penguins.Penguin")
    @patch("apis._penguins.logging")
    @patch("apis._penguins.Session")
    def test_api(self, requests_mock, logging_mock, penguin_mock):
        """
            Dynamically import the created api module, instantiate the class
            and make some assertions about the object methods
        """
        self.maxDiff = None
        penguins = __import__("apis._penguins", fromlist=[""])
        session_mock = MagicMock()
        penguin_api = penguins._penguins("test-endpoint", session_mock)
        self.assertEqual(
            penguin_api.addPenguin("philip"),
            penguin_mock.return_value
        )

        self.assertEqual(
            penguin_api.getPenguinDetails(),
            penguin_mock.return_value
        )