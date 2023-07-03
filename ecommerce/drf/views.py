from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from ecommerce.inventory.models import (
    Product,
    Category,
    ProductType,
    ProductInventory,
    Brand,
)
from ecommerce.drf.serializer import (
    AllProducts,
    # AllCategory,
    # AllProductType,
    AllProductInventory,
    # AllBrand,
)


class AllProductsViewset(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Product.objects.all()
    serializer_class = AllProducts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        queryset = Product.objects.filter(category__slug=slug)
        serializer = AllProducts(queryset, many=True)
        return Response(serializer.data)


class AllProductInventoryViewset(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = ProductInventory.objects.all()

    def list(self, request, slug=None):
        queryset = ProductInventory.objects.filter(product__category__slug=slug)
        serializer = AllProductInventory(
            queryset, context={"request": request}, many=True
        )
        return Response(serializer.data)


"""
class AllCategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = AllCategory
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AllProductTypeViewset(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = AllProductType
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AllBrandViewset(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = AllBrand
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]"""
