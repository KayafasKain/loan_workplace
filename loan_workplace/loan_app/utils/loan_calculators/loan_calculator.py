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
            self.amount_remain = self.amount + self.calculate_interest()
            self.status = loan.status
            self.profile = loan.profile
        else:
            raise ValueError('Please, provide Loan object')

    def get_amount_remain(self):
        return self.amount_remain

    def calculate_expected_payment(self):
        duration = self.end - self.start.date()
        duration = duration.days / 30
        return self.amount_remain/duration

    def calculate_interest(self):
        return (self.amount/100) * self.type.interest