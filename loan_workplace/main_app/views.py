from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    template_name = "main_app/index.html"
    context_name = 'index-page'

index = HomePageView.as_view()