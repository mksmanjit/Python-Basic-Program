students =[]

class Student:
    def __init__(self, name, student_id=331):
        student = {"name":name, "student_id":student_id}
        students.append(student)


    def __str__(self):
        return "Student"


mark = Student("Mark")
print(mark)