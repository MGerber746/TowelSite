from django.contrib import admin

# Register your models here.
#Used to create items in the database
from .models import Order, Product, Category, ProductInstance
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductInstance)
