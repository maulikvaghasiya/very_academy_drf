from django.shortcuts import render
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Count
from ecommerce.inventory.models import (
    Category,
    Product,
    ProductInventory,
    ProductTypeAttribute,
)



def home(request):
    return render(request, "index.html")


def category(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "categories.html", context)


def product_by_category(request, category):
    products_by_category = Product.objects.filter(category__name=category).values(
        "id", "name", "slug", "category__name", "product__store_price"
    )
    context = {"products_by_category": products_by_category}
    return render(request, "product_by_category.html", context)


def product_details(request, slug):
    filter_arguments = []

    if request.GET:
        for value in request.GET.values():
            filter_arguments.append(value)
    
        product_detail = ProductInventory.objects.filter(product__slug=slug).annotate(num_tags=Count("attribute_values")).filter(attribute_values__attribute_value__in=filter_arguments).values("id", "product__name", "sku", "store_price", "product_inventory__units")
        
    else:
        product_detail = ProductInventory.objects.filter(product__slug=slug).values("id", "product__name", "sku", "store_price", "product_inventory__units").annotate(field = ArrayAgg("attribute_values__attribute_value")).get()
        
    product_attribute_name_value = ProductInventory.objects.filter(product__slug=slug).values("attribute_values__product_attribute__name", "attribute_values__attribute_value")

    product_attribute_name = ProductTypeAttribute.objects.filter(product_type__product_type__product__slug=slug).values("product_attribute__name")

    context = {
        "product_detail": product_detail,
        "product_attribute_name_value": product_attribute_name_value,
        "product_attribute_name": product_attribute_name,
    }
    return render(request, "product_details.html", context)
