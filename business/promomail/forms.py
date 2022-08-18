from .models import customer
from django import forms


class Customer(forms.ModelForm):
    # specify model to be used to create from
    model = customer
    fields = 'email'
