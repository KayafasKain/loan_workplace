from django import forms
from django.apps import apps

Loan = apps.get_model('loan_app', 'Loan')
ClientClass = apps.get_model('profile_app', 'ClientClass')
LoanType = apps.get_model('loan_app', 'LoanType')

class CreateLoanForm(forms.ModelForm):
    closed = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Loan
        fields = [
            'amount',
            'closed',
            'type',
        ]

    def __init__ (self, *args, **kwargs):
        profile = kwargs.pop("profile")
        super(CreateLoanForm, self).__init__(*args, **kwargs)
        self.fields["type"].queryset = LoanType.objects.filter(client_classes=profile.client_class)

    def clean(self):
        pass