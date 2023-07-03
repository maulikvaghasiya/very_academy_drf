from django.urls import path
from ecommerce.demo import views

urlpatterns = [
    path("", views.home, name="home"),
    path("categories/", views.category),
    path("product-by-category/<slug:category>", views.product_by_category, name = "product-by-category"),
    path("<slug:slug>", views.product_details, name="product_details"),  
]
