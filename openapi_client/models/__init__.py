# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.model.additional_properties_class import AdditionalPropertiesClass
from openapi_client.model.address import Address
from openapi_client.model.animal import Animal
from openapi_client.model.animal_farm import AnimalFarm
from openapi_client.model.api_response import ApiResponse
from openapi_client.model.apple import Apple
from openapi_client.model.apple_req import AppleReq
from openapi_client.model.array_of_array_of_number_only import ArrayOfArrayOfNumberOnly
from openapi_client.model.array_of_number_only import ArrayOfNumberOnly
from openapi_client.model.array_test import ArrayTest
from openapi_client.model.banana import Banana
from openapi_client.model.banana_req import BananaReq
from openapi_client.model.capitalization import Capitalization
from openapi_client.model.cat import Cat
from openapi_client.model.cat_all_of import CatAllOf
from openapi_client.model.category import Category
from openapi_client.model.class_model import ClassModel
from openapi_client.model.client import Client
from openapi_client.model.dog import Dog
from openapi_client.model.dog_all_of import DogAllOf
from openapi_client.model.enum_arrays import EnumArrays
from openapi_client.model.enum_class import EnumClass
from openapi_client.model.enum_test import EnumTest
from openapi_client.model.file import File
from openapi_client.model.file_schema_test_class import FileSchemaTestClass
from openapi_client.model.foo import Foo
from openapi_client.model.format_test import FormatTest
from openapi_client.model.fruit import Fruit
from openapi_client.model.fruit_req import FruitReq
from openapi_client.model.gm_fruit import GmFruit
from openapi_client.model.has_only_read_only import HasOnlyReadOnly
from openapi_client.model.health_check_result import HealthCheckResult
from openapi_client.model.inline_response_default import InlineResponseDefault
from openapi_client.model.list import List
from openapi_client.model.mammal import Mammal
from openapi_client.model.map_test import MapTest
from openapi_client.model.mixed_properties_and_additional_properties_class import MixedPropertiesAndAdditionalPropertiesClass
from openapi_client.model.model200_response import Model200Response
from openapi_client.model.model_return import ModelReturn
from openapi_client.model.name import Name
from openapi_client.model.nullable_class import NullableClass
from openapi_client.model.number_only import NumberOnly
from openapi_client.model.order import Order
from openapi_client.model.outer_composite import OuterComposite
from openapi_client.model.outer_enum import OuterEnum
from openapi_client.model.outer_enum_default_value import OuterEnumDefaultValue
from openapi_client.model.outer_enum_integer import OuterEnumInteger
from openapi_client.model.outer_enum_integer_default_value import OuterEnumIntegerDefaultValue
from openapi_client.model.pet import Pet
from openapi_client.model.read_only_first import ReadOnlyFirst
from openapi_client.model.special_model_name import SpecialModelName
from openapi_client.model.string_boolean_map import StringBooleanMap
from openapi_client.model.tag import Tag
from openapi_client.model.user import User
from openapi_client.model.whale import Whale
from openapi_client.model.zebra import Zebra
