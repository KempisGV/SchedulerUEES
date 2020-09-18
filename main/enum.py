from enum import Enum


class FileFormat(Enum):
    """Class that represent"""
    TEACHERS = "Profes"
    PARALLEL_CLASSROOM = "ParAulas"
    SUBJECT_LEVEL = "MatNiv"
    SUBJECT_CAREER = "MatCar"
    WORKING_DAY = "Jornada"
    AVAILABILITY_TEACHERS = "DispProfes"
    QUANTITY_PARALLEL = "CantParalelos"
    QUANTITY_SUBJECT_TEACHERS = "CantMatProfes"
    AFIN_CLASSROOM = "AfinAulas"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
