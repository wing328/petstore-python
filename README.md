# swagger_client
This is a sample server Petstore server.  You can find out more about Swagger at <a href=\"http://swagger.io\">http://swagger.io</a> or on irc.freenode.net, #swagger.  For this sample, you can use the api key \"special-key\" to test the authorization filters

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API verion: 1.0.0
- Package version: 
- Build date: 2016-03-30T16:40:30.719+08:00
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/wing328/petstore-python.git
```

Import the pacakge:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Import the pacakge:
```python
import swagger_client
```

### Manual Installation

Download the latest release to the project folder (e.g. ./path/to/swagger_client) and import the package:

```python
import path.to.swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: petstore_auth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

api_instance = swagger_client.PetApi
body = swagger_client.Pet() # Pet | Pet object that needs to be added to the store (optional)

try:
    # Add a new pet to the store
    api_instance.add_pet(body=body);
except ApiException as e:
    print "Exception when calling PetApi->add_pet: {e}\n";

```

## Documentation for API Endpoints

All URIs are relative to *http://petstore.swagger.io/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*PetApi* | [**add_pet**](docs/PetApi.md#add_pet) | **POST** /pet | Add a new pet to the store
*PetApi* | [**add_pet_using_byte_array**](docs/PetApi.md#add_pet_using_byte_array) | **POST** /pet?testing_byte_array=true | Fake endpoint to test byte array in body parameter for adding a new pet to the store
*PetApi* | [**delete_pet**](docs/PetApi.md#delete_pet) | **DELETE** /pet/{petId} | Deletes a pet
*PetApi* | [**find_pets_by_status**](docs/PetApi.md#find_pets_by_status) | **GET** /pet/findByStatus | Finds Pets by status
*PetApi* | [**find_pets_by_tags**](docs/PetApi.md#find_pets_by_tags) | **GET** /pet/findByTags | Finds Pets by tags
*PetApi* | [**get_pet_by_id**](docs/PetApi.md#get_pet_by_id) | **GET** /pet/{petId} | Find pet by ID
*PetApi* | [**get_pet_by_id_in_object**](docs/PetApi.md#get_pet_by_id_in_object) | **GET** /pet/{petId}?response=inline_arbitrary_object | Fake endpoint to test inline arbitrary object return by &#39;Find pet by ID&#39;
*PetApi* | [**pet_pet_idtesting_byte_arraytrue_get**](docs/PetApi.md#pet_pet_idtesting_byte_arraytrue_get) | **GET** /pet/{petId}?testing_byte_array=true | Fake endpoint to test byte array return by &#39;Find pet by ID&#39;
*PetApi* | [**update_pet**](docs/PetApi.md#update_pet) | **PUT** /pet | Update an existing pet
*PetApi* | [**update_pet_with_form**](docs/PetApi.md#update_pet_with_form) | **POST** /pet/{petId} | Updates a pet in the store with form data
*PetApi* | [**upload_file**](docs/PetApi.md#upload_file) | **POST** /pet/{petId}/uploadImage | uploads an image
*StoreApi* | [**delete_order**](docs/StoreApi.md#delete_order) | **DELETE** /store/order/{orderId} | Delete purchase order by ID
*StoreApi* | [**find_orders_by_status**](docs/StoreApi.md#find_orders_by_status) | **GET** /store/findByStatus | Finds orders by status
*StoreApi* | [**get_inventory**](docs/StoreApi.md#get_inventory) | **GET** /store/inventory | Returns pet inventories by status
*StoreApi* | [**get_inventory_in_object**](docs/StoreApi.md#get_inventory_in_object) | **GET** /store/inventory?response=arbitrary_object | Fake endpoint to test arbitrary object return by &#39;Get inventory&#39;
*StoreApi* | [**get_order_by_id**](docs/StoreApi.md#get_order_by_id) | **GET** /store/order/{orderId} | Find purchase order by ID
*StoreApi* | [**place_order**](docs/StoreApi.md#place_order) | **POST** /store/order | Place an order for a pet
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /user | Create user
*UserApi* | [**create_users_with_array_input**](docs/UserApi.md#create_users_with_array_input) | **POST** /user/createWithArray | Creates list of users with given input array
*UserApi* | [**create_users_with_list_input**](docs/UserApi.md#create_users_with_list_input) | **POST** /user/createWithList | Creates list of users with given input array
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /user/{username} | Delete user
*UserApi* | [**get_user_by_name**](docs/UserApi.md#get_user_by_name) | **GET** /user/{username} | Get user by user name
*UserApi* | [**login_user**](docs/UserApi.md#login_user) | **GET** /user/login | Logs user into the system
*UserApi* | [**logout_user**](docs/UserApi.md#logout_user) | **GET** /user/logout | Logs out current logged in user session
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /user/{username} | Updated user


## Documentation For Models

 - [Animal](docs/Animal.md)
 - [Cat](docs/Cat.md)
 - [Category](docs/Category.md)
 - [Dog](docs/Dog.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [Model200Response](docs/Model200Response.md)
 - [ModelReturn](docs/ModelReturn.md)
 - [Name](docs/Name.md)
 - [Order](docs/Order.md)
 - [Pet](docs/Pet.md)
 - [SpecialModelName](docs/SpecialModelName.md)
 - [Tag](docs/Tag.md)
 - [User](docs/User.md)


## Documentation For Authorization


## test_api_key_header

- **Type**: API key
- **API key parameter name**: test_api_key_header
- **Location**: HTTP header

## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header

## test_http_basic

- **Type**: HTTP basic authentication

## test_api_client_secret

- **Type**: API key
- **API key parameter name**: x-test_api_client_secret
- **Location**: HTTP header

## test_api_client_id

- **Type**: API key
- **API key parameter name**: x-test_api_client_id
- **Location**: HTTP header

## test_api_key_query

- **Type**: API key
- **API key parameter name**: test_api_key_query
- **Location**: URL query string

## petstore_auth

- **Type**: OAuth
- **Flow**: implicit
- **Authorizatoin URL**: http://petstore.swagger.io/api/oauth/dialog
- **Scopes**: 
 - **write:pets**: modify pets in your account
 - **read:pets**: read your pets


## Author

apiteam@swagger.io

