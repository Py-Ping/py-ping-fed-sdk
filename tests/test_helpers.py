
from unittest import TestCase
from unittest.mock import patch, MagicMock, call
from helpers import safe_class_name, safe_name, safe_module_name, \
    ref_type_convert, json_type_convert, get_auth_session, \
    retry_with_backoff


class TestHelpers(TestCase):
    def test_safe_name(self):
        self.assertEqual(
            safe_name("test/string"),
            "test_string"
        )
        self.assertEqual(
            safe_name("teststring"),
            "teststring"
        )
        self.assertEqual(
            safe_name("test_string"),
            "test_string"
        )

    def test_safe_module_name(self):
        self.assertEqual(
            safe_module_name("test_snakeWithCamelCaseString"),
            "test_snake_with_camel_case_string"
        )
        self.assertEqual(
            safe_module_name("CamelCaseString"),
            "camel_case_string"
        )

    def test_safe_class_name(self):
        self.assertEqual(
            safe_class_name("/test/apiClassName"),
            "TestApiClassName"
        )
        self.assertEqual(
            safe_class_name("/oauth/resourceOwnerCredentialsMappings"),
            "OauthResourceOwnerCredentialsMappings"
        )

    def test_ref_type_convert(self):
        self.assertEqual(
            ref_type_convert(
                {"$ref": "Map[string, SomeClass]"}
            ),
            "dict"
        )
        self.assertEqual(
            ref_type_convert(
                {"$ref": "SomeClass"}
            ),
            "SomeClass"
        )

    def test_json_type_convert(self):
        self.assertEqual(
            json_type_convert("enum"),
            "str"
        )
        self.assertEqual(
            json_type_convert("string"),
            "str"
        )
        self.assertEqual(
            json_type_convert("boolean"),
            "bool"
        )
        self.assertEqual(
            json_type_convert("array"),
            "list"
        )
        self.assertEqual(
            json_type_convert("integer"),
            "int"
        )
        self.assertEqual(
            json_type_convert("notatype"),
            ""
        )

    @patch("helpers.HTTPBasicAuth")
    @patch("helpers.requests")
    @patch("helpers.os")
    def test_get_auth_session(
        self, os_mock, requests_mock, http_basic_auth_mock
    ):
        self.assertEqual(
            get_auth_session(),
            requests_mock.Session.return_value
        )

        self.assertEqual(
            requests_mock.Session.return_value.auth,
            http_basic_auth_mock.return_value
        )

        self.assertEqual(
            requests_mock.Session.return_value.headers,
            {
                "Accept": "application/json",
                "X-Xsrf-Header": "PingFederate"
            }
        )

        os_mock.environ.get.assert_has_calls([
            call(
                "PING_IDENTITY_DEVOPS_ADMINISTRATOR", "administrator"
            ),
            call(
                "PING_IDENTITY_DEVOPS_PASSWORD", "2FederateM0re"
            )
        ])

        requests_mock.Session.assert_called_once_with()

        http_basic_auth_mock.assert_called_once_with(
            os_mock.environ.get.return_value,
            os_mock.environ.get.return_value
        )

    @patch("helpers.print")
    @patch("helpers.sleep")
    def test_retry_with_backoff(self, sleep_mock, print_mock):

        self.assertTrue(
            retry_with_backoff(MagicMock)
        )

        error_mock = MagicMock()
        error_mock.side_effect = Exception('test except')
        self.assertFalse(
            retry_with_backoff(error_mock)
        )

        error_mock = MagicMock()
        error_mock.side_effect = [Exception('test except'), None]
        self.assertTrue(
            retry_with_backoff(error_mock)
        )
