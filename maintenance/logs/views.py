from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from equipment.models import Location, Equipment, Part

# Create your views here.
def index(request):
    return HttpResponse("Maintenance homepage. Dash here should have tickets, reporting, PM activities")
