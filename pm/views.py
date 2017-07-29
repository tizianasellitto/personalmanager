from django.shortcuts import render
from django.http import HttpResponse

from .models import Inventory

def index(request):
    return HttpResponse("Hello, world. You're at the personal manager index.")

# CRUD Inventory
def index(request):
    inventory_list = Inventory.objects.order_by('-name')[:5]
    context = {'inventory_list': inventory_list}
    return render(request, 'pm/inventory/index.html', context)