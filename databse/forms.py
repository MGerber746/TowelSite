from django import forms
from .models import Order

class CreateOrderForm(forms.ModelForm):
    Fname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    Lname= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    Address= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Postal Code'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'State'}))


    class Meta:
        model = Order
        fields = ['Fname', 'Lname', 'email', 'Address', 'postal_code', 'city', 'state']
