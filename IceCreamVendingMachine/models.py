from django.db import models

# Create your models here.

class IceCream(models.Model):
	iceCreamID = models.IntegerField(default=0)
	iceCreamID.primary_key = True
	flavor = models.CharField(max_length=30)
	scoopable = models.CharField(max_length=3)
	#description = models.CharField(max_length = 200)

	def __str__(self):
		return self.flavor

class Stores(models.Model):
	storeID = models.IntegerField(default=0)
	storeID.primary_key = True
	storeName = models.CharField(max_length=30)
	city = models.CharField(max_length = 30)
	state = models.CharField(max_length = 2)

	def __str__(self):
		return self.storeID

class WhereOffered(models.Model):
	storeID = models.IntegerField(default=0)
	storeID.primary_key = True
	iceCreamID = models.IntegerField(default=0)
	class Meta:
		unique_together = ('storeID', 'iceCreamID')

	def __str__(self):
		return self.storeID

class Cart(models.Model):
	iceCreamID = models.IntegerField(default=0)
	iceCreamID.primary_key = True
	quantity = models.IntegerField(default=0)

	def __str__(self):
		return self.quantity
	
