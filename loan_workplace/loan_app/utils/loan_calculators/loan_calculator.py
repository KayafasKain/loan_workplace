from datetime import datetime
from django.apps import apps

LoanType = apps.get_model('loan_app', 'LoanType')

class LoanCalculator:

    def __init__(self, loan=None):
        if loan is not None:
            self.amount = loan.amount
            self.start = loan.given
            self.end = loan.closed
            self.type = loan.type
            self.status = loan.status
            self.profile = loan.profile
        else:
            raise ValueError('Please, provide Loan object')


    def calculate_expected_payment(self):
        duration = self.end - self.start.date()
        duration = duration.days / 30
        return self.amount/duration

    def calculate_interest(self):
        return (self.amount/100) * self.type.interest