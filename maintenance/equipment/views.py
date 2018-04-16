from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse
from .models import Location, Equipment, Part


def index(request):
	location_list = Location.objects.order_by('location_name')
	context = {'plant_locations': location_list}
	return render(request,'equipment/locations.html', context)

def location(request, location_id):
	loc = get_object_or_404(Location, pk = location_id)
	return HttpResponse("You're looking at location %s" % loc.location_name)

def info(request, equipment_id):
	response = "You're looking at the info page of equipment %s"
	return HttpResponse(response % equipment_id)