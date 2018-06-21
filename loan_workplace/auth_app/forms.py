from django import forms

class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass