from django.db import models

class merchants(models.Model):
    name=models.CharField(max_length=120)
    merchant_id=models.IntegerField(default=0)

    def __str__(self):
        return self.name
class Order(models.Model):
    merchant=models.ForeignKey(merchants,on_delete=models.CASCADE)
    merchant_invoice_id=models.IntegerField(default=0)
    Product_type=models.CharField(max_length=120)
    weight=models.FloatField(default=0)
    Division=models.CharField(max_length=120)
    District=models.CharField(max_length=120)
    Street=models.CharField(max_length=120)
    Charge=models.FloatField(default=0)
    Cod_charge_add=models.FloatField(default=0)
    return_charge_add=models.FloatField(default=0)
    def merchant_name(self):
        return self.merchant.name
