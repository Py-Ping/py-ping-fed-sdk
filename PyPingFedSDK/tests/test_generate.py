""" Tests for generate.py """

import os

from unittest import TestCase
from unittest.mock import patch, Mock
from generate import Generate

REAL_PATH = os.path.realpath(__file__)


class TestGenerate(TestCase):
    """ Tests for the Generate class """

    @patch('apis._penguins.requests')
    @patch('apis._penguins.logging')
    @patch('generate.os.path.realpath')
    @patch('generate.Fetch')
    def test_generation(self, fetch_mock, realpath_mock, logging_mock, requests_mock):
        fetch_mock.return_value.fetch.return_value = {
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
                }
            }
        }
        penguin_dict = {
            "firstName": "terrence",
            "lastName": "mcflappy",
            "height": "1.42",
            "soundMade": "honk"
        }
        realpath_mock.return_value = REAL_PATH
        generate = Generate("fake-url.com:9999").generate()

        Penguin = __import__("models.Penguin", fromlist=[""])
        penguin_inst = Penguin.Penguin()
        self.assertEqual(
            hash(penguin_inst), 6555679905594400944
        )
        self.assertTrue(penguin_inst == penguin_inst)
        self.assertEqual(
            str(penguin_inst),
            "{'firstName': None, 'lastName': None, 'height': None, 'soundMade': None}"
        )
        self.assertEqual(Penguin.Penguin().from_dict(
            penguin_dict
        ), Penguin.Penguin(**penguin_dict))

        penguins = __import__("apis._penguins", fromlist=[""])

        penguin_api = penguins._penguins("test-endpoint")
        self.assertEqual(
            penguin_api.addPenguin('philip'),
            requests_mock.post.return_value
        )

        self.assertEqual(
            penguin_api.getPenguinDetails(),
            requests_mock.get.return_value
        )