# products/admin.py
from django.contrib import admin
from .models import Product, Category, Customer
from reviews.models import Review

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Review)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email')

admin.site.register(Customer, CustomerAdmin)
