from django.db import models

# Create your models here.
class Location(models.Model):
	location_id = models.CharField(primary_key = True, max_length = 5)
	location_name = models.CharField(max_length = 50)

	def __str__(self):
		return '%s' % self.location_name

class Equipment(models.Model):
	# Primary key is auto-generated
	equipment_name = models.CharField(max_length = 100)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	manufacturer = models.CharField(max_length=50)
	purchase_date = models.DateField()
	serial_no = models.CharField(max_length=50)
	supplier = models.CharField(max_length=50)
	service_contact = models.TextField()

class Part(models.Model):
	part_name = models.CharField(max_length = 100)
	date_installed = models.DateTimeField()
	on_equipment = models.ForeignKey(Equipment, on_delete = models.CASCADE)
	supplier = models.CharField(max_length = 50)
	lead_time = models.DurationField()
