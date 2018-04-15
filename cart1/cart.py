from decimal import Decimal
from django.conf import settings
from databse.models import Product

#Cart object that uses local caching
class Cart(object):
    #Creates the cart if there isnt one in the cache
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    #Adds an item to the cart or changes the quantity
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity' : 0, 'price' : str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    #Saves the cart
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    #Removes an item from the cart
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    #Iterator to print items in the cart
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item ['quantity']
            yield item

    #Total items in cart
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    #Returns total price of cart
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    #Clears the cart (Used for when someone places an order)
    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
