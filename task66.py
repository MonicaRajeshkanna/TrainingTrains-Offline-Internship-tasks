attendance = {
    "Monica":"Present",
    "Rahul":"Absent",
    "Priya":"Present"
}

name = input("Enter Student Name: ")

print(attendance.get(name,"Student Not Found"))