""""""
from django import forms
from django.forms.formsets import BaseFormSet

from main.models import SubjectModel, TeacherModel, ClassRoomModel, ParallelModel
from main.models.planning import PlanModel, LineItemScheduleModel


class BasicSchedulerForm(forms.ModelForm):
    class Meta:
        model = PlanModel
        exclude = ('created', 'modified', 'deleted_at', 'creator', 'modifier', 'status', 'state', 'date_emi', 'version')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["term"].widget.attrs["class"] = "form-control select2"
        self.fields["career"].widget.attrs["class"] = "form-control select2"


class SchedulerLineItemFormSet(BaseFormSet):

    def clean(self):
        """
        Adds validation to check that ....
        :return:
        """
        # TODO: Validations
        if any(self.errors):
            return

        for form in self.forms:
            if form.cleaned_data:
                print(form)


class LineForm(forms.ModelForm):
    """
    Form for individual use lineItemSchedule
    """
    # iterable
    WEEK_CHOICES = (
        ("lunes", "Lunes"),
        ("martes", "Martes"),
        ("miércoles", "Miércoles"),
        ("jueves", "Jueves"),
        ("viernes", "Viernes"),
        ("sabado", "Sábado"),
    )

    subject = forms.ModelChoiceField(
        required=False, label='Materia',
        queryset=SubjectModel.objects.filter(status=True)
    )
    teacher = forms.ModelChoiceField(
        required=False, label='Profesor',
        queryset=TeacherModel.objects.filter(status=True)
    )
    parallel = forms.ModelChoiceField(
        required=False, label='Paralelo',
        queryset=ParallelModel.objects.filter(status=True)
    )
    classroom = forms.ModelChoiceField(
        required=False, label='Aula',
        queryset=ClassRoomModel.objects.filter(status=True)
    )
    start_day = forms.ChoiceField(required=False, choices=WEEK_CHOICES, label="Día 1")

    class Meta:
        model = LineItemScheduleModel
        widgets = {
            "availability": forms.Select({"class": "availability form-control select2"}),
            "parallel": forms.Select({"class": "parallel form-control select2"}),
            "start_day": forms.Select({"class": "start_day form-control select2"}),
            'start_time': forms.TimeInput(format='%I:%M %p', attrs={"class": "time form-control timepicker"}),
            'end_time': forms.TimeInput(format='%I:%M %p', attrs={"class": "time form-control timepicker"}),
        }
        exclude = ('created', 'modified', 'deleted_at', 'creator', 'modifier', 'status', 'plan')
