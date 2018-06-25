from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CreateLoanForm
from django.shortcuts import redirect
from django.urls import reverse
from .utils.loan_calculators.loan_calculator import LoanCalculator
from django.apps import apps
from django.views.generic.edit import FormView

Loan = apps.get_model('loan_app', 'Loan')
Status = apps.get_model('loan_app', 'Status')
Profile = apps.get_model('profile_app', 'Profile')

#@login_required
class TakeLoan(FormView):
    template_name = 'loan_app/loan_create.html'
    form_class = CreateLoanForm
    context_name = 'create-loan'
    model = Loan
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(TakeLoan, self).get_form_kwargs()
        kwargs.update({
            'profile': Profile.objects.get(user=self.request.user)
        })
        return kwargs

    def form_valid(self, form):
        loan = form.save()
        loan_calc = LoanCalculator(loan)
        loan.expected_payment = loan_calc.calculate_expected_payment()
        loan.status = Status.objects.get(code=3)
        loan.profile_id = self.request.user.pk
        loan.pay_interest = loan_calc.calculate_interest()
        loan.save()
        return redirect('/')


take_loan = TakeLoan.as_view()