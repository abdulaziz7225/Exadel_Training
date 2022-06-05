import pytest

from pytest_factoryboy import register
from factories import RequestStatusFactory, RequestFactory


register(RequestStatusFactory)
register(RequestFactory)