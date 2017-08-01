from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect

from .models import Inventory
from .forms import InventoryForm

# CRUD Inventory
def inventory_index(request):
    inventory_list = Inventory.objects.order_by('-name')[:5]
    context = {'inventory_list': inventory_list}
    return render(request, 'pm/inventory/index.html', context)

def inventory_detail(request, item_id):
    inventory_item = get_object_or_404(Inventory, pk=item_id)
    return render(request, 'pm/inventory/detail.html', {'item': inventory_item})

def inventory_new(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            inventory_item = form.save()
            return redirect('inventory_detail', item_id=inventory_item.pk)
    else:
        form = InventoryForm()
    return render(request, 'pm/inventory/new.html', {'form': form})