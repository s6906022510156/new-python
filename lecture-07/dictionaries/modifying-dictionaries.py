student = {"name":"alice","age":25, "grade":"a"}

student["age"] = 26
student["major"] =  "compiter science"
print(student)

del student["grade"]
print(student)

removed_major = student.pop("major")
print(removed_major)
print(student)