from .cart import Cart

#Returns the cart context
def cart(request):
    return {'cart': Cart(request)}
