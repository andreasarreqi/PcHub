from django.db import models


class Contact(models.Model):
    """
    Defines the contact model in our database
    """
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    sent = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name
