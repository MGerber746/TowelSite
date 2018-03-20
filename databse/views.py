from django.shortcuts import render
from django.views import generic
from databse.models import Product

# Create your views here.
class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products.html'

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_detail.html'
