from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['nombre', 'cedula', 'telefono', 'direccion_raw', 'pago_en_casa', 'precio']
        widgets = {
                'direccion_raw': forms.Textarea(attrs={'rows':4})
                }
