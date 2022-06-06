from model_bakery import baker
import json
import pytest

from apps.user.models import Role, User, Client, Company


"""
test_role_instance
"""
@pytest.mark.parametrize(
    "role, validity",
    [
        ("NewTitle", True),
        # ("NewTitle2", True),
    ],
)
def test_role_instance(
    db, role_factory, role, validity
):
    test = role_factory(
        role=role,
    )

    item = Role.objects.count()
    print(item)
    assert item == validity


"""
test_user_instance
"""
@pytest.mark.parametrize(
    "email, role, phone, country, city, is_staff, is_active, validity",
    [
        ("NewEmail", 1, "998xxxxxxxxx", "Uzbekistan", "Tashkent", False, True, True),
        # ("NewEmail2", 1, "998xxxxxxxxx", "Uzbekistan", "Tashkent", False, True, True),
    ],
)
def test_user_instance(
    db, user_factory, email, role, phone, country, city, is_staff, is_active, validity
):
    test = user_factory(
        email=email, 
        role_id=role,
        phone=phone,
        country=country,
        city=city,
        is_staff=is_staff,
        is_active=is_active,
    )

    item = User.objects.count()
    print(item)
    assert item == validity


"""
test_client_instance
"""
@pytest.mark.parametrize(
    "user, first_name, last_name, street, house_number, apartment, validity",
    [
        (2, "Abdulaziz", "Musaev", "Jurabayeva", 3, "44", True),
    ],
)
def test_client_instance(
    db, client_factory, user, first_name, last_name, street, house_number, apartment, validity
):
    test = client_factory(
        user_id=user, 
        first_name = first_name,
        last_name = last_name,
        street=street,
        house_number=house_number,
        apartment=apartment,
    )

    item = Client.objects.count()
    print(item)
    assert item == validity


"""
test_company_instance
"""
@pytest.mark.parametrize(
    "user, name, validity",
    [
        (3, "AsiaClean", True),
        # (4, "Express Cleaning", True),
    ],
)
def test_company_instance(
    db, company_factory, user, name, validity
):
    test = company_factory(
        user_id=user,
        name=name, 
    )

    item = Company.objects.count()
    print(item)
    assert item == validity