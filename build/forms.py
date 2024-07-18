from django import forms
from .models import *

class TicketForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'FirstName'}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'LastName'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'Email', 'placeholder': 'E-ticket will be sent via this Email ID'}))
    contact_no = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'Contact'}))
    age = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'Age'}))
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'Qty'}))
    tr_id = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'trId'}))

    class Meta:
        model = Ticket
        fields = ('first_name', 'last_name', 'contact_no', 'email', 'age', 'quantity', 'seats', 'file', 'tr_id')
            