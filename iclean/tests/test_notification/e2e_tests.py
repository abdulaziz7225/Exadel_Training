from model_bakery import baker
import json
import pytest

from apps.notification.models import Notification


@pytest.mark.parametrize(
    "name, details, viewed_by_company, created_at, request, company, slug, validity",
    [
        ("NewTitle", "NewDescription", False, "2011-06-01 08:15:29", 4, 1, "slug", True),
        # ("NewTitle2", "NewDescription2", True, "2011-06-01 08:15:29", 4, 2, "slug", True),
    ],
)
def test_notification_instance(
    db, notification_factory, name, details, viewed_by_company, created_at, request, company, slug, validity
):
    test = notification_factory(
        name=name, 
        details=details,
        viewed_by_company=viewed_by_company,
        created_at=created_at,
        request_id=request,
        company_id=company,
        slug=slug,
    )

    item = Notification.objects.count()
    print(item)
    assert item == validity



# @pytest.mark.django_db
# def test_list(api_client, notification_factory):
#     endpoint = '/notifications/'
#     # baker.make(Notification, _quantity=3)

#     response = api_client().get(endpoint)

#     assert response.status_code == 200
#     assert len(json.loads(response.content)) == 1

# @pytest.mark.django_db
# class TestNotificationEndpoints:

#     endpoint = '/notifications/'

#     def test_list(self, api_client):

#         baker.make(Notification, _quantity=3)

#         response = api_client().get(
#             self.endpoint
#         )

#         assert response.status_code == 200
#         assert len(json.loads(response.content)) == 3



# pytestmark = pytest.mark.django_db
# @pytest.mark.django_db
# class TestNotificationEndpoints:

#     endpoint = '/notifications/'

#     def test_list(self, api_client):
#         baker.make(Notification, _quantity=3)

#         response = api_client().get(
#             self.endpoint
#         )

#         assert response.status_code == 200
#         assert len(json.loads(response.content)) == 3

#     def test_create(self, api_client):
#         notification = baker.prepare(Notification) 
#         expected_json = {
#             'name': notification.name,
#             'details': notification.details,
#             'viewed_by_company': notification.viewed_by_company,
#             'created_at': notification.created_at,
#             'request': notification.request,
#             'company': notification.company,
#             'slug': notification.slug,
#         }

#         response = api_client().post(
#             self.endpoint,
#             data=expected_json,
#             format='json'
#         )

#         assert response.status_code == 201
#         assert json.loads(response.content) == expected_json

#     def test_retrieve(self, api_client):
#         notification = baker.make(Notification)
#         expected_json = {
#             'name': notification.name,
#             'details': notification.details,
#             'viewed_by_company': notification.viewed_by_company,
#             'created_at': notification.created_at,
#             'request': notification.request,
#             'company': notification.company,
#             'slug': notification.slug,
#         }
#         url = f'{self.endpoint}{notification.id}/'

#         response = api_client().get(url)

#         assert response.status_code == 200
#         assert json.loads(response.content) == expected_json

#     def test_update(self, rf, api_client):
#         old_notification = baker.make(Notification)
#         new_notification = baker.prepare(Notification)
#         notification_dict = {
#             'name': new_notification.name,
#             'details': new_notification.details,
#             'viewed_by_company': new_notification.viewed_by_company,
#             'slug': new_notification.slug,
#         } 

#         url = f'{self.endpoint}{old_notification.id}/'

#         response = api_client().put(
#             url,
#             notification_dict,
#             format='json'
#         )

#         assert response.status_code == 200
#         assert json.loads(response.content) == notification_dict

#     @pytest.mark.parametrize('field',[
#         ('name'),
#         ('details'),
#         ('viewed_by_company'),
#         ('slug'),
#     ])
#     def test_partial_update(self, mocker, rf, field, api_client):
#         notification = baker.make(Notification)
#         notification_dict = {
#         'name': notification.name,
#         'details': notification.details,
#         'viewed_by_company': notification.viewed_by_company,
#         'slug': notification.slug,
#         } 
#         valid_field = notification_dict[field]
#         url = f'{self.endpoint}{notification.id}/'

#         response = api_client().patch(
#             url,
#             {field: valid_field},
#             format='json'
#         )

#         assert response.status_code == 200
#         assert json.loads(response.content)[field] == valid_field

#     def test_delete(self, mocker, api_client):
#         notification = baker.make(Notification)
#         url = f'{self.endpoint}{notification.id}/'

#         response = api_client().delete(url)

#         assert response.status_code == 204
#         assert Notification.objects.all().count() == 0
