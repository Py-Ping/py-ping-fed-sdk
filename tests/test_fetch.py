""" Tests for fetch.py """

from unittest import TestCase
from unittest.mock import patch, MagicMock, call
from fetch import Fetch


class TestFetch(TestCase):
    """ Tests for the Fetch class """

    @patch("fetch.os")
    @patch("fetch.logging")
    def setUp(self, logging_mock, os_mock):
        self.logging_mock = logging_mock.getLogger.return_value
        os_mock.path.dirname.return_value = "/dummy/path"
        self.fetch = Fetch("https://dummy.url/doc")

    @patch("fetch.Fetch.write_json")
    @patch("fetch.requests")
    def test_get_source(self, requests_mock, write_json_mock):
        self.fetch.get_source()

        requests_mock.get.assert_called_once_with(
            "https://dummy.url/doc",
            verify=False
        )
        requests_mock.get.return_value.json.assert_called_once_with()
        write_json_mock.assert_called_once_with(
            data=requests_mock.get.return_value.json.return_value,
            name="pf-admin-api", directory="./source/"
        )
        self.logging_mock.info.assert_called_once_with(
            "Successfully downloaded Ping Swagger document: "
            "https://dummy.url/doc"
        )

        requests_mock.get.side_effect = Exception("test exception")
        self.assertRaises(ConnectionError, self.fetch.get_source)
        self.logging_mock.error.assert_called_once_with(
            "Failed to download swagger from: "
            "https://dummy.url/doc with error test exception"
        )

    @patch("fetch.Fetch.get_source")
    @patch("fetch.Fetch.get_api_schema")
    def test_fetch(self, get_source_mock, get_api_schema_mock):

        self.assertEqual(
            self.fetch.fetch(),
            {
                "models": self.fetch.models,
                "apis": self.fetch.models,
                "enums": self.fetch.models
            }
        )

        get_source_mock.assert_called_once_with()
        get_api_schema_mock.assert_called_once_with()

    @patch("fetch.json")
    @patch("fetch.os")
    @patch("builtins.open")
    def test_write_json(self, open_mock, os_mock, json_mock):
        os_mock.path.join.return_value = '/some/test/directory'
        os_mock.path.exists.return_value = False
        write_handle_mock = MagicMock()
        open_mock.return_value.__enter__.return_value = write_handle_mock

        self.fetch.write_json({"test": "data"}, "newfile", "/test/directory")
        os_mock.makedirs.assert_called_once_with(
            os_mock.path.join.return_value
        )
        os_mock.path.join.assert_has_calls([
            call('/dummy/path', '/test/directory'),
            call('/dummy/path', '/some/test/directory/newfile.json')
        ])
        open_mock.assert_called_once_with(os_mock.path.join.return_value, "w")
        open_mock.return_value.__enter__.assert_called_once_with()

        write_handle_mock.write.assert_called_once_with(
            json_mock.dumps.return_value
        )

        json_mock.dumps.assert_called_once_with(
            {"test": "data"}, default=str, sort_keys=True,
            indent=4, separators=(",", ": ")
        )

        open_mock.reset_mock()
        os_mock.reset_mock()
        os_mock.path.exists.return_value = True
        self.fetch.write_json({"test": "data"}, "newfile")
        open_mock.assert_called_once_with(os_mock.path.join.return_value, "w")
        open_mock.return_value.__enter__.assert_called_once_with()
        os_mock.path.join.assert_has_calls([
            call('/dummy/path', './templates/resources/'),
            call('/dummy/path', '/some/test/directory/newfile.json')
        ])
        os_mock.makedirs.assert_not_called()

    @patch("fetch.json")
    @patch("fetch.os")
    @patch("builtins.open")
    def test_read_json(self, open_mock, os_mock, json_mock):

        self.assertEqual(
            self.fetch.read_json("file_name.test"),
            json_mock.loads.return_value
        )
        open_mock.assert_called_once_with(os_mock.path.join.return_value, "r")
        enter_mock = MagicMock()
        enter_mock = open_mock.return_value.__enter__
        enter_mock.assert_called_once_with()
        enter_mock.return_value.read.assert_called_once_with()
        json_mock.loads.assert_called_once_with(
            enter_mock.return_value.read.return_value
        )

        open_mock.side_effect = IOError
        self.assertFalse(
            self.fetch.read_json("another_file_name.test")
        )

    def test_get_api_imports(self):
        test_api_data = [{
            "operations": [
                {"type": "boolean"},
                {"type": "Penguin"},
                {"type": "integer"}
            ]
        }]

        self.assertEqual(
            self.fetch.get_api_imports(test_api_data),
            {"imports": {"Penguin"}, "details": test_api_data}
        )

        self.assertEqual(
            self.fetch.get_api_imports(
                [{"operations": []}]
            ),
            {"imports": set({}), "details": [{"operations": []}]}
        )

    def test_get_model_imports(self):
        test_model_data = {
            "properties": {
                "PenguinImport": {"$ref": "Penguin"},
                "DuckImport": {"type": "boolean", "enum": "dummy"},
                "PelicanImport": {"type": "array"},
                "IbisImport": {"$ref": "Ibis", "enum": ["bin", "tree", "air"]},
                "AnotherIbisImport": {
                    "$ref": "Ibis", "enum": ["bin", "tree", "snoot"]
                },
            }
        }
        self.assertEqual(
            self.fetch.get_model_imports(test_model_data),
            {"enums": {"Ibis"}, "models": {"Penguin"}}
        )

        self.logging_mock.warn.assert_called_once_with(
            "Found redefined enum type: Ibis original "
            "-> ['bin', 'tree', 'air'], new -> ['bin', 'tree', 'snoot']..."
        )

        self.assertEqual(
            self.fetch.get_model_imports({"properties": {}}),
            {"models": set(), "enums": set()}
        )

    @patch("fetch.Fetch.write_json")
    @patch("fetch.requests")
    @patch("fetch.Fetch.get_api_imports")
    @patch("fetch.Fetch.read_json")
    @patch("fetch.os")
    @patch("fetch.safe_name")
    def test_api_schema(
        self, safe_name_mock, os_mock, read_json_mock,
        get_api_imports_mock, requests_mock, write_json_mock
    ):

        self.fetch.ping_data = {}
        self.assertIsNone(self.fetch.get_api_schema())
        self.assertEqual(self.fetch.ping_data, {})
        self.assertEqual(self.fetch.models, {})
        self.assertEqual(self.fetch.apis, {})
        self.assertEqual(self.fetch.enums, {})

        self.fetch.ping_data = {
            "apis": [
                {"path": "have/a/penguin"},
                {"path": "have/a/pelican"}
            ]
        }

        safe_name_mock.side_effect = [
            "have_a_penguin", "have_a_penguin",
            "have_a_pelican", "have_a_pelican"
        ]
        os_mock.path.exists.side_effect = [True, False]

        read_json_mock.get.return_value = {
            "resourcePath": "test",
            "apis": [],
            "models": {}
        }
        side_effects = [
            {"imports": {"Penguin"}, "details": [{
                "operations": [
                    {"type": "boolean"},
                    {"type": "Penguin"},
                    {"type": "integer"}
                ]
            }]},
            {"imports": {"Pelican"}, "details": [{
                "operations": [
                    {"type": "array"},
                    {"type": "Pelican"},
                    {"type": "string"}
                ]
            }]},
        ]

        get_api_imports_mock.side_effect = side_effects

        requests_mock.get.return_value.json.return_value = {
            "models": {}
        }
        self.assertIsNone(self.fetch.get_api_schema())

        os_mock.path.exists.has_calls([
            call("/dummy/path/source/apis/have_a_penguin.json"),
            call("/dummy/path/source/apis/have_a_pelican.json")
        ])

        requests_mock.get.assert_called_once_with(
            "https://dummy.url/dochave/a/pelican", verify=False
        )
        self.assertEqual(
            self.fetch.ping_data,
            {"apis": [{"path": "have/a/penguin"}, {"path": "have/a/pelican"}]}
        )
        self.assertEqual(self.fetch.models, {})
        self.assertEqual(
            self.fetch.apis,
            {
                "have_a_penguin": side_effects[0],
                "have_a_pelican": side_effects[1]
            }
        )
        self.assertEqual(self.fetch.enums, {})
