# Generated by Django 3.1.1 on 2020-09-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_timeavailabilitymodel_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeavailabilitymodel',
            name='day2',
            field=models.DateField(blank=True, help_text='Fecha 2 disponiblidad', null=True, verbose_name='Día 2'),
        ),
    ]