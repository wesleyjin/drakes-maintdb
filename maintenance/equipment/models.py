from django.db import models
from django.shortcuts import get_object_or_404


class Location(models.Model):
    location_id = models.CharField(primary_key=True, max_length=5)
    location_name = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % self.location_name


class Equipment(models.Model):
    # Primary key is auto-generated
    equipment_name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=50, blank=True)
    serial_no = models.CharField(max_length=50, blank=True)
    purchase_date = models.DateField(blank=True, null=True)
    supplier = models.CharField(max_length=50, blank=True)
    service_contact = models.TextField(blank=True)
    file = models.FileField(upload_to='equipment_files', blank=True, null=True)

    def __str__(self):
        return '%s' % self.equipment_name

    def get_location(self):
        loc = self.location
        return loc.location_id

#     Get tickets. get parts


class Part(models.Model):
    part_name = models.CharField(max_length=100)
    date_installed = models.DateTimeField(null=True, blank=True)
    on_equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=50, blank=True)
    supplier = models.CharField(max_length=50, blank=True)
    lead_time = models.DurationField(blank=True, null=True)

    def __str__(self):
        return '%s on %s' % (self.part_name,
                             Equipment.objects.get(pk=self.on_equipment).equipment_name)
