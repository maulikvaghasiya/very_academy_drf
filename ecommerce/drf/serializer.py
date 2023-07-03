from rest_framework import serializers
from ecommerce.inventory.models import (
    Product,
    Category,
    ProductType,
    ProductInventory,
    Brand,
    ProductAttributeValue,
    Media,
)


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only = True
        editable = False


class AllBrand(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        fields = "__all__"
        depth = 2


class MeadiaSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["img_url"]

    def get_img_url(self, obj):
        return self.context["request"].build_absolute_uri(obj.img_url.url)


class AllProductInventory(serializers.ModelSerializer):
    brand = AllBrand(many=False, read_only=True)
    attribute = ProductAttributeValueSerializer(source="attribute_values", many=True)
    media_product_inventory = MeadiaSerializer(many=True)

    class Meta:
        model = ProductInventory
        fields = "__all__"
        read_only = True


"""class AllCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AllProductType(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = "__all__"






        """
