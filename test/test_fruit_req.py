"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import petstore_api
from petstore_api.model.apple_req import AppleReq
from petstore_api.model.banana_req import BananaReq
globals()['AppleReq'] = AppleReq
globals()['BananaReq'] = BananaReq
from petstore_api.model.fruit_req import FruitReq


class TestFruitReq(unittest.TestCase):
    """FruitReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFruitReq(self):
        """Test FruitReq"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FruitReq()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
