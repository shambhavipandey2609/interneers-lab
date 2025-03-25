from django.urls import path
from .views import ProductList, ProductDetail, ProductView

urlpatterns = [
    path("products/", ProductList.as_view(), name="product-list"),  # /api/products/
    path("products/<int:pk>/", ProductDetail.as_view(), name="product-detail"),  # /api/products/<id>/



    #week3 for mongodb
    path("new-products/",ProductView.as_view(),name="new-product"),
    path("new-products/<str:product_id>/",ProductView.as_view(),name="new-product"),
]
