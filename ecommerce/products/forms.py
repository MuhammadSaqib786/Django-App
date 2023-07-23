# products/forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    

    class Meta:
        model = Product
        fields = ['category', 'title', 'description', 'image', 'price']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('Price must be a positive number.')
        return price
