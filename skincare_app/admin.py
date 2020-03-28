from django.contrib import admin
from skincare_app.models import Product, Tag

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('name', 'description', 'price', 'tags')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_filter = ('name', 'description')