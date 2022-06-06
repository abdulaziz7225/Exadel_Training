from model_bakery import baker
import json
import pytest

from apps.review.models import Review


@pytest.mark.parametrize(
    "comment, rating, created_at, client, company, slug, validity",
    [
        ("NewTitle", 4.7, "2011-06-01 08:15:29", 4, 1, "slug", True),
        # ("NewTitle2", 4.1, "2011-06-01 08:15:29", 4, 2, "slug", True),
    ],
)
def test_review_instance(
    db, review_factory, comment, rating, created_at, client, company, slug, validity
):
    test = review_factory(
        comment=comment,
        rating=rating,
        created_at=created_at,
        client_id=client,
        company_id=company,
        slug=slug,
    )

    item = Review.objects.count()
    print(item)
    assert item == validity