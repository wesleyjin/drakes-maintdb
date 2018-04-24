from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from equipment.models import Equipment


# Create your models here.

class Service(models.Model):
    """
    A record of all the preventative maintenance SERVICEs that need to be repeated for
    desired frequency (weekly, monthly, annually, etc.)
    """
    FREQUENCY_CHOICES = (
        ('daily', _('Daily')),
        ('weekly', _('Weekly')),
        ('monthly', _('Monthly')),
        ('quarterly', _('Quarterly')),
        ('semiannually', _('Semi-annually')),
        ('annually', _('Annually')),
        ('2years', _('2 Years')),
        ('4years', _('4 Years')),
    )

    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE
    )

    description = models.CharField(
        max_length=150,
        help_text='150 character limit description of maintenance service'
    )

    frequency = models.CharField(
        _('Service Frequency'),
        max_length=20,
        choices=FREQUENCY_CHOICES
    )

    def __str__(self):
        return '%s: %s ' % (self.equipment, self.description)


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
        help_text='Type of log: breakdown, PM, issue, request, other'
    )

    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE
    )

    summary = models.CharField(
        _('Summary of work done/issue'),
        max_length=200
    )

    description = models.TextField(
        help_text=_('Please be as descriptive as possible and include all details.')
    )

    issue_datetime = models.DateTimeField(
        help_text=_('Date and time of estimated start of issue or maintenance work'),
        blank=True,
        null=True
    )

    resolved = models.BooleanField(
        default=False
    )

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assigned_to',
        blank=True,
        null=True,
        help_text='Person responsible for log activity.'
    )

    resolved_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='resolved_by',
        blank=True,
        null=True,
        help_text='Person closing the log'
    )

    resolved_datetime = models.DateTimeField(
        help_text='Time machine was ready for production',
        blank=True,
        null=True
    )

    services = models.ManyToManyField(
        Service,
        help_text='Scheduled maintenance services completed with this log',
        blank=True
    )

    # verbose_name attribute if needed

    class Meta:
        get_latest_by = 'created'

    def __str__(self):
        return '%s %s' % (self.id, self.summary)
