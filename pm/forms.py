from django.forms import ModelForm
from .models import Inventory

class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'description', 'manufacturer', 'color', 'weight', 'note']