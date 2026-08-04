students = [
    {"name":"Sudin Shrestha", "marks":78},
    {"name": "Simrika Khanal", "marks": 88},
    {"name": "Sangat Tripathee", "marks": 66}
]


def add_student():
    name = str(input("Enter students name: "))
    marks = int(input("Enter student's marks: "))
    student = {
        "name": name,
        "marks": marks
    }
    print(f"Added Student's name as {name} and marks as {marks} successfully")

def view_student():
    for student in students:
        print(student["name"])
        print(student["marks"])
        print("-------------")

def search_student():
    std = str(input("Enter your student name: "))
    found = False

    for student in students:
        if std == student["name"]:
            print(f"found student {student['name']} \n marks: {student['marks']}")
            found = True
            break
        else :
            found = False
    if not found:
        print("Student not found")

def update_marks():
    std = str(input("Enter your student name: "))
    found = False
    
    for student in students:
        if std == student["name"]:
                print(f"found student {student['name']} \n marks: {student['marks']}")
                found = True
                new_marks = int(input("Enter a new marks to update: "))
                student['marks'] = new_marks
                print(f"Updated marks of {student['name']} is {student['marks']}")
                break
        else :
                found = False
    if not found:
            print("Student not found")
    

def delete_student():
    std = str(input("Enter the name of the student you wanna delete: "))
    found = False

    for student in students:
        if std == student['name']:
            print(f"Std name: {student['name']} \n marks: {student['marks']}")
            students.remove(student)
            print("Student deleted")
            found = True
            break
        else:
            found = False
    if not found:
        print("Student not found")

def show_topper():
    topper = students[0]
    for student in students:
        if student['marks'] > topper['marks']:
            topper = student

    print(f"topper is {topper['name']} with {topper['marks']}")

def average_marks():
    total = 0
    count = 0
    for student in students:
        total += student['marks'] 
        count += 1

    avg = total/count
    print(f'averge of all is {avg}')

    

while True:
    choice =int(input("Enter your choice: \n 1. Add Student\n 2. View All Students\n 3. Search Student\n 4. Update Marks\n 5. Delete Student\n 6. Show Toppper \n 7. Show Average Class Marks\n 8.Exit \n (choose from 1-8): \t "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_marks()
    elif choice == 5:
        delete_student()

    elif choice == 6:
        show_topper()
    elif choice == 7:
        average_marks()

    elif choice == 8:
        break