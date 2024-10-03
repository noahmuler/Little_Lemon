from django.db import models


# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)
    guest_count = models.IntegerField(default=1)

    def __str__(self): 
        return self.first_name


# Add code to create Menu model
class Menu(models.Model):
    title = models.CharField(max_length=255, null=True) 
    price = models.DecimalField(null=False, max_digits=10, decimal_places=2) 
    menu_item_description = models.TextField(max_length=1000, default='')
    inventory = models.IntegerField(default=0) 

    def __str__(self):
        return self.title
   
    def get_item(self):
        return f'{self.title} : {str(self.price)}'
