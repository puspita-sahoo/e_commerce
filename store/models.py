from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(null=True, blank=True, default=None)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.id)
 
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    mobile = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=50)
    default = models.BooleanField()

    def __str__(self):
        return str(self.id)

class Cartitem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, null=False)
    def __str__(self):
        return str(f"item no-{self.id}")

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price