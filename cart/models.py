from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	name = models.CharField(max_length=100)
	description = models.TextField(null=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='products/')

	def __str__(self):
		return self.name

class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=0)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.quantity} x {self.product.name}'
	
class Order(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	address=models.CharField(max_length=200)
	
	def __str__(self):
		return self.address


