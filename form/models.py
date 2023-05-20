from django.db import models

# Create your models here.


class Bookacall(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    business_type = models.CharField(max_length=2500)
    business_name = models.CharField(max_length=2500)
    email = models.EmailField()
    business_detail = models.TextField()


    def __str__(self):
        return f"{self.first_name}from{self.business_name}"




class contactform(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    contact_matter = models.TextField()

    def __str__(self):
        return f"{self.first_name}from{self.email}"