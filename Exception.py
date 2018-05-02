student = {
    "name":"Mark",
    "student_id":15163,
    "feedback":None
}

try:
    lastName = student["last_name"]
except KeyError:
    print("Key not found")

try:
    con = 3 + "x"
except TypeError as error:
    print("Cannot add int to string")
    print(error)
except Exception:
    print("Unknown error")
print("Program executed...")
