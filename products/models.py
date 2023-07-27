from django.db import models
from profiles.models import User


class Computers(models.Model):
    """
    The computers database model holding all the data descriping the computers
    """
    name = models.CharField(max_length=250, null=False, blank=False)
    motherboard = models.CharField(max_length=250, null=False, blank=False)
    proccessor = models.CharField(max_length=250, null=False, blank=False)
    ram = models.CharField(max_length=250, null=False, blank=False)
    memory = models.CharField(max_length=250, null=False, blank=False)
    in_stock = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    operating_system = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Monitors(models.Model):
    """
    The Monitors database model holding all the data descriping the monitors
    """
    name = models.CharField(max_length=150, null=False, blank=False)
    screen_size = models.CharField(max_length=50, null=False, blank=False)
    in_stock = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)


class Reviews(models.Model):
    """
    The review class defining all the database structure of the model
    """
    post = models.ForeignKey(Computers,
                             on_delete=models.CASCADE,
                             related_name="comments")
    name = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name="user")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
