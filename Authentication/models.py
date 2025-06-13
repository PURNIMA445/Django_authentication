from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=15, blank=True)
    role = models.CharField(max_length=10, choices=[('tenant', 'Tenant'), ('landlord', 'Landlord')])

# Create your models here.
