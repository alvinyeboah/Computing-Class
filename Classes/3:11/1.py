def register(students):
    student = input("Enter student name (type 'done' to finish): ")
    if student != 'done':
        students.append({'name': student, 'score': None})
        return True
    else:
        return False

def list_students(students):
    for student in students:
        print(f"Student Name: {student['name']}, Score: {student['score']}")

def add_scores(students):
    for student in students:
        score = input(f"Enter score for {student['name']}: ")
        student['score'] = int(score)

students = []

while True:
    entry = input("This is the grade system. Type 1 to register new students, Type 2 to enter new grades, Type 3 to list current students, type exit to leave submenu: ")
    if entry == '1':
        while register(students):
            pass
    elif entry == '2':
        add_scores(students)
    elif entry == '3':
        list_students(students)
    elif entry == 'exit':
        break
    else:
        print("Invalid input. Please try again.")