from django.db import models


class Computers(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    motherboard = models.CharField(max_length=250, null=False, blank=False)
    proccessor = models.CharField(max_length=250, null=False, blank=False)
    ram = models.CharField(max_length=250, null=False, blank=False)
    memory = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField()
    in_stock = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
