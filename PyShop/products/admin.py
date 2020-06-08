from django.contrib import admin
from .models import Product, Offer


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class Offeradmin(admin.ModelAdmin):
    list_display = ('codename', 'discount')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, Offeradmin)