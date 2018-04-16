from django.contrib import admin
from .models import Location, Equipment, Part

# Register your models here.
admin.site.register(Location)
admin.site.register(Equipment)
admin.site.register(Part)