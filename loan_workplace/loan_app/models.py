from django.db import models
# from django.apps import apps
# ProfileModel = apps.get_model('profile_app', 'Profile')

class Loan(models.Model):
    amount = models.FloatField()
    given = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    closed = models.DateField(null=True, default=None)
    is_outdated = models.BooleanField(default=False, blank=True)
    expected_payment = models.FloatField(null=True, blank=True)
    type = models.ForeignKey('LoanType', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.ForeignKey('Status', null=True, blank=True, on_delete=models.SET_NULL)
    profile = models.ForeignKey('profile_app.Profile', on_delete=models.CASCADE, null=True, blank=True)

class LoanType(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=256)
    interest = models.FloatField()
    penalty = models.FloatField(default=0)
    client_classes = models.ManyToManyField('profile_app.ClientClass')

    def __str__(self):
        return '{}'.format(self.name)


class Status(models.Model):
    name = models.CharField(max_length=32, unique=True)
    code = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return '{}'.format(self.name)

class Payments(models.Model):
    loan = models.ForeignKey('Loan', on_delete=models.CASCADE)
    amount = models.FloatField()
    is_suffise = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)