from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductApiView.as_view()),
    path('products/<str:id>', ProductApiView.as_view()),
    path('product_by_category/<str:id>', ProductByCategoryApiView.as_view()),
    path('category/<str:id>', CategoryApiView.as_view()),
    path('category', CategoryApiView.as_view()),
    path('product-details/<str:id>', ProductDetailsApiView.as_view()),
    path('product-create', CreateProductDetailsApiView.as_view())

]