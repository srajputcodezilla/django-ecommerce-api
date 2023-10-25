from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","category_name","category_id",'price','discount','discount_type','stock_qnt','avilable_qnt']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display=["product_id","product_name","description","price"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetail,ProductDetailsAdmin)
