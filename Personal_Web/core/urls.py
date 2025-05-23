from django.urls import path
from .views import *

urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('about/',About.as_view(),name='about'),
    path('resume/',Resume.as_view(),name='resume'),
    path('contact/',Contact.as_view(),name='contact'),
]