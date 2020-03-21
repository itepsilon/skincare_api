from django.contrib import admin
from skincare_app.models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('name', 'description', 'price')