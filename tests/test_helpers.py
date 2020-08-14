
from unittest import TestCase
from unittest.mock import patch, Mock, MagicMock
from helpers import safe_name


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
