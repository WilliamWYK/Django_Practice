from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=50,blank=True,default='')
    
    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=4, decimal_places=0)
    comment = models.CharField(max_length=50,blank=True,default='')
    is_avalible = models.BooleanField(default=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['price']
    
class Comment(models.Model):
    content = models.CharField(max_length=255)
    visitor = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    date_time = models.DateTimeField()
    restaurant = models.ForeignKey(Restaurant, on_delete=CASCADE)
    def __str__(self):
        return self
    class Meta:
        ordering = ['-date_time']
