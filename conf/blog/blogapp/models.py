# models.py
from django.db import models

class ConsultationRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    service = models.CharField(max_length=50, choices=[
        ('Business Services', 'Business Services'),
        ('Consumer Product', 'Consumer Product'),
        ('Financial Services', 'Financial Services'),
        ('Software Research', 'Software Research'),
    ])
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"
