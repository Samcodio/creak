from .models import *
from django.forms import *


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'category_logo', 'description']
        widgets = {
            'category_name': TextInput(
                attrs={
                    'type': 'text',
                    'required': 'true',
                    'placeholder': 'Please enter Category Name...'
                }
            ),
            'category_logo': FileInput(
                attrs={
                    'type': 'file',
                    'accept': 'image/*',
                    'required': 'true',
                }
            ),
            'description': Textarea(
                attrs={
                    'type': 'text',
                    'placeholder': 'Please enter Description...'
                }
            ),
        }


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select Category..."
    class Meta:
        model = Product
        fields = [
            'product_name',
            'category',
            'product_img',
            'price',
            'old_price',
            'description',
            'parts',
        ]
        widgets = {
            'product_name': TextInput(
                attrs={
                    'type': 'text',
                    'required': 'true',
                    'placeholder': 'Product Name',
                }
            ),
            'parts': TextInput(
                attrs={
                    'type': 'text',
                    'required': 'true',
                }
            ),
            'category': Select(
                attrs={
                    'required': 'true',
                }
            ),
            'product_img': FileInput(
                attrs={
                    'type': 'file',
                    'accept': 'image/*',
                    'required': 'true',
                }
            ),
            'price': TextInput(
                attrs={
                    'type': 'number',
                    'required': 'true',
                }
            ),
            'old_price': TextInput(
                attrs={
                    'type': 'number',
                }
            ),
            'description': Textarea(
                attrs={
                    'type': 'text',
                    'placeholder': 'Please enter the Product Description...'
                }
            )
        }