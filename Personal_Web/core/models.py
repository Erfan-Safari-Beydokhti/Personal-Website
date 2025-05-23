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
