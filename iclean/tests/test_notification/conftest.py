import pytest

from pytest_factoryboy import register
from tests.test_notification.factories import NotificationFactory


register(NotificationFactory)