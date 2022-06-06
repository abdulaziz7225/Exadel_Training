from model_bakery import baker
import json
import pytest

from apps.service.models import Service


@pytest.mark.parametrize(
    "name, type_of_service, cost_of_service, created_at, company, slug, validity",
    [
        ("NewTitle", "NewDescription", 12, "2011-06-01 08:15:29", 1, "slug", True),
        # ("NewTitle2", "NewDescription2", True, "2011-06-01 08:15:29", "BMW", "slug", True),
    ],
)
def test_service_instance(
    db, service_factory, name, type_of_service, cost_of_service, created_at, company, slug, validity
):
    test = service_factory(
        name=name, 
        type_of_service = type_of_service,
        cost_of_service = cost_of_service,
        created_at=created_at,
        company_id=company,
        slug=slug,
    )

    item = Service.objects.count()
    print(item)
    assert item == validity


# @pytest.mark.django_db
# class TestServiceEndpoints:

#     endpoint = '/services/'

#     def test_list(self, api_client):

#         baker.make(Service, _quantity=3)

#         response = api_client().get(
#             self.endpoint
#         )

#         assert response.status_code == 200
#         assert len(json.loads(response.content)) == 3