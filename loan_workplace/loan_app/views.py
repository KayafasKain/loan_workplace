from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CreateLoanForm, LoanPayForm
from django.shortcuts import redirect
from django.urls import reverse
from .utils.loan_calculators.loan_calculator import LoanCalculator
from django.apps import apps
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, RedirectView

Loan = apps.get_model('loan_app', 'Loan')
Status = apps.get_model('loan_app', 'Status')
Profile = apps.get_model('profile_app', 'Profile')
Payments = apps.get_model('loan_app', 'Payments')

class LoanList(ListView):
    model = Loan
    template_name = 'loan_app/loan_list.html'
    context_object_name = 'loan-list'
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.filter(profile=Profile.objects.get(user=self.request.user).pk)

loan_list = LoanList.as_view()

class LoanPay(FormView):
    form_class = LoanPayForm
    template_name = 'loan_app/loan_pay.html'
    context_name = 'loan-pay'
    model = Payments
    success_url = '/loan/list/'

    def form_valid(self, form):
        loan = Loan.objects.get(pk=self.kwargs['pk'])
        obj = form.save()
        obj.loan = loan
        if loan.expected_payment <= obj.amount:
            obj.is_suffise = True
        loan.amount_remain -= obj.amount
        loan.save()
        obj.save()
        return redirect(reverse('loan-list'))

loan_pay = LoanPay.as_view()

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
        loan.amount_remain = loan_calc.get_amount_remain()
        loan.expected_payment = loan_calc.calculate_expected_payment()
        loan.status = Status.objects.get(code=3)
        loan.profile_id = Profile.objects.get(user=self.request.user).pk
        loan.pay_interest = loan_calc.calculate_interest()
        loan.save()
        return redirect(reverse('loan-list'))


take_loan = TakeLoan.as_view()