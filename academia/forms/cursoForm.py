from django import forms
from academia.models import curso

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=200)
    fecha_inicio = forms.DateField()
    fecha_fin = forms.DateField()
    cupo = forms.IntegerField()