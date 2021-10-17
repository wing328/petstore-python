"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import petstore_api
from petstore_api.api.store_api import StoreApi  # noqa: E501


class TestStoreApi(unittest.TestCase):
    """StoreApi unit test stubs"""

    def setUp(self):
        self.api = StoreApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_order(self):
        """Test case for delete_order

        Delete purchase order by ID  # noqa: E501
        """
        pass

    def test_get_inventory(self):
        """Test case for get_inventory

        Returns pet inventories by status  # noqa: E501
        """
        pass

    def test_get_order_by_id(self):
        """Test case for get_order_by_id

        Find purchase order by ID  # noqa: E501
        """
        pass

    def test_place_order(self):
        """Test case for place_order

        Place an order for a pet  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()