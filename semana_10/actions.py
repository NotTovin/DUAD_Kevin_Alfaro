def enter_student_information(student):
    
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
    
    student_list = {
        'Name' : name,
        'Class Room' : class_room,
        'Scores' : scores
    }
    
    student.append(student_list)
    print('Student added')
    print(student)
    
def check_all_students_information(students):
    
    if students:
        print("\n *** List of all the students registered ***")
        for student in students:
            print(f"\nName: {student['Name']}")
            print(f"Class Room: {student['Class Room']}")
            for subject, score in student['Scores'].items():
                print(f"{subject} : {score}")
    else:
        print("0 Students registered")

    
def get_average_score(student, students):
    scores = student["Scores"]
    total_score = sum(scores.values())
    total_subjects = len(scores)
    
    average_score = total_score / total_subjects
    return average_score
    
def top_3_average_scores():
    print()

def get_students_average_scores(students):
    average_scores = []
    for student in students:
        average_scores.append(get_average_score(student, students))
    
    total_average = sum(average_scores)
    general_average = total_average / len(students)
    print(f'Average score among all the students: {general_average:.2f}')

