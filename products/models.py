from django.db import models
from django.conf import settings

# from accounts.models import User

User = settings.AUTH_USER_MODEL


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=False)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)

    class Meta:
        verbose_name = 'Product'

    def __str__(self):
        return str(self.id)
