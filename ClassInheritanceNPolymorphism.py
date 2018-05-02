students =[]


class Student:

    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student" + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


class HighSchool(Student):

    school_name = "SpringField HighSchool"

    def get_school_name(self):
        return self.school_name

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"


mark = HighSchool("Mark")
print(mark.get_school_name())
print(mark.get_name_capitalize())