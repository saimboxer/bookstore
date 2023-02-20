from django import forms
from .models import *

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "author", "year", "publisher")
        years = [(year, year) for year in range(1700, 2100)]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'required': True}),
            'author':forms.TextInput(attrs={'class':'form-control', 'required': True}),
            'year':forms.Select(attrs={'class':'form-control', 'required': True}, choices=years),
            'publisher':forms.TextInput(attrs={'class':'form-control', 'required': False})
        }

class AddAttributeForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = ("attribute",)
        widgets = {
            'attribute':forms.TextInput(attrs={'class':'form-control'}),
        } 

class AddAttributeValueForm(forms.ModelForm):
    class Meta:
        model = AttributeValue
        fields = ("attribute_value",)
        widgets = {
            'attribute_value':forms.TextInput(attrs={'class':'form-control'}),
        }         

class BookAttributeValueForm(forms.ModelForm):
    class Meta:
        model = BookAttributeValue
        fields = ("book", "attribute", "attribute_value",)
        widgets = {
            'book':forms.TextInput(attrs={'class':'form-control'}),
            'attribute':forms.TextInput(attrs={'class':'form-control'}),
            'attribute_value':forms.TextInput(attrs={'class':'form-control'})
        }          