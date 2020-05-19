from django.contrib.auth.forms import forms
from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('owner', )
