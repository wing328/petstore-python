# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.order import Order


class TestOrder(unittest.TestCase):
    """Order unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrder(self):
        """Test Order"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Order()  # noqa: E501
        print("Current value of the recursion limit:")
        print(sys.getrecursionlimit())
        #pass


if __name__ == '__main__':
    unittest.main()
