from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    text = RichTextField()

    def __str__(self):
        return f"About"

    class Meta:
        verbose_name_plural = 'About'

class Condtion(models.Model):

    req_documents = RichTextField('Requirements Document')
    text = RichTextField()

    def __str__(self):
        return f"Condtion"

    class Meta:
        verbose_name_plural = 'Condtion'



class Contact(models.Model):

    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    text = models.TextField()

    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.fullname


class ContactInformationPhoneNumber(models.Model):
    phone = models.CharField(max_length=255)


class ContactEmail(models.Model):
    email = models.EmailField()


class Adress(models.Model):
    adress = models.CharField(max_length=300)

class Quote(models.Model):

    author = models.CharField(max_length=255)
    text = models.TextField()


    def __str__(self):
        return self.author
