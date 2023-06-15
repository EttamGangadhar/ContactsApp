from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=50)
    organisation = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    website = models.URLField(max_length=200)
    notes = models.TextField()
    address = models.TextField()
    image = models.ImageField(upload_to='images/', null=True)
