from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

# Create your models here.
class Order(models.Model):
	cust_name = models.CharField(max_length=100)
	create_date = models.DateTimeField(default=timezone.now)

class Menu(models.Model):
	item_name = models.CharField(max_length=100)
	item_amt  = models.DecimalField(max_digits=7, decimal_places=2)

class Sales(models.Model):
	order_id =  models.OneToOneField(
	Order,
	on_delete=models.CASCADE,
	primary_key=True,)
	total_amt = models.DecimalField(max_digits=19, decimal_places=2)

class OrderMenu(models.Model):
	order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
	menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
	qty = models.IntegerField()



