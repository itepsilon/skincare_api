from django.contrib import admin
from skincare_app.models import Product, Tag, Profile

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('name', 'description', 'price', 'tags')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_filter = ('name', 'description')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_filter = ('user', 'first_name', 'last_name', 'middle_name', 'favorite_products')