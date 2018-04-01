from django.shortcuts import render
from django.views import generic
from databse.models import Product
from cart1.forms import CartAddProductForm

# Create your views here.
class ProductListView(generic.ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products.html'

class ProductDetailView(generic.DetailView):
    model = Product
    cart_product_form = CartAddProductForm()
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['cart_product_form'] = CartAddProductForm()
        return context
