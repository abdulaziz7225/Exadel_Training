import pytest

from pytest_factoryboy import register
from tests.test_request.factories import RequestStatusFactory, RequestFactory


register(RequestStatusFactory)
register(RequestFactory)