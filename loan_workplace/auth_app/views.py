from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.views.generic.edit import FormView
from .forms import UserRegisterForm, UserLoginForm, ProfileRegisterForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_form'] = ProfileRegisterForm
        return context

register = RegisterView.as_view()