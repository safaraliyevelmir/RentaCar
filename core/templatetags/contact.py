from core.models import Adress, ContactEmail, ContactInformationPhoneNumber
from django import template
 
register = template.Library()


@register.simple_tag
def contactnumber():
    number = ContactInformationPhoneNumber.objects.all()
    return number


@register.simple_tag
def contactemail():
    email = ContactEmail.objects.all()
    return email


@register.simple_tag
def contactaAdress():
    adress = Adress.objects.all()
    return adress