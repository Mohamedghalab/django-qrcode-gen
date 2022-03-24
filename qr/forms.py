from django import forms
from .models import QrCodeGen

class QrCodeForm(forms.ModelForm):
    class Meta:
        model=QrCodeGen
        fields = ['product', 'price']