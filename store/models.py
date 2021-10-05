from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='photos/', height_field=None, width_field=None)
    price =  models.DecimalField(max_digits=7, decimal_places=2)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def image_url(self):
        return self.image.url

    
