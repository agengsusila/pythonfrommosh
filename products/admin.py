from django.contrib import admin
from .models import Product, Offer


class AdminOffer(admin.ModelAdmin):
    list_display = ('code', 'discount')


class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Product, AdminProduct)
admin.site.register(Offer, AdminOffer)
