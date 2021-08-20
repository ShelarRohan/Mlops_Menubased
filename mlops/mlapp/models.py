from django.db import models

# Create your models here.

class startup_info(models.Model):
    state_choices = (("Ney York","01"),("California","00"),("Florida","10"))
    
    rnd = models.IntegerField(max_length=10)
    admin = models.IntegerField(max_length=10)
    marketing = models.IntegerField(max_length=10)
    state = models.CharField(blank=True, null=True, max_length=36)

class titanic_info(models.Model):
    
    passenger_class = models.IntegerField(max_length=10)
    sex = models.IntegerField(max_length=10)
    age = models.IntegerField(max_length=10)
    no_sibling = models.IntegerField(max_length=10)
    parch = models.IntegerField(max_length=10)
    fare_amt = models.IntegerField(max_length=10)
    embarc_c = models.IntegerField(max_length=10)
    embarc_q = models.IntegerField(max_length=10)
    embarc_s = models.FloatField(max_length=10)
    
class dogcat_info(models.Model):
    id = models.AutoField(primary_key=True)
    image=models.ImageField(upload_to="image/")
    def __str__(self):
        return self.image
    
class wine_info(models.Model):
    
    alcohol = models.FloatField(max_length=10)
    malic_acid = models.FloatField(max_length=10)
    ash = models.FloatField(max_length=10)
    acl  = models.FloatField(max_length=10)
    mg = models.FloatField(blank=True, null=True, max_length=36)
    phenols = models.FloatField(blank=True, null=True, max_length=36)
    flavanoids = models.FloatField(blank=True, null=True, max_length=36)
    nonflavanoid_phenols  = models.FloatField(blank=True, null=True, max_length=36)
    proanth  = models.FloatField(blank=True, null=True, max_length=36)
    color_int  = models.FloatField(blank=True, null=True, max_length=36)
    hue  = models.FloatField(blank=True, null=True, max_length=36)
    od  = models.FloatField(blank=True, null=True, max_length=36)
    proline = models.FloatField(blank=True, null=True, max_length=36)
    
    