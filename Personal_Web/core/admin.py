from django.contrib import admin
from .models import ContactMessage,ResumeEntry,CertificateEntry
admin.site.register(ContactMessage)
admin.site.register(ResumeEntry)
admin.site.register(CertificateEntry)

# Register your models here.
