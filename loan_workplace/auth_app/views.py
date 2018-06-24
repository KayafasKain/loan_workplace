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
from .utils.classifiers.numerical_classifier import NumericalClassifier as NC

Profile = apps.get_model('profile_app', 'Profile')
ClientClass = apps.get_model('profile_app', 'ClientClass')

User = get_user_model()

class LoginView(FormView):
    template_name = 'auth_app/login.html'
    form_class = UserLoginForm
    context_object_name = 'login'
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)

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
        clas = NC(profile)
        profile.user = self.user_model.objects.get(pk=self.kwargs['pk'])
        profile.client_class = clas.get_user_class()
        profile.save()
        return redirect('/')

create_profile = CreateProfileView.as_view()