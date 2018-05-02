students = []


class Student:

    def add_student(self, name, student_id=332):
        student = {"name": name, "student_id": student_id}
        students.append(student)


student = Student()
student.add_student("Mark")
print(students)
# This is comment
