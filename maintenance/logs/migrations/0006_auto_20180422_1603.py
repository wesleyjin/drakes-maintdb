# Generated by Django 2.0.3 on 2018-04-22 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0005_auto_20180422_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='type',
            field=models.CharField(choices=[('pm', 'Preventative Maintenance'), ('breakdown', 'Equipment Breakdown'), ('request', 'Maintenance Request'), ('issue', 'Issue with equipment'), ('other', 'Other')], default='pm', help_text='Type of log: breakdown, PM, issue, request, other', max_length=10, verbose_name='Log Type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='log',
            name='services',
            field=models.ManyToManyField(blank=True, help_text='Scheduled maintenance services completed with this log', to='logs.Service'),
        ),
    ]