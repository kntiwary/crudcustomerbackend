from django.db import models

# from company.models import Company
# Create your models here.

# from starlly.models import Clienttype
from django.core.validators import URLValidator
from django.db.models.fields import EmailField


class Customer(models.Model):
    customer_name = models.CharField(max_length=225,
                                     help_text=("alphanumeric identifier"),null=False,blank=False)
    contact_number = models.CharField(unique=True,null=True,blank=True,max_length=17)
    email = EmailField(max_length=30)
    address = models.CharField(max_length=100, blank=True, null=True, help_text="string")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.customer_name