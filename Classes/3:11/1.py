file1 = open("Classes/3:11/1.txt", 'w')
def register(students):
    student = input("Enter student name (type 'done' to finish): ")
    if student != 'done':
        file1.write("{'name': student, 'score': None ,'assignment' : None}")
        return True
    else:
        file1.close()
        return False

def list_students(students):
    for student in students:
        print(f"Student Name: {student['name']}, Assignment:{student['assignment']} ,Score: {student['score']}")

def add_scores_assignment(students):
    for student in students:
        assignment = input(f"Enter assignment :")
        score = input(f"Enter score for {student['name']}: ")
        student['score'] = int(score)
        student['assignment'] = str(assignment)

students = []
while True:
    entry = input("This is the grade system. Type 1 to register new stu3dents, Type 2 to enter new grades, Type 3 to list current students, type exit to leave submenu: ")
    if entry == '1':
        while register(students) :
            pass
    elif entry == '2':
        add_scores_assignment(students)
    elif entry == '3':
        list_students(students)
    elif entry == 'exit':
        break
    else:
        print("Invalid input. Please try again.")

file1.close()