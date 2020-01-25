from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoryAdmin(ImportExportModelAdmin):
	list_display = ('name',)

class ProductAdmin(ImportExportModelAdmin):
    list_display = ('name', 'category', 'price', 'description')

class ProductImageAdmin(ImportExportModelAdmin):
	list_display = ('product', 'image')

class BrandAdmin(ImportExportModelAdmin):
	list_display = ('name',)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Brand, BrandAdmin)