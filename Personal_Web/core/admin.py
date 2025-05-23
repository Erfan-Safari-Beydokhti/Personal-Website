from django.contrib import admin
from .models import ContactMessage,ResumeEntry,CertificateEntry,AboutMe

admin.site.register(ContactMessage)
admin.site.register(ResumeEntry)
admin.site.register(CertificateEntry)
admin.site.register(AboutMe)
# Register your models here.
