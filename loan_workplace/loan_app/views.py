from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CreateLoan
from django.shortcuts import redirect
from .utils.loan_calculators.loan_calculator import LoanCalculator
from django.apps import apps
from django.views.generic.edit import FormView

Loan = apps.get_model('loan_app', 'Loan')
Profile = apps.get_model('profile_app', 'Profile')

#@login_required
class TakeLoan(FormView):
    template_name = 'loan_app/loan_create.html'
    form_class = CreateLoan
    context_name = 'create-loan'
    model = Loan
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = {'initial': self.get_initial()}
        kwargs.update({
            'profile': Profile.objects.get(user=self.request.user)
        })
        return kwargs

    def

    # def form_valid(self, form):
    #     loan = form.save(commit=False)
    #     loan_calc = LoanCalculator(loan)
    #     loan.expected_payment = loan_calc.calculate_expected_payment()
    #     print("-------=================------")
    #     print(loan)
    #     print(loan_calc.calculate_expected_payment())
    #     redirect('/')


take_loan = TakeLoan.as_view()