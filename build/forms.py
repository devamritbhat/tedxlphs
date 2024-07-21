from django import forms
from .models import *

class TicketForm(forms.ModelForm):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'id': 'FirstName', 'autocomplete': 'off'}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'id': 'LastName', 'autocomplete': 'off'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'id': 'Email', 'placeholder': 'E-ticket will be sent via this Email ID', 'autocomplete': 'off'}))
    contact_no = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'id': 'Contact', 'autocomplete': 'off'}))
    age = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'id': 'Age', 'autocomplete': 'off'}))
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'id': 'Qty', 'autocomplete': 'off'}))
    tr_id = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'trId', 'autocomplete': 'off'}))

    class Meta:
        model = Ticket
        fields = ('first_name', 'last_name', 'contact_no', 'email', 'age', 'quantity', 'seats', 'file', 'tr_id')
            