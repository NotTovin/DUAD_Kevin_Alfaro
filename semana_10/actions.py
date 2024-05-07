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
                    total_score = sum(scores.values())
                    total_subjects = len(scores)
                    average_score = total_score / total_subjects
                    running = False
                else:
                    print('Enter a valid number between 0 an 100')
            except ValueError:
                print('Enter a valid number between 0 an 100')
    
    student_dict = {
        'Name' : name,
        'Class Room' : class_room,
        'Scores' : scores,
        'Average Score' : average_score
    }
    
    student_list.append(student_dict)
    print('Student added')
    print(student_list)
    
def check_all_students_information(student_list):
    
    if student_list:
        print("\n *** List of all the students registered ***")
        for student in student_list:
            print(f"\nName: {student['Name']}")
            print(f"Class Room: {student['Class Room']}")
            for subject, score in student['Scores'].items():
                print(f"{subject} : {score}")
            print(f'Average Score: {student['Average Score']}')
    else:
        print("0 Students registered")

def top_3_average_scores(student_list):
    student_list_sorted = sorted(student_list, key=lambda student:student['Average Score'], reverse=True)
    top_3_students = student_list_sorted[:3]
    
    print(f'\nTOP 3 STUDENTS WITH THE BEST AVERAGE')
    for student in top_3_students:
        name = student['Name']
        class_room = student['Class Room']
        average_score = student['Average Score']
        print(f'Name: {name}, from classroom {class_room} with an average score of {average_score}')
        
        

def get_students_average_scores(student_list):
    total_average = 0
    
    for student in student_list:
        average_score = student['Average Score']
        total_average += average_score
    if student_list:
        general_average = total_average / len(student_list)
        print(f'Average score among all the students: {general_average}')
    else:
        print('No students registered')