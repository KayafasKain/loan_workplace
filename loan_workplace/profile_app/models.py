from django.db import models
from django.conf import settings

class Profile(models.Model):
    income_yearly = models.FloatField()
    employer_name = models.CharField(max_length=64)
    birth_date = models.DateField()
    last_loan_taken = models.DateField()
    last_loan_paid = models.DateField()
    profile_updated = models.DateField()
    emplyment_type = models.ForeignKey('EmploymentType', null=True, on_delete=models.SET_NULL)
    client_class = models.ForeignKey('ClientClass', null=True, on_delete=models.SET_NULL)

class Contact(models.Model):
    name = models.CharField(max_length=32)
    value = models.CharField(max_length=64)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

class EmploymentType(models.Model):
    name = models.CharField(max_length=64, unique=True)
    descriptinon = models.CharField(max_length=128)

class ClientClass(models.Model):
    name = models.CharField(max_length=64, unique=True)
    descriptinon = models.CharField(max_length=128)

