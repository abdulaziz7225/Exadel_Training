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
