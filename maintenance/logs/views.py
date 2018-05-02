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
        context['recent_logs'] = Log.objects.all().order_by('created')[:5]
        context['upcoming_services'] = Service.objects.all()[:5]
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
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['extra'] = 'this'
        return context


class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = 'logs/service_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_logs'] = context['service'].get_log_set()
        return context
