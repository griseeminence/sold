from django import forms

from .models import Item

INPUT_FORMATS = 'w-full py-4 px-6 rounded-xl border'


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_FORMATS
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_FORMATS
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_FORMATS
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_FORMATS
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_FORMATS
            })
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_FORMATS
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_FORMATS
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_FORMATS
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_FORMATS
            })
        }
