from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.name, self.email)

class ResumeEntry(models.Model):
    title=models.CharField(max_length=100)
    company=models.CharField(max_length=100,blank=True)
    description=models.TextField(blank=True)
    start_date=models.DateField()
    end_date=models.DateField()
    is_current=models.BooleanField(default=False)
    category=models.CharField(max_length=100,choices=[
        ('work',"Work Experience"),
        ('education','Education'),
        ('project','Project'),
    ])
    def __str__(self):
        return self.title
class CertificateEntry(models.Model):
    title=models.CharField(max_length=100)
    issuer=models.CharField(max_length=100)
    issue_date=models.DateField()
    file=models.FileField(upload_to='certificates/',blank=True,null=True)
    url=models.URLField(blank=True)
    def __str__(self):
        return self.title


class AboutMe(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField()
    profile_picture=models.FileField(upload_to='about/',blank=True,null=True)
    skills=models.TextField(help_text="Comma-separated skills")
    def __str__(self):
        return self.name
