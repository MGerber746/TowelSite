from django.shortcuts import render
from django.views import generic
from databse.models import Product, Order, OrderItem, Category
from .forms import CreateOrderForm, ContactForm
from cart1.forms import CartAddProductForm
from cart1.cart import Cart
from .tasks import order_created
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']
            template = get_template('contact_template.txt')
            context = Context({'contact_name':contact_name, 'contaxt_email':contact_email, 'form_content':form_content})
            content = template.render(context)
            email = EmailMessage('New contact form submission', content, 'LTDC <test@ltdc.com>', [''], headers = {'Reply-To':contact_email})
            email.send()
            return redirect('')
    return render(request, 'about.html', {'form':form_class})

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

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            order_created.delay(order.id)
            return render(request, 'created.html', {'order': order})
    else:
        form = CreateOrderForm()
    return render(request, 'create.html', {'cart': cart, 'form': form})
