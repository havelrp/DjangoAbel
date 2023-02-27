from django.shortcuts import render
# Create your views here.

def clientes_list(request):
    return render(request, 'plastic_dreams/clientes_list.html', {})