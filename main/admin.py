from django.contrib import admin

from main.models import CareerModel, MeshModel, ContractModel, TeacherModel, TermModel, \
    SubjectModel, SubjectMeshModel, TimeAvailabilityModel, ParallelModel, PlanModel
from main.models.classroom import ClassRoomModel


class TimeAvailabilitySetModelAdmin(admin.TabularInline):
    model = TimeAvailabilityModel
    fields = ("term", "teachers", "num_start_day", "num_end_day", "start_time", "end_time")
    raw_id_fields = ('term', 'teachers')


@admin.register(SubjectMeshModel)
class SubjectMeshModelAdmin(admin.ModelAdmin):
    model = SubjectMeshModel
    search_fields = ["subject__code", "subject__name"]
    list_display = ("subject", "level", "status")
    list_editable = ["level", ]
    fields = ("subject", "level",)
    raw_id_fields = ("subject",)


class TeacherModelSetModelAdmin(admin.TabularInline):
    model = TeacherModel
    fields = ("full_name", "alias", "skill", "contract", "career")
    raw_id_fields = ('contract', 'career')


class MeshModelSetModelAdmin(admin.TabularInline):
    model = MeshModel
    fields = ("name", "year", "subject_mesh")


@admin.register(CareerModel)
class CareerModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'status')
    ordering = ('created',)
    list_filter = ('status',)
    search_fields = ('name', 'code')
    # fields = ('name', 'code')

    fieldsets = (
        ("INFORMACIÓN BÁSICA", {
            "fields": (
                "name", "code", "alias"
            ),
        }),
    )
    inlines = [
        # MeshModelSetModelAdmin,
        TeacherModelSetModelAdmin
    ]
    list_per_page = 20


@admin.register(ContractModel)
class ContractModelAdmin(admin.ModelAdmin):
    fields = ('name', 'code')
    list_filter = ('status',)
    search_fields = ('name', 'code')
    ordering = ('created',)


@admin.register(TeacherModel)
class TeacherModelAdmin(admin.ModelAdmin):
    fields = ('contract', 'full_name', 'alias', 'career', 'skill', 'affinity')
    raw_id_fields = ('contract', 'career')
    list_display = ('full_name', 'alias', 'contract', 'skill', 'affinity', 'status')
    search_fields = (
        'full_name', 'alias',
        'contract__code',
        'contract__name',
        'career__code',
        'career__name'
    )
    list_filter = ('career__code', 'contract__code', 'status')
    list_editable = ('status',)
    inlines = [TimeAvailabilitySetModelAdmin]
    list_per_page = 20


@admin.register(MeshModel)
class MeshModelAdmin(admin.ModelAdmin):
    fields = ('name', 'career', 'year')
    raw_id_fields = ('career',)
    list_display = ('name', 'career', 'year')
    search_fields = ('career__code', 'career__name', 'name')
    list_filter = ('career__code',)


@admin.register(TermModel)
class TermModelAdmin(admin.ModelAdmin):
    fields = ('name', 'year')
    list_display = ('name', 'year', 'status')
    list_filter = ('year', 'status')


@admin.register(ClassRoomModel)
class ClassRoomModelAdmin(admin.ModelAdmin):
    fields = ('name', 'code', 'capacity', 'affinity')
    search_fields = ('name', 'code')
    list_filter = ('capacity', 'affinity')
    list_per_page = 20


@admin.register(SubjectModel)
class SubjectModelAdmin(admin.ModelAdmin):
    search_fields = ("name", "code")
    list_per_page = 15
    fieldsets = (
        (
            "INFORMACIÓN BÁSICA", {
                "fields": (
                    "name", "code", "status"
                ),
            }
        ),
    )


@admin.register(TimeAvailabilityModel)
class TimeAvailabilityModelModelAmin(admin.ModelAdmin):
    fields = ('teachers', 'term', 'day', 'start_time', 'end_time')
    list_display = ('teachers', 'term', 'num_start_day', 'num_end_day', 'start_time', 'end_time', "status")
    list_editable = ("status",)
    search_fields = ('teachers__name', 'term__name',)
    raw_id_fields = ('teachers', 'term')
    list_filter = ('term',)
    list_per_page = 20


@admin.register(ParallelModel)
class ParallelModelAdmin(admin.ModelAdmin):
    fields = ('name', 'code', 'term', 'plan', 'teacher', 'subject_mesh', 'classroom')
    raw_id_fields = ('plan', 'term', 'teacher', 'subject_mesh', 'classroom')
    search_fields = ("name", "code")
    list_display = ('name', 'code', 'plan', 'term')
    list_filter = ('term',)
    list_per_page = 20


@admin.register(PlanModel)
class PlanModelAdmin(admin.ModelAdmin):
    fields = ('term', 'career', 'state', 'status',)
    raw_id_fields = ('term', 'career',)
    list_display = ('term', 'career', 'state', 'status')
    list_filter = ('term',)
    list_editable = ('status', 'state')
    list_per_page = 20
