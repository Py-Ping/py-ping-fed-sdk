
from unittest import TestCase
from unittest.mock import patch, MagicMock, call
from helpers import safe_class_name, safe_name, safe_module_name, \
    get_py_type, get_auth_session, retry_with_backoff


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

    def test_get_py_type(self):
        self.assertEqual(
            get_py_type("enum"),
            "str"
        )
        self.assertEqual(
            get_py_type("string"),
            "str"
        )
        self.assertEqual(
            get_py_type("boolean"),
            "bool"
        )
        self.assertEqual(
            get_py_type("array"),
            "list"
        )
        self.assertEqual(
            get_py_type("integer"),
            "int"
        )
        self.assertEqual(
            get_py_type("int"),
            "int"
        )
        self.assertEqual(
            get_py_type("number"),
            "float"
        )
        self.assertEqual(
            get_py_type("notatype"),
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
                "X-XSRF-Header": "PingFederate"
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
