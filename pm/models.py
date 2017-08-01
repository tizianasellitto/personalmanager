from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    color = models.CharField(max_length=50)
    weight = models.IntegerField(default=0)
    note = models.CharField(max_length=200)
    class Meta:
        unique_together = ('name', 'manufacturer', 'color')
    # # ...
    # def __str__(self):
    #     return self.name

class Storage(models.Model):
    inventory_item = models.ForeignKey(Inventory, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    last_modified = models.DateTimeField('last modified')

class Invoice(models.Model):
    date = models.DateTimeField('date')
    quantity = models.IntegerField(default=0)
    shipping_price = models.DecimalField(max_digits=9, decimal_places=2)
    purchase_channel = models.CharField(max_length=200)
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
    
class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT)
    inventory_item = models.ForeignKey(Inventory, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=9, decimal_places=2)