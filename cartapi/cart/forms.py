# -*- coding: utf-8 -*-
from django.forms import *

from .models import Order, TypeDelivery


# Create the form class.
class OrderForm(ModelForm):

    class Meta:

        model = Order
        fields = ['name', 'address', 'phone', 'email', 'shipping_options']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+38(0XX) XXX-XXXX'
            }),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'shipping_options': Select(),
        }

    def clean(self):
        cleaned_data = super(OrderForm, self).clean()
        self.cleaned_data = cleaned_data

    def clean_email(self):

        email = self.cleaned_data['email']
        # if not self.user.is_authenticated and User.objects.filter(email=email).exists():
        #     raise ValidationError("Email already exists")
        return email

    def __init__(self, user, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)