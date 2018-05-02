from student import Student


class HighSchool(Student):

    student_name = "SpringField HighSchool"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HF"
