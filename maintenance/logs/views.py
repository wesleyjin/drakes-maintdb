from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Service, Log


# Create your views here.
def index(request):
    return HttpResponse("Maintenance homepage. Dash here should have tickets, reporting, PM activities")


class LogListView(generic.ListView):
    template_name = 'logs/logs_home.html'
    model = Log
    context_object_name = 'log_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    # def get_queryset(self):
    #     """Return all logs"""
    #     return Log.objects.order_by('-id')
