from django.db import models
# from django.apps import apps
# ProfileModel = apps.get_model('profile_app', 'Profile')

class Loan(models.Model):
    amount = models.FloatField()
    given = models.DateField()
    closed = models.DateField()
    is_outdated = models.BooleanField(default=False)
    expected_payment = models.FloatField()
    type = models.ForeignKey('LoanType', null=True, on_delete=models.SET_NULL)
    status = models.ForeignKey('Status', null=True, on_delete=models.SET_NULL)
    profile = models.ForeignKey('profile_app.Profile', on_delete=models.CASCADE)

class LoanType(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=256)
    interest = models.FloatField()
    penalty = models.FloatField

class Status(models.Model):
    name = models.CharField(max_length=32, unique=True)
    code = models.CharField(max_length=32, unique=True)

class Payments(models.Model):
    loan = models.ForeignKey('Loan', on_delete=models.CASCADE)
    amount = models.FloatField()
    is_suffise = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)