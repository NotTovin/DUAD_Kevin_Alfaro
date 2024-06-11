from student import Student

def enter_student_information(student_list):
    
    scores = {}
    subjects = ['Spanish', 'English', 'History', 'Science']

    name = input('Enter the student name: ')
    class_room = input('Enter the student class room: ')

    for subject in subjects:
        running = True
        while running:
            try:
                score = float(input(f'Enter the score of {subject}: '))
                if 0 <= score <= 100:
                    scores[subject] = score
                    running = False
                else:
                    print('Enter a valid number between 0 an 100')
            except ValueError:
                print('Enter a valid number between 0 an 100')
    
    student = Student(name, class_room, scores)
    student_list.append(student)
    
    print('Student added')
    print(student_list)
    
def check_all_students_information(student_list):
    if student_list:
        print("\n *** List of all the students registered ***")
        for student in student_list:
            print(f"\nName: {student.name}")
            print(f"Class Room: {student.class_room}")
            for subject, score in student.scores.items():
                print(f"{subject} : {score}")
            print(f'Average Score: {student.average_score}')
    else:
        print("0 Students registered")

def top_3_average_scores(student_list):
    student_list_sorted = sorted(student_list, key=lambda student: student.average_score, reverse=True)
    top_3_students = student_list_sorted[:3]
    
    print(f'\nTOP 3 STUDENTS WITH THE BEST AVERAGE')
    for student in top_3_students:
        print(f'Name: {student.name}, from classroom {student.class_room} with an average score of {student.average_score}')
        
        

def get_students_average_scores(student_list):
    total_average = 0
    
    for student in student_list:
        total_average += student.average_score
    if student_list:
        general_average = total_average / len(student_list)
        print(f'Average score among all the students: {general_average}')
    else:
        print('No students registered')