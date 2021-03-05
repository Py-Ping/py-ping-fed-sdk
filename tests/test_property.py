""" Tests for property.py """

from unittest import TestCase
from property import Property


class TestProperty(TestCase):
    """ Tests for the Property class """

    def setUp(self):
        self.array_example = Property({
            "description": "A list of penguins.",
            "items": {
                "$ref": "Penguin"
            },
            "type": "array"
        }, 'Penguins', 'items')

        self.array_enum_example = Property({
            "description": "A list of penguin traits.",
            "items": {
                "enum": [
                    "HUNGRY",
                    "TIRED",
                    "IRATE",
                    "PINING"
                ],
                "$ref": "PenguinState"
            },
            "type": "array"
        }, 'Penguins', 'items')

        self.array_primitive_example = Property({
            "description": "A list of penguin dimensions.",
            "items": {
                "type": "number"
            },
            "type": "array"
        })

        self.model_example = Property({
            "$ref": "Penguin",
            "description": "The penguin of the hour."
        }, 'Penguins', 'a_penguin')

        self.str_example = Property({
            "$ref": "string",
            "description": "A penguins name."
        }, 'Penguin', 'penguin_name')

        self.dict_example = Property({
            "$ref": "Map[string,Penguin]",
            "description": "The boys"
        })

        self.set_example = Property({
            "$ref": "Set",
            "description": "A group of penguins names",
            "items": {"type": "string"}
        })

        self.set_enum_example = Property({
            "$ref": "Set",
            "description": "A bunch of states a penguin can be in",
            "items": {
                "$ref": "PenguinStates",
                "enum": [
                    "HUNGRY",
                    "TIRED",
                    "IRATE",
                    "PINING"
                ]
            }
        })

        self.enum_example = Property({
            "$ref": "PenguinCurrentState",
            "description": "How the penguin feels right now",
            "enum": [
                "HUNGRY",
                "TIRED",
                "IRATE",
                "PINING"
            ]
        })

    def test_process(self):
        self.assertEqual(
            self.array_example.get_model_import(),
            "Penguin"
        )

        self.assertIsNone(self.array_example.get_enum_import())

        self.assertIsNone(self.str_example.get_model_import())
        self.assertIsNone(self.str_example.get_enum_import())

        self.assertIsNone(
            self.enum_example.get_model_import()
        )
        self.assertEqual(
            self.enum_example.get_enum_import(),
            "PenguinCurrentState"
        )
        self.assertIsNone(
            self.set_enum_example.get_model_import()
        )
        self.assertEqual(
            self.set_enum_example.get_enum_import(),
            "PenguinStates"
        )

        self.assertEqual(
            self.model_example.get_model_import(),
            "Penguin"
        )

        self.assertIsNone(
            self.model_example.get_enum_import()
        )

        self.assertEqual(
            self.dict_example.get_model_import(),
            "Penguin"
        )

        self.assertIsNone(
            self.dict_example.get_enum_import()
        )

        self.assertIsNone(
            self.set_example.get_enum_import()
        )

        self.assertIsNone(
            self.set_example.get_model_import()
        )

        self.assertIsNone(
            self.array_enum_example.get_model_import()
        )

        self.assertEqual(
            self.array_enum_example.get_enum_import(),
            "PenguinState"
        )

        self.assertIsNone(self.array_primitive_example.get_enum_import())
        self.assertIsNone(self.array_primitive_example.get_model_import())
