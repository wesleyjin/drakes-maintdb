from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Location, Equipment, Part


def index(request):
    return HttpResponse("Equipment homepage. Navigate to equipment/locations to see what we have so far.")


class LocationListView(generic.ListView):
    template_name = 'equipment/location_list.html'
    context_object_name = 'plant_locations'

    def get_queryset(self):
        """Return all locations"""
        return Location.objects.order_by('location_name')


# def plant_locations(request):
# 	location_list = Location.objects.order_by('location_name')
# 	context = {'plant_locations': location_list}
# 	return render(request,'equipment/location_list.html', context)

def location(request, location_id):
    loc = get_object_or_404(Location, pk=location_id)
    equipment_list = list(Equipment.objects.filter(location=loc.location_id))
    context = {'location': loc, 'equipments': equipment_list}
    return render(request, 'equipment/location_detail.html', context)


class EquipmentListView(generic.ListView):
    template_name = 'equipment/equipment_list.html'
    context_object_name = 'equipments'

    def get_queryset(self):
        """Return all equipment"""
        return Equipment.objects.order_by('equipment_name')


class EquipmentView(generic.DetailView):
    model = Equipment
    template_name = 'equipment/equipment_detail.html'


def info(request, equipment_id):
    response = "You're looking at the info page of equipment %s"
    return HttpResponse(response % equipment_id)
