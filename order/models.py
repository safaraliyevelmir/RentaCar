from django.db import models
from car.models import Car


TITUL_CHOICE = (
    ('Mr.','Mr.'),
    ('Ms.','Ms.'),
    ('Company.','Company.'),
)



class Order(models.Model):

    titul = models.CharField(choices=TITUL_CHOICE,max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    message = models.CharField(max_length=255)


    start_date = models.CharField(max_length=255,blank=True,null=True)
    start_time = models.CharField(max_length=255,blank=True,null=True)

    end_date = models.CharField(max_length=255,blank=True,null=True)
    end_time = models.CharField(max_length=255,blank=True,null=True)

    from_place = models.ForeignKey('Place',on_delete=models.CASCADE, related_name='from_place')
    to_place = models.ForeignKey('Place',on_delete=models.CASCADE, related_name='to_place')

    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    is_wifi = models.BooleanField()
    to_airplane = models.BooleanField()
    in_city = models.BooleanField()
    has_wifi = models.BooleanField()
    child_seat = models.BooleanField()


class Place(models.Model):
    place = models.CharField(max_length=255)

    def __str__(self):
        return self.place





