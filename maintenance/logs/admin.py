from django.contrib import admin
from .models import Service, Log


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('description', 'equipment', 'frequency')
    list_filter = ['frequency']


class LogAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'equipment', 'resolved']
    list_filter = ['created', 'resolved']


admin.site.register(Log, LogAdmin)
admin.site.register(Service, ServiceAdmin)
