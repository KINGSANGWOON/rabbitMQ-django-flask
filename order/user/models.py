from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=30)

class Order(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order_data = models.DateTimeField('date order',auto_now_add=True)
    home_address = models.CharField(max_length=40)
    deliver_finish = models.BooleanField(default=0)
    
