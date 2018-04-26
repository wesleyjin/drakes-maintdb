from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Service, Log


# Create your views here.
def index(request):
    return HttpResponse("Maintenance homepage. Dash here should have tickets, reporting, PM activities")


class HomepageView(generic.TemplateView):
    template_name = 'logs/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['extra'] = extra object
        return context


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


class LogDetailView(generic.DetailView):
    model = Log
    template_name = 'logs/log_detail.html'


class ServiceListView(generic.ListView):
    template_name = 'logs/service_home.html'
    model = Service
    context_object_name = 'service_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['extra'] = 'this'
        return context


class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = 'logs/service_detail.html'
