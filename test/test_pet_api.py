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
from openapi_client.api.pet_api import PetApi  # noqa: E501


class TestPetApi(unittest.TestCase):
    """PetApi unit test stubs"""

    def setUp(self):
        self.api = PetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_pet(self):
        """Test case for add_pet

        Add a new pet to the store  # noqa: E501
        """
        pass

    def test_delete_pet(self):
        """Test case for delete_pet

        Deletes a pet  # noqa: E501
        """
        pass

    def test_find_pets_by_status(self):
        """Test case for find_pets_by_status

        Finds Pets by status  # noqa: E501
        """
        pass

    def test_find_pets_by_tags(self):
        """Test case for find_pets_by_tags

        Finds Pets by tags  # noqa: E501
        """
        pass

    def test_get_pet_by_id(self):
        """Test case for get_pet_by_id

        Find pet by ID  # noqa: E501
        """
        pass

    def test_update_pet(self):
        """Test case for update_pet

        Update an existing pet  # noqa: E501
        """
        pass

    def test_update_pet_with_form(self):
        """Test case for update_pet_with_form

        Updates a pet in the store with form data  # noqa: E501
        """
        pass

    def test_upload_file(self):
        """Test case for upload_file

        uploads an image  # noqa: E501
        """
        print("Current value of the recursion limit:")
        print(sys.getrecursionlimit())
        pass


if __name__ == '__main__':
    unittest.main()
