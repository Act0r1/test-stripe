from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()

    def get_price(self):
        return f"{self.price} $"

    def get_name(self):
        return f"Name: {self.name}" 

