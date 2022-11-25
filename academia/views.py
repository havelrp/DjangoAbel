from django.shortcuts import render
# Create your views here.

def clientes_list(request):
    return render(request, 'academia/clientes_list.html', {})