from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.http import QueryDict
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from .forms import UserRegisterForm, UserLoginForm, ProfileRegisterForm
from django.apps import apps

Profile = apps.get_model('profile_app', 'Profile')

User = get_user_model()

class LoginView(FormView):
    template_name = 'auth_app/login.html'
    form_class = UserLoginForm
    context_object_name = 'login'
    success_url = '/'

login = LoginView.as_view()

class RegisterView(FormView):
    template_name = 'auth_app/register.html'
    form_class = UserRegisterForm
    success_url = '/'

    # def get_success_url(self):
    #     email = self.request.POST['email']
    #     print(email)
    #     email_qs = User.objects.filter(email=email)
    #     return redirect('/short/' + str(link.pk))

    def post(self, request, *args, **kwargs):

        qdict = QueryDict('', mutable=True)
        dict = {
                'username': request.POST['username'],
                'email': request.POST['email'],
                'password': request.POST['password']
            }
        qdict.update(dict)
        print(qdict)
        user_form = UserRegisterForm(qdict)
        profile_form = ProfileRegisterForm({
                'income_yearly': request.POST['income_yearly'],
                'employer_name': request.POST['employer_name'],
                'birth_date': request.POST['birth_date'],
                'client_class': None,
                'employment_type': request.POST['employment_type'],
                'user': None
            })
        if user_form.is_valid():
            print("NICE")
        print("ERROR")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = ProfileRegisterForm
        return context

register = RegisterView.as_view()