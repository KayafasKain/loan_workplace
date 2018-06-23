from django.contrib import admin

# Register your models here.
from django.apps import apps

Loan = apps.get_model('loan_app', 'Loan')
LoanType = apps.get_model('loan_app', 'LoanType')
Status = apps.get_model('loan_app', 'Status')
Payments = apps.get_model('loan_app', 'Payments')

admin.site.register(Loan)
admin.site.register(LoanType)
admin.site.register(Status)
admin.site.register(Payments)
