# Generated by Django 2.0.3 on 2018-04-22 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0004_auto_20180422_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='frequency',
            field=models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'), ('quarterly', 'Quarterly'), ('semiannually', 'Semi-annually'), ('annually', 'Annually'), ('2years', '2 Years'), ('4years', '4 Years')], max_length=20, verbose_name='Service Frequency'),
        ),
    ]