from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from ecommerce.drf import views

router = routers.DefaultRouter()
router.register(r"productapi", views.AllProductsViewset, basename="allproduct")
router.register(
    r"productinventoryapi/(?P<slug>[^/.]+)",
    views.AllProductInventoryViewset,
    basename="allproductinventory",
)
# router.register(r"categoryapi", views.AllCategoryViewset, basename="allcategory")
# router.register(
#    r"producttypeapi", views.AllProductTypeViewset, basename="allproducttype"
# )
# router.register(r"brandapi", views.AllBrandViewset, basename="allbrand")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("demo/", include("ecommerce.demo.urls"), name="demo"),
    path("", include(router.urls)),
]
