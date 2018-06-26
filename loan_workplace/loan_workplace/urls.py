"""loan_workplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from auth_app import views as auth_views
from loan_app import views as loan_views
from profile_app import views as profile_views
from main_app import views as main_views
from django.contrib.auth.decorators import login_required
#loan_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name = 'index-page'),
    path('register/', auth_views.register, name='register'),
    path('loan/take/', login_required(loan_views.take_loan), name='create-loan'),
    path('loan/list/', login_required(loan_views.loan_list), name='loan-list'),
    path('loan/pay/<str:pk>', login_required(loan_views.loan_pay), name='loan-pay'),
    path('create_profile/', auth_views.create_profile , name = 'register-profile'),
    path('profile/edit/',login_required(profile_views.edit_profile), name = 'edit-profile'),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout')
]
