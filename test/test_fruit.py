"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import petstore_api
from petstore_api.model.apple import Apple
from petstore_api.model.banana import Banana
globals()['Apple'] = Apple
globals()['Banana'] = Banana
from petstore_api.model.fruit import Fruit


class TestFruit(unittest.TestCase):
    """Fruit unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFruit(self):
        """Test Fruit"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Fruit()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()