# reviews/forms.py
from django import forms
from .models import Review

from django import forms
from .models import Product

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError('Rating must be between 1 and 5.')
        return rating



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title', 'description', 'image', 'price']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('Price must be a positive number.')
        return price
