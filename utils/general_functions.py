""""""
from django.db.models import Sum, Count

from main.enum import FileFormat


def generate_file_(instance=None, data=None, format=''):
    """
    Function that generate all formats.
    :param instance:
    :param data:
    :param format:
    :return:
    """
    content = ""
    content += "Composite Table\n"
    if format == FileFormat.TEACHERS.value:  # Profes
        heading = "p\ti\t\tAfinP\tHabP\n"
        content += heading
        info = list(data.values('teacher__alias', 'subject__code', 'teacher__affinity',
                                'teacher__skill'))
        for item in info:
            codep = item.get("teacher__alias")
            codes = item.get("subject__code")
            afinityp = item.get("teacher__affinity")
            skillp = item.get("teacher__skill")
            label = f"{codep}\t{codes}\t\t{afinityp}\t{skillp}\n"
            content += label

    elif format == FileFormat.QUANTITY_SUBJECT_TEACHERS.value:  # CantMatProfes
        heading = "p\t\tCantMatProf\t\tTipoProf\n"
        content += heading
        info = list(data.values('teacher__alias', 'teacher__contract__code'))
        result = []
        for item in info:
            codep = item.get("teacher__alias")
            if codep not in result:
                result.append(codep)
                qsubjects = instance.lineitemschedulemodel_set.filter(teacher__alias__exact=codep) \
                    .annotate(subjects_count=Count('subject')).count()
                tipoprof = item.get("teacher__contract__code")  # Calling to api
                label = f"{codep}\t\t{qsubjects}\t\t\t{tipoprof}\n"
                content += label

    elif format == FileFormat.AFIN_CLASSROOM.value:  # AfinAulas
        heading = "i\t\t\ta\t\tCostAula\n"
        content += heading
        info = list(
            data.values('subject__code', 'classroom__code', 'classroom__affinity')
        )
        for item in info:
            codes = item.get("subject__code")
            codec = item.get("classroom__code")
            caffinity = item.get("classroom__affinity")
            if len(codes) >= 8:
                label = f"{codes}\t\t{codec}\t\t{caffinity}\n"
            else:
                label = f"{codes}\t\t\t{codec}\t\t{caffinity}\n"
            content += label

    elif format == FileFormat.SUBJECT_CAREER.value:  # MatCar
        heading = "i\t\tc\tMatCar\n"
        content += heading
        info = list(
            data.values('subject__code', 'plan__career__alias', 'classroom__affinity')
        )
        for item in info:
            codes = item.get("subject__code", "")
            active = "1"
            codec = item.get("plan__career__alias", "")
            if len(codes) >= 8:
                label = f"{codes}\t{codec}\t{active}\n"
            else:
                label = f"{codes}\t\t{codec}\t{active}\n"
            content += label

    elif format == FileFormat.PARALLEL_CLASSROOM.value:  # ParAulas
        heading = "a\t\tCapAula\n"
        content += heading
        info = list(
            data.values('classroom__code', 'classroom__capacity')
        )
        for item in info:
            codep = item.get("classroom__code")
            cq = item.get("classroom__capacity")
            label = f"{codep}\t\t{cq}\n"
            content += label

    elif format == FileFormat.WORKING_DAY.value:  # Jornada
        heading = "i\t\th\t\tJornada\n"
        content += heading
        # TODO: Save hour pm/am
        info = list(
            data.values(
                'subject__code',
                'start_time', 'end_time',
                'status'
            )
        )
        for item in info:
            active = "1" if item.get("status") else "0"
            codes = item.get("subject__code")
            s = str(item.get("start_time")).replace(" ", "")
            e = str(item.get("end_time")).replace(" ", "")
            houry = str(f"{s}-{e}").strip()
            label = f"{codes}\t\t{houry}\t{active}\n"
            content += label

    elif format == FileFormat.SUBJECT_LEVEL.value:
        heading = "i\t\tn\t\tMatNiv\n"
        content += heading
        info = list(
            data.values('subject__code', 'subject__subjectmeshmodel__level')
        )
        for item in info:
            codes = item.get("subject__code")
            level = "S" + str(item.get("subject__subjectmeshmodel__level", 0))
            matniv = "1"  # Calling to api
            if len(codes) >= 8:
                label = f"{codes}\t{level}\t\t{matniv}\n"
            else:
                label = f"{codes}\t\t{level}\t\t{matniv}\n"
            content += label

    elif format == FileFormat.AVAILABILITY_TEACHERS.value:  # DispProfes
        heading = "p\th\t\td\tDispHorProf\n"
        content += heading
        info = list(
            data.values('teacher__alias', 'availability__start_time', 'availability__end_time',
                        'availability__num_start_day')
        )
        days = {
            "1": "Lunes", "2": "Martes", "3": "Miércoles",
            "4": "Jueves", "5": "Viernes", "6": "Sábado",
            "7": "Domingo"
        }
        for item in info:
            codet = item.get("teacher__alias")
            s = str(item.get("start_time"))
            e = str(item.get("end_time"))
            houry = f"{s}-{e}"
            d = str(days.get(item.get("num_start_day"))).lower()
            dispohorprof = "1"  # Calling to api
            label = f"{codet}\t{houry}\t{d}\t{dispohorprof}\n"
            content += label

    elif format == FileFormat.QUANTITY_PARALLEL.value and instance:  # CantParalelos
        heading = "i\t\tParMat\n"
        content += heading
        info = list(data.values('subject__code'))
        result = []
        for item in info:
            codes = item.get("subject__code")
            if codes not in result:
                qparallel = instance.lineitemschedulemodel_set.filter(subject__code__exact=codes) \
                    .annotate(num_parallel=Sum('parallel'))
                qpar = str(qparallel[0].num_parallel)
                label = f"{codes}\t\t{qpar}\n"
                content += label
                result.append(codes)
    return content
