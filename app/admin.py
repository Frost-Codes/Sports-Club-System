from django.contrib import admin
from .models import Product, CustomerDetails, CustomerAddress, County, Town, Cart, WishList
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'current_price', 'previous_price', 'description', 'category',
                    'in_stock', 'image']


@admin.register(CustomerDetails)
class CustomerDetailsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'last_name', 'gender', 'next_of_kin',
                    'next_of_kin_contact', 'date_of_birth', 'contact', 'sub_county', 'school',
                    'games_of_interest', 'height_in_cm', 'weight_in_kgs', 'special_needs']


@admin.register(CustomerAddress)
class CustomerAddressModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'county', 'town', 'pick_up_station', 'zip_code', 'contact']


@admin.register(County)
class CountyModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'county']


@admin.register(Town)
class TownModelaAmin(admin.ModelAdmin):
    list_display = ['id', 'county', 'town', 'shipping_cost']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

    def products(self, obj):
        link = reverse('admin:app_product_change', args=[obj.product.pk])
        return format_html('a href="{}">{}</a>', link, obj.product.title)


@admin.register(WishList)
class WishListModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product']

