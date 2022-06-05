from collections import OrderedDict
import factory
from faker import Faker
fake = Faker()

from apps.notification.models import Notification
from tests.test_request.factories import RequestFactory
from tests.test_user.factories import CompanyFactory


class NotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Notification

    name = fake.text(max_nb_chars=20)
    details = fake.text(max_nb_chars=100)
    viewed_by_company = fake.random_element(
    elements=OrderedDict([True, False]))
    created_at = fake.date_time_this_century()
    request = factory.SubFactory(RequestFactory)
    company = factory.SubFactory(CompanyFactory)
    slug = "notification_slug"