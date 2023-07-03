from django.contrib import admin
from ecommerce.inventory.models import (
    Category,
    Product,
    ProductInventory,
    ProductType,
    Brand,
    Media,
    Stock,
    ProductAttribute,
    ProductAttributeValue,
    ProductTypeAttribute,
)


class CategoryAdmin(admin.ModelAdmin):
    """
    Category model admin interface.
    """

    list_display = ("id", "name")
    list_display_links = ("id",)


class ProductAdmin(admin.ModelAdmin):
    """
    Product model admin interface.
    """

    list_display = ("id", "name")
    list_display_links = ("id",)


class ProductInventoryAdmin(admin.ModelAdmin):
    """
    Product inventory model admin interface.
    """

    list_display = ("id", "product", "product_type", "brand", "attribute_value")
    list_display_links = ("id",)

    @admin.display(description="attribute_values")
    def attribute_value(self, obj):
        return [value.attribute_value for value in obj.attribute_values.all()]


class ProductTypeAdmin(admin.ModelAdmin):
    """
    Product type model admin interface.
    """

    list_display = ("id", "name")
    list_display_links = ("id",)


class BrandAdmin(admin.ModelAdmin):
    """
    Brand model admin interface.
    """

    list_display = ("id", "name")
    list_display_links = ("id",)


class MediaAdmin(admin.ModelAdmin):
    """
    Media model admin interface.
    """

    list_display = ("id", "img_url")
    list_display_links = ("id",)


class StockAdmin(admin.ModelAdmin):
    """
    Stock model admin interface.
    """

    list_display = ("id", "product_inventory", "units")
    list_display_links = ("id",)


class ProductAttributeAdmin(admin.ModelAdmin):
    """
    Product attribute model admin interface.
    """

    list_display = ("id", "name")
    list_display_links = ("id",)


class ProductAttributeValueAdmin(admin.ModelAdmin):
    """
    Product attribute value model admin interface.
    """

    list_display = ("id", "product_attribute", "attribute_value")
    list_display_links = ("id",)
    
class ProductTypeAttributeAdmin(admin.ModelAdmin):
    """
    Product type attribute model admin interface.
    """

    list_display = ("id","product_attribute","product_type")
    list_display_links = ("id",)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductInventory, ProductInventoryAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(ProductAttributeValue, ProductAttributeValueAdmin)
admin.site.register(ProductTypeAttribute, ProductTypeAttributeAdmin)
