from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse
from .models import Location, Equipment, Part

def index(request):
	return HttpResponse("Equipment homepage. Navigate to equipment/locations to see what we have so far.")

def plant_locations(request):
	location_list = Location.objects.order_by('location_name')
	context = {'plant_locations': location_list}
	return render(request,'equipment/locationdash.html', context)

def location(request, location_id):
	loc = get_object_or_404(Location, pk = location_id)
	equipment_list = list(Equipment.objects.filter(location = loc.location_id))
	context = {'location': loc, 'equipments': equipment_list}
	return render(request, 'equipment/locationinfo.html', context)

def info(request, equipment_id):
	response = "You're looking at the info page of equipment %s"
	return HttpResponse(response % equipment_id)