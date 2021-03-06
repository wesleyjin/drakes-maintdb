from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from equipment.models import Equipment
from django.utils import timezone
from datetime import timedelta


class Service(models.Model):
    """
    A record of all the preventative maintenance services that need to be repeated for
    desired frequency (weekly, monthly, annually, etc.)
    """
    created = models.DateTimeField(auto_now_add=True)

    FREQUENCY_CHOICES = (
        ('daily', _('Daily')),
        ('weekly', _('Weekly')),
        ('monthly', _('Monthly')),
        ('quarterly', _('Quarterly')),
        ('semiannually', _('Semi-annually')),
        ('annually', _('Annually')),
        ('2years', _('2 Years')),
        ('4years', _('4 Years')))

    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE)

    description = models.CharField(
        max_length=150,
        help_text='150 character limit description of maintenance service')

    notes = models.TextField(
        help_text=_('Any additional details regarding the maintenance service.'),
        blank=True)

    frequency = models.CharField(
        _('Service Frequency'),
        max_length=20,
        choices=FREQUENCY_CHOICES)

    def __str__(self):
        return '%s: %s ' % (self.equipment, self.description)

    def get_log_set(self):
        return self.log_set.all()

    def has_resolved_logs(self):
        return self.log_set.filter(resolved=True, resolved_datetime__isnull=False).count() > 0

    def get_last_service_time(self):
        last_log = self.log_set.latest()
        return last_log.resolved_datetime

    def time_since_last_service(self):
        if self.has_resolved_logs():
            delta = timezone.now() - self.get_last_service_time()
        else:
            return 'No logs recorded for service.'
        return delta

    def days_since_last_service(self):
        return self.time_since_last_service().days

    def due_for_service(self):
        if not self.has_resolved_logs():
            return True
        elif self.frequency == 'daily':
            return timedelta(days=1) < self.time_since_last_service()
        elif self.frequency == 'weekly':
            return timedelta(weeks=1) < self.time_since_last_service()
        elif self.frequency == 'monthly':
            return timedelta(weeks=4.345) < self.time_since_last_service()
        elif self.frequency == 'quarterly':
            return timedelta(weeks=13) < self.time_since_last_service()
        elif self.frequency == 'semiannually':
            return timedelta(weeks=26) < self.time_since_last_service()
        elif self.frequency == 'annually':
            return timedelta(weeks=52) < self.time_since_last_service()
        elif self.frequency == '2years':
            return timedelta(weeks=104) < self.time_since_last_service()
        elif self.frequency == '4years':
            return timedelta(weeks=208) < self.time_since_last_service()


class Log(models.Model):
    """
    To allow a log to be entered as quickly and efficiently as possible, only the bare minimum
    fields are required. The necessary fields allow us to sort and manage the ticket. User can
    come back to edit description with notes, contacts, and information about the resolving
    employee and resolved date.
    """
    TYPE_CHOICES = (
        ('pm', _('Preventative Maintenance')),
        ('breakdown', _('Equipment Breakdown')),
        ('request', _('Maintenance Request')),
        ('issue', _('Issue with equipment')),
        ('other', _('Other'))
    )

    # Date of ticket creation
    created = models.DateTimeField(auto_now_add=True)

    type = models.CharField(
        _('Log Type'),
        max_length=10,
        choices=TYPE_CHOICES,
        help_text='Type of log: breakdown, PM, issue, request, other')

    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE)

    summary = models.CharField(
        help_text=_('The title of the log entry. Summary of work done/issue'),
        max_length=200)

    description = models.TextField(
        help_text=_('Please be as descriptive as possible and include all details.'))

    file = models.FileField(
        upload_to='log_files/',
        help_text='Any file or image associated with this log.',
        blank=True,
        null=True)

    issue_datetime = models.DateTimeField(
        help_text=_('Date and time of estimated start of issue or maintenance work'),
        blank=True,
        null=True)

    resolved = models.BooleanField(
        default=False)

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assigned_to',
        blank=True,
        null=True,
        help_text="Person responsible for this log's activity & data.")

    resolved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='resolved_by',
        blank=True,
        null=True,
        help_text='Person closing the log')

    resolved_datetime = models.DateTimeField(
        help_text='Time machine was ready for production',
        blank=True,
        null=True)

    services = models.ManyToManyField(
        Service,
        help_text='Scheduled maintenance services completed with this log',
        blank=True)

    class Meta:
        get_latest_by = 'resolved_datetime'
        ordering = ['-id']

    def __str__(self):
        return '%s %s' % (self.id, self.summary)

    def has_services(self):
        return self.services.all().count() > 0

    def get_services(self):
        return self.services.all()

