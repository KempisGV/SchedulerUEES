# Generated by Django 3.1.1 on 2020-09-01 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20200830_0353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subjectmeshmodel',
            options={'verbose_name': 'Materia Malla', 'verbose_name_plural': 'Materias Malla'},
        ),
        migrations.AlterField(
            model_name='subjectmeshmodel',
            name='mesh',
            field=models.ForeignKey(blank=True, help_text='Malla nivel', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='level', to='main.meshmodel', verbose_name='Malla'),
        ),
        migrations.CreateModel(
            name='ParallelModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted_at')),
                ('status', models.BooleanField(default=True, help_text='Status the object has currently', verbose_name='status')),
                ('creator', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modifier', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_parallels', to='main.planmodel', verbose_name='Planificación')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parallels', to='main.subjectmodel', verbose_name='Aula')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='main.teachermodel', verbose_name='Profesor')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='term_parallels', to='main.termmodel', verbose_name='Periodo')),
            ],
            options={
                'verbose_name': 'Paralelo',
                'verbose_name_plural': 'Paralelos',
                'db_table': 'paralelo',
            },
        ),
        migrations.CreateModel(
            name='ClassRoomModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted_at')),
                ('status', models.BooleanField(default=True, help_text='Status the object has currently', verbose_name='status')),
                ('name', models.CharField(help_text='Nombres completos', max_length=200, verbose_name='Nombres')),
                ('code', models.CharField(help_text='Código referencial del contrato. Ej: A01-2', max_length=10, verbose_name='Codigo')),
                ('capacity', models.PositiveSmallIntegerField(verbose_name='Capacidad')),
                ('affinity', models.CharField(max_length=70, verbose_name='Afinidad')),
                ('creator', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modifier', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Aula',
                'verbose_name_plural': 'Aulas',
                'db_table': 'aula',
            },
        ),
    ]
