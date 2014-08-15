from django import forms


class PinLookup(forms.Form):
    pin = forms.CharField()
