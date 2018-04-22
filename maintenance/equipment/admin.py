from django.contrib import admin
from .models import Location, Equipment, Part


class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'location_id')


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('equipment_name', 'location')
    list_filter = ['location']


class PartAdmin(admin.ModelAdmin):
    list_display = ('part_name', 'on_equipment', 'date_installed')
    list_filter = ['date_installed']


admin.site.register(Location, LocationAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Part, PartAdmin)