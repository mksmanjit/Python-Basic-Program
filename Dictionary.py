student = {
    "name":"Mark",
    "rollNo":10,
    "class":None
}

print(student)
print(student["name"])
print(student.get("last_name","Unknown"))
print(student.keys())
print(student.values())
student["name"]="James"
print(student)
del student["name"]
print(student)
student["last_name"]="lee"
print(student)