import pytest

from pytest_factoryboy import register
from tests.test_user.factories import RoleFactory, UserFactory, ClientFactory, CompanyFactory


register(RoleFactory)
register(UserFactory)
register(ClientFactory)
register(CompanyFactory)


@pytest.fixture
def new_user(db, user_factory):
    user = user_factory.create()
    return user
