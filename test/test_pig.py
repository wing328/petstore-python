"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import petstore_api
from petstore_api.model.basque_pig import BasquePig
from petstore_api.model.danish_pig import DanishPig
globals()['BasquePig'] = BasquePig
globals()['DanishPig'] = DanishPig
from petstore_api.model.pig import Pig


class TestPig(unittest.TestCase):
    """Pig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPig(self):
        """Test Pig"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Pig()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
