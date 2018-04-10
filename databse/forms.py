from django import forms
from .models import Order

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['Fname', 'Lname', 'email', 'Address', 'postal_code', 'city']
