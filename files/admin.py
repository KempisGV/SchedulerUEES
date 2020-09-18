from django.contrib import admin

# Register your models here.
# from files.models import FilVersionModel, FilVersionDetailModel, IbmScheduleModel
#
#
# class FilVersionDetailModelAdmin(admin.TabularInline):
#     model = FilVersionDetailModel
#     fields = ("name_file", "type_file", "generate_file")
#     ordering = ("created",)
#
#
# @admin.register(FilVersionModel)
# class FileVersionModelAdmin(admin.ModelAdmin):
#     raw_id_fields = ('plan',)
#     fields = ("version", "plan", "academic_period", "generation_date")
#     list_display = ("plan", "version", "generation_date", "academic_period")
#     list_filter = ("status",)
#     ordering = ("created",)
#     inlines = [FilVersionDetailModelAdmin]
#
#
# @admin.register(IbmScheduleModel)
# class IbmScheduleModelAdmin(admin.ModelAdmin):
#     raw_id_fields = ('file_version',)
#     fields = ("file_version", "day_week", "start_time", "end_time", "assigned_teacher", "assigned_classroom")
#     list_display = ("file_version", "day_week", "start_time", "end_time")
#     list_filter = ("status",)
#     ordering = ("created",)
