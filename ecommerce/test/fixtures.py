import pytest
from django.core.management import call_command


@pytest.fixture
def create_admin_user(django_user_model):
    """
    Return admin user.
    """
    return django_user_model.objects.create_superuser(
        "admin", "admin@gmail.com", "admin"
    )


@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load DB data fixture.
    """
    with django_db_blocker.unblock():
        call_command("loaddata", "db_admin_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
        call_command("loaddata", "db_product_fixture.json")
        call_command("loaddata", "db_brand_fixture.json")
        call_command("loaddata", "db_producttype_fixture.json")
        call_command("loaddata", "db_inventory_fixture.json")
        call_command("loaddata", "db_media_fixture.json")
        call_command("loaddata", "db_stock_fixture.json")
        call_command("loaddata", "db_attribute_fixture.json")
        call_command("loaddata", "db_product_attribute_value.json")
        call_command("loaddata", "db_product_attribute_values.json")
