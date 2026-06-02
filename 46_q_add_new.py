student={"name": "Abhay", "age": 20, "grade": "B"}

student["sec"]="A"  #new key value pair added
print(student)

student["name"]="Sachin" #key is modified
print(student)
print(student["name"])
print(student.get("grade","not found"))












"""student ={"name": "Abhay","age":20, "grade":"B" }

#1. add a new key-value pair
student["city"]="Rnachi"

#2. modify an existing value
student["grade"] = "A"

#3. Access a specific key
student_name =student["name"]

print("Upload Student Dictionary: ", student)
print("Accessed Name:", student_name)
"""