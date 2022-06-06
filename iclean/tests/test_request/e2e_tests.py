from model_bakery import baker
import json
import pytest

from apps.request.models import RequestStatus, Request


@pytest.mark.parametrize(
    "name, validity",
    [
        ("NewTitle", True),
        # ("NewTitle2", True),
    ],
)
def test_request_status_instance(
    db, request_status_factory, name, validity
):
    test = request_status_factory(
        name=name, 
    )

    item = RequestStatus.objects.count()
    print(item)
    assert item == validity


@pytest.mark.parametrize(
    "name, total_area, created_at, client, company, status, service, slug, validity",
    [
        ("NewTitle", 24, "2011-06-01 08:15:29", 4, 1, 2, 3, "slug", True),
        # ("NewTitle2", 15, "2011-06-01 08:15:29", 3, 2, 1, 4, "slug", True),
    ],
)
def test_request_instance(
    db, request_factory, name, total_area, created_at, client, company, status, service, slug, validity
):
    test = request_factory(
        name=name, 
        total_area=total_area,
        created_at=created_at,
        client_id=client,
        company_id=company,
        status_id=status,
        service_id=service,
        slug=slug,
    )

    item = Request.objects.count()
    print(item)
    assert item == validity