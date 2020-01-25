from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class OrderProductInline(admin.TabularInline):
    model = OrderProduct

class OrderAdmin(ImportExportModelAdmin):
	list_display = ('name', "address", 'phone', 'email')
	inlines = [OrderProductInline]

class TypeDeliveryAdmin(ImportExportModelAdmin):
	list_display = ('name', 'price', "active_more", 'active_default')

admin.site.register(Order, OrderAdmin)
admin.site.register(TypeDelivery, TypeDeliveryAdmin)