"""
from django import forms
from .models import Item

class AddForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('created_by',
        'title', 'image', 'description', 'price', 'pieces', 'instructions', 'labels', 'label_colour', 'slug')
    """

from django import forms


class Subscribe(forms.Form):
    Email = forms.EmailField()
    def __str__(self):
        return self.Email