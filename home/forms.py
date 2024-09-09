# forms.py

from django import forms
from .models import IsbnRegister, CoverForm, EditForm

class IsbnForm(forms.ModelForm):
    class Meta:
        model = IsbnRegister
        fields = '__all__'

        # Adding Bootstrap classes to each field using widgets
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',  # Bootstrap form-control class for input
                'placeholder': 'Enter book title',  # Optional placeholder
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter author name',
            }),
            'language_of_book': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book language',
            }),
            'editor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter editor (optional)',
            }),
            'book_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book type',
            }),
        }

class CoverdForm(forms.ModelForm):
    class Meta:
        model = CoverForm
        fields = '__all__'

        # Adding Bootstrap classes to each field using widgets
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',  # Bootstrap form-control class for input
                'placeholder': 'Enter book title',  # Optional placeholder
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter author name',
            }),
            'language_of_book': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book language',
            }),
            'editor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter editor (optional)',
            }),
            'book_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book type',
            }),
            'isbn_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your ISBN Number',
            }),
        }

class EditBForm(forms.ModelForm):
    class Meta:
        model = EditForm
        fields = '__all__'

        # Adding Bootstrap classes to each field using widgets
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',  # Bootstrap form-control class for input
                'placeholder': 'Enter book title',  # Optional placeholder
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter author name',
            }),
            'language_of_book': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book language',
            }),
            'book': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }