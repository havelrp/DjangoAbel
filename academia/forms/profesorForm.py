from django import forms
from academia.models import profesor

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dni = forms.CharField(max_length=8)
    fecha_nacimiento = forms.DateField()
    email = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=100)