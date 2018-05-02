student_names =["James","Katarina","Jessica","Mark","Bort","Frank Grimes"]

for name in student_names:
    if(name=="Mark"):
        print("Found him! " + name)
        break
    print("Currently Testing..." + name)

for name in student_names:
    if(name=="Mark"):
        continue
    print("Currently Testing..." + name)
