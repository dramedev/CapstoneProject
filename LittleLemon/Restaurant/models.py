from django.db import models

class Booking(models.Model):
    name = models.CharField( max_length=50)
    last_name =models.CharField( max_length=50)
    no_of_guest = models.IntegerField()
    date =models.DateTimeField()
    
    def __str__(self):
        return self.name ,self.last_name
    

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    inventory = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name