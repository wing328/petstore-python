
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.another_fake_api import AnotherFakeApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from openapi_client.api.another_fake_api import AnotherFakeApi
from openapi_client.api.default_api import DefaultApi
from openapi_client.api.fake_api import FakeApi
from openapi_client.api.fake_classname_tags_123_api import FakeClassnameTags123Api
from openapi_client.api.pet_api import PetApi
from openapi_client.api.store_api import StoreApi
from openapi_client.api.user_api import UserApi
