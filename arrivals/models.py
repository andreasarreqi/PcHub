from django.db import models


class Arrivals(models.Model):
    """
    The Arrivals database model holding all the data describing the arrivals
    """
    name = models.CharField(max_length=250, null=False, blank=False)
    product_type = models.CharField(max_length=300, blank=False, null=False)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
