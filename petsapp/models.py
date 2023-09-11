from django.db import models

# Create your models here.
class pet(models.Model):
    gender_option = (("male","male"),("female","female"))
    type = (("d" ,"dog"),("c","cat"))
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media",default=None)
    species = models.CharField(max_length=100)
    price = models.FloatField(default="10")
    gender = models.CharField(max_length=30,choices=gender_option)
    age = models.IntegerField()
    animal_type = models.CharField(max_length=30,choices=type,default="NA")
    breed = models.CharField(max_length=100)
    description = models.TextField()

    class meta:
        db_table = "petTbL"

        


