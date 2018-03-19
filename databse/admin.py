from django.contrib import admin

# Register your models here.
from .models import Order, Product, Category, ProductInstance, Customer
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductInstance)
admin.site.register(Customer)
