# admin.py
from django.contrib import admin
from .models import ConsultationRequest

@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'submitted_at')
    search_fields = ('name', 'email', 'service')
