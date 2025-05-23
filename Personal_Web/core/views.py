from django.shortcuts import render
from django.views.generic import TemplateView
from templates import *

# Create your views here.
class Home(TemplateView):
    template_name = "core/home.html"

class About(TemplateView):
    template_name = "core/about.html"

class Resume(TemplateView):
    template_name = "core/resume.html"