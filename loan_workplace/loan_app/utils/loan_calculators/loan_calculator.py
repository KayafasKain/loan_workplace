import datetime

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
        duration = self.start.datetime.now().date() - self.end
        duration = duration.days / 30
        return self.amount/duration