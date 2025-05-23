
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy
from .models import ContactMessage,CertificateEntry,ResumeEntry
# Create your views here.
class Home(TemplateView):
    template_name = "core/home.html"

class About(TemplateView):
    template_name = "core/about.html"

class Resume(TemplateView):
    template_name = "core/resume.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["entries"]=ResumeEntry.objects.all()
        context["certificates"]=CertificateEntry.objects.all()
        return context

class Contact(FormView):
    model=ContactMessage
    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


