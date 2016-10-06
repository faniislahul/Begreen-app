from django.contrib import admin
from webapp.models import *
# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "description",)
    #ordering = ('id',)
   
admin.site.register(categories, CategoriesAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ("SKU","name","price1","price2","price3","description","category","pic","is_stockable",)
    #ordering = ('id',)
   
admin.site.register(products, ProductsAdmin)

class subsAdmin(admin.ModelAdmin):
    list_display = ("name", "description","parent","pic",)
    #ordering = ('id',)
   
admin.site.register(subcategories, subsAdmin)
