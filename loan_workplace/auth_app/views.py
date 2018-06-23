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
    context_name = 'create-user'
    success_url = '/'
    model = User

    def form_valid(self, form):
        try:
            user = self.model.objects.get(email=form.cleaned_data['email'])
        except self.model.DoesNotExist as e:
            user = form.save()
        return redirect(reverse('create-profile', kwargs={'pk': str(user.pk)}))

register = RegisterView.as_view()

class CreateProfileView(FormView): #Work In Progress
    template_name = 'auth_app/register_profile.html'
    form_class = ProfileRegisterForm
