from django.db import models
from django.urls import reverse

FUEL_CHOICE = (
    ('benzin','benzin'),
    ('dizel','dizel'),
    ('elektrik','elektrik'),
)

TYPES_OF_TRANSMISSIONS_CHOICE = (
    ('auto','auto'),
    ('mexanika','mexanika'),
)

class Catagory(models.Model):

    img = models.ImageField(upload_to='cars/')
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title

class Car(models.Model):

    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='cars/')

    fuel = models.CharField(max_length=255,choices=FUEL_CHOICE)
    type_of_transmissions = models.CharField(max_length=255,choices=TYPES_OF_TRANSMISSIONS_CHOICE)
    catagory = models.ForeignKey('Catagory', on_delete=models.CASCADE)
    engine = models.FloatField()
    year = models.IntegerField(default=2000)
    luggage = models.IntegerField()
    seat_count = models.IntegerField()
    door = models.IntegerField() 
    star_count = models.IntegerField()
    
    price_2_3 = models.CharField('Price for 2-3 Day',max_length=255)
    price_4_7 = models.CharField('Price for 4-7 Day',max_length=255)
    price_7_15 = models.CharField('Price for 7-15 Day',max_length=255)
    price_16_30 = models.CharField('Price 1for 6-30 Day',max_length=255)
    price_30 = models.CharField('Price for more 30 Day',max_length=255)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    


class ConditionForCar(models.Model):

    pass