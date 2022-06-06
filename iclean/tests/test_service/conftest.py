import pytest

from pytest_factoryboy import register
from tests.test_service.factories import ServiceFactory


register(ServiceFactory)