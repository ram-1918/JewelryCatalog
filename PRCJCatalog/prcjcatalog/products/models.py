from django.db import models
from users.models import Users

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Products(models.Model):
    values = (("gold", "Gold"), ("silver", "Silver"))
    name = models.CharField(max_length = 255)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name = "category_set", on_delete = models.CASCADE)
    type = models.CharField(choices = values, max_length = 10, default = "Gold")
    weight = models.FloatField()
    image = models.ImageField(upload_to = "images/")

    def __str__(self):
        return self.name + " " + str(self.weight)

    # use the function name to while accessing image "imageURL"
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class GoldPrice(models.Model):
    gold = models.FloatField(default = 1927.32)
    date_added = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return str(self.gold)

class Price(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='price')
    gold_price = models.ForeignKey(GoldPrice, related_name= "goldPrice", on_delete = models.CASCADE)
    #price = models.FloatField(default = 0, blank = True)

    # "get_product_price" returns calculated total price of product
    @property
    def get_product_price(self):
        return self.product.weight*self.gold_price.gold

    # def save(self, *args, **kwargs):
    #     self.price = self.product.weight * self.gold_price.gold
    #     super(Price, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.product.name