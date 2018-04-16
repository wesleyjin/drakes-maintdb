from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the equipment index.")

def location(request, location_id):
	return HttpResponse("You're looking at location %s" % location_id)

def info(request, equipment_id):
	response = "You're looking at the info page of equipment %s"
	return HttpResponse(response % equipment_id)