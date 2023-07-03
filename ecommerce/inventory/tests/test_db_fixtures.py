import pytest
from django.db import IntegrityError
from ecommerce.inventory.models import (
    Category,
    Product,
    ProductInventory,
    Media,
    Stock,
    ProductAttribute,
    ProductAttributeValue,
)


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id ,name, slug, is_active",
    [
        (3, "fashion", "fashion", 1),
        (4, "trainers", "trainers", 1),
        (5, "basball", "basball", 1),
    ],
)
def test_inventory_category_dbfixture(db, db_fixture_setup, id, name, slug, is_active):
    result = Category.objects.get(id=id)
    print(result.name)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "slug, is_active",
    [
        ("fashion", 1),
        ("trainers", 1),
        ("basball", 1),
    ],
)
def test_inventory_db_category_insert_data(db, category_factory, slug, is_active):
    result = category_factory.create(slug=slug, is_active=is_active)
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id ,web_id, name, slug, description, is_active, created_at, updated_at",
    [
        (
            1,
            "202361",
            "Men's T-shirt",
            "Mens-T-shirt",
            "Best quality product for men.",
            1,
            "2023-06-08 13:14:05",
            "2023-06-08 13:14:05",
        ),
    ],
)
def test_inventory_db_product_dbfixture(
    db,
    db_fixture_setup,
    id,
    web_id,
    name,
    slug,
    description,
    is_active,
    created_at,
    updated_at,
):
    result = Product.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    assert result.web_id == web_id
    assert result.name == name
    assert result.slug == slug
    assert result.description == description
    assert result.is_active == is_active
    assert result_created_at == created_at
    assert result_updated_at == updated_at


def test_inventory_db_product_uniqueness_integrity(db, product_factory):
    new_web_id = product_factory.create(web_id=123456789)
    with pytest.raises(IntegrityError):
        product_factory.create(web_id=123456789)


@pytest.mark.dbfixture
def test_inventory_db_product_insert_data(db, product_factory):
    new_product = product_factory.create(category=(7, 3, 5, 6))
    result_product_category = new_product.category.all()
    print(result_product_category)


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, sku, upc, product_type, product, brand, is_active, retail_price, store_price, sale_price, weight, created_at, updated_at",
    [
        (
            1,
            "7894561325",
            "789045601230",
            1,
            2,
            1,
            1,
            899.00,
            799.00,
            699.00,
            100.0,
            "2023-06-13 06:35:48",
            "2023-06-13 06:35:48",
        ),
    ],
)
def test_inventory_db_product_inventory_dataset(
    db,
    db_fixture_setup,
    id,
    sku,
    upc,
    product_type,
    product,
    brand,
    is_active,
    retail_price,
    store_price,
    sale_price,
    weight,
    created_at,
    updated_at,
):
    result = ProductInventory.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    assert result.sku == sku
    assert result.upc == upc
    assert result.product_type.id == product_type
    assert result.product.id == product
    assert result.brand.id == brand
    assert result.is_active == is_active
    assert result.retail_price == retail_price
    assert result.store_price == store_price
    assert result.sale_price == sale_price
    assert result.weight == weight
    assert result_created_at == created_at
    assert result_updated_at == updated_at


@pytest.mark.dbfixture
def test_inventory_db_product_inventory_insert_data(db, product_inventory_factory):
    new_product = product_inventory_factory.create(
        sku="123456789",
        upc="123456789",
        product_type__name="new_name",
        product__web_id="123456789",
        brand__name="new_name",
    )

    assert new_product.sku == "123456789"
    assert new_product.upc == "123456789"
    assert new_product.product_type.name == "new_name"
    assert new_product.product.web_id == "123456789"
    assert new_product.brand.name == "new_name"
    assert new_product.is_active == 1
    assert new_product.retail_price == 899.00
    assert new_product.store_price == 799.00
    assert new_product.sale_price == 699.00
    assert new_product.weight == 100.0


def test_inventory_db_producttype_insert_data(db, product_type_factory):
    new_type = product_type_factory.create(name="demo_type")
    assert new_type.name == "demo_type"


def test_inventory_db_producttype_uniqeness_integrity(db, product_type_factory):
    product_type_factory.create(name="not_unique")
    with pytest.raises(IntegrityError):
        product_type_factory.create(name="not_unique")


def test_inventory_db_producttype_insert_data(db, brand_factory):
    new_brand = brand_factory.create(name="demo_type")
    assert new_brand.name == "demo_type"


def test_inventory_db_producttype_uniqeness_integrity(db, brand_factory):
    brand_factory.create(name="not_unique")
    with pytest.raises(IntegrityError):
        brand_factory.create(name="not_unique")


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_inventory,image,alt_text,is_feature,created_at,updated_at,",
    [
        (
            1,
            1,
            "image/shorts.jpg",
            "A default image",
            1,
            "2023-06-13 13:17:02",
            "2023-06-13 13:17:02",
        ),
    ],
)
def test_inventory_db_media_dataset(
    db,
    db_fixture_setup,
    id,
    product_inventory,
    image,
    alt_text,
    is_feature,
    created_at,
    updated_at,
):
    result = Media.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    assert result.product_inventory.id == product_inventory
    assert result.image == image
    assert result.alt_text == alt_text
    assert is_feature == is_feature
    assert result_created_at == created_at
    assert result_updated_at == updated_at


def test_inventory_db_media_insert_data(db, media_factory):
    new_media = media_factory.create(product_inventory__sku="123456789")
    assert new_media.product_inventory.sku == "123456789"
    assert new_media.image == "image/default.png"
    assert new_media.alt_text == "A default image solid color"
    assert new_media.is_feature == 1


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_inventory, last_checked, units, units_sold",
    [
        (
            1,
            1,
            "2023-06-14 08:14:17",
            5,
            0,
        ),
    ],
)
def test_inventory_db_stock_dataset(
    db,
    db_fixture_setup,
    id,
    product_inventory,
    last_checked,
    units,
    units_sold,
):
    result = Stock.objects.get(id=id)
    result_created_at = result.last_checked.strftime("%Y-%m-%d %H:%M:%S")
    assert result.product_inventory.id == product_inventory
    assert result.units == units
    assert result.units_sold == units_sold
    assert result_created_at == last_checked


def test_inventory_db_stock_insert_data(db, stock_factory):
    new_stock = stock_factory.create(product_inventory__sku="123456789")
    assert new_stock.product_inventory.sku == "123456789"
    assert new_stock.units == 5
    assert new_stock.units_sold == 1


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, description",
    [
        (
            1,
            "men-tshirt-size",
            "men tshirt size",
        ),
    ],
)
def test_inventory_db_product_attribute_dataset(
    db,
    db_fixture_setup,
    id,
    name,
    description,
):
    result = ProductAttribute.objects.get(id=id)
    assert result.name == name
    assert result.description == description


def test_inventory_db_product_attribuute_insert_data(db, product_attribute_factory):
    new_product_attribute = product_attribute_factory.create()
    assert new_product_attribute.name == "name_0"
    assert new_product_attribute.description == "description_0"


def test_inventory_db_product_attribute_uniqueness_integrity(
    db, product_attribute_factory
):
    product_attribute_factory.create(name="not_unique")
    with pytest.raises(IntegrityError):
        product_attribute_factory.create(name="not_unique")


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, product_attribute, attribute_value",
    [
        (1, 1, "M"),
    ],
)
def test_inventory_db_product_attribute_value_dataset(
    db,
    db_fixture_setup,
    id,
    product_attribute,
    attribute_value,
):
    result = ProductAttributeValue.objects.get(id=id)
    assert result.product_attribute.id == product_attribute
    assert result.attribute_value == attribute_value


def test_inventory_db_product_attribute_value_insert_data(
    db,
    product_attribute_value_factory,
):
    new_product_attribute_value = product_attribute_value_factory.create(
        attribute_value="new_value", product_attribute__name="new_value"
    )
    assert new_product_attribute_value.attribute_value == "new_value"
    assert new_product_attribute_value.product_attribute.name == "new_value"


def test_inventory_db_insert_inventory_product_values(
    db, product_with_attribute_values_factory
):
    new_inv_attribute = product_with_attribute_values_factory(sku="123456789")
    result = ProductInventory.objects.get(sku="123456789")
    count = result.attribute_values.all().count()
    assert count == 2
