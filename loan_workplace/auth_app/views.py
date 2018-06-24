from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from .forms import UserRegisterForm, UserLoginForm, ProfileRegisterForm
from django.apps import apps

Profile = apps.get_model('profile_app', 'Profile')
ClientClass = apps.get_model('profile_app', 'ClientClass')

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
    context_name = 'register'
    model = User

    def form_valid(self, form):
        try:
            user = self.model.objects.get(email=form.cleaned_data['email'])
        except self.model.DoesNotExist as e:
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()

        return HttpResponseRedirect(reverse('register-profile', kwargs={'pk': str(user.pk)}))

register = RegisterView.as_view()

class CreateProfileView(FormView): #Work In Progress
    template_name = 'auth_app/register_profile.html'
    form_class = ProfileRegisterForm
    context_name = 'register-profile'
    model = Profile
    user_model = User
    class_model = ClientClass

    def form_valid(self, form):
        try:
            profile = self.model.objects.get(user=self.kwargs['pk'])
        except self.model.DoesNotExist as e:
            profile = form.save()

        profile.user = self.user_model.objects.get(pk=self.kwargs['pk'])
        profile.client_class = self.class_model.objects.get(pk=1)#mock classification
        profile.save()
        return redirect('/')

create_profile = CreateProfileView.as_view()