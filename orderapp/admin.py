from django.contrib import admin

from .models import *


# admin.site.register(Customer)
# admin.site.register(Product)
# admin.site.register(OrderApp)

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']


admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover', 'price', 'description', 'create_at']


admin.site.register(Product, ProductAdmin)


class OrderAppAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ['title', 'product', 'create_at']


admin.site.register(OrderApp, OrderAppAdmin)
