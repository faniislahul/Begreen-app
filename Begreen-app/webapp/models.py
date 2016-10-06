from django.db import models

# Create your models here.

class categories(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 1000, default = None)
    pic = models.CharField(max_length = 500, default = None)
    
    def __str__(self):
        return self.name

class subcategories(models.Model):
    name = models.CharField(max_length = 100)
    parent = models.ForeignKey(categories, on_delete = models.CASCADE)
    description = models.TextField(max_length = 1000, default = None)
    pic = models.CharField(max_length = 500, default = None)
    
    def __str__(self):
        return self.name

class products(models.Model):
    name = models.CharField(max_length = 100)
    price1 = models.IntegerField(default = 0)
    price2 = models.IntegerField(default = 0)
    price3 = models.IntegerField(default = 0)
    is_stockable = models.BooleanField(default = False)
    SKU = models.CharField(max_length = 32, default = None)
    description = models.TextField(max_length = 1000)
    pic = models.CharField(max_length = 500 , default = None)
    category = models.ForeignKey(subcategories, on_delete = models.CASCADE)
    def __str__(self):
        return self.name


class stockable(models.Model):
    items = models.ForeignKey(products, on_delete = models.CASCADE)
    stock = models.IntegerField(default = 0)