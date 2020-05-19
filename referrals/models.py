from django.db import models
from django.conf import settings
from datetime import datetime
from products.models import Product

User = settings.AUTH_USER_MODEL

'''
    a User can refer multiple products
'''


# class Refer(models.Model):

#    referrer = models.ForeignKey(User, related_name='referrer', on_delete=models.CASCADE)
#    referred = models.ForeignKey(User, related_name='referral', on_delete=models.CASCADE)
#    product = models.ForeignKey(Product, on_delete=models.CASCADE)

#    class Meta:
#        verbose_name = "Refer"
#        verbose_name_plural = "Refers"

#    def __str__(self):
#        return str(self.referrer.id)


class Refer(models.Model):
    invited = models.ForeignKey(User, related_name='invited', null=True, on_delete=models.CASCADE)
    inviter = models.ForeignKey(User, related_name='inviter', null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE)
    ref_id = models.CharField(max_length=120, default='ABC', unique=True)
    ip_address = models.CharField(max_length=120, default='ABC')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name}-invitation by {self.inviter.email}"

        class Meta:
            unique_together = ("invited", "ref_id",)
