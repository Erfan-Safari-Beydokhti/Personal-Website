from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('about/',About.as_view(),name='about'),
    path('resume/',Resume.as_view(),name='resume'),
    path('contact/',Contact.as_view(),name='contact'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)