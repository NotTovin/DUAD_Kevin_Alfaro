import csv
from student import Student


def export_students_to_csv(student_list, file_list='students.csv'):
    if student_list:
        with open(file_list, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Class Room', 'Spanish', 'English', 'History', 'Science', 'Average Score'])
            for student in student_list:
                data = student.obj_to_dict()
                writer.writerow([
                    data['Name'], 
                    data['Class Room'], 
                    data['Scores']['Spanish'], 
                    data['Scores']['English'], 
                    data['Scores']['History'], 
                    data['Scores']['Science'], 
                    data['Average Score']
                ])
            print('Data exported')
    else:
        print('There are no students registered to export')
    
def import_students_from_csv(file_list='students.csv'):
    students = []
    try:
        with open(file_list, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                scores = {
                    'Spanish': float(row['Spanish']),
                    'English': float(row['English']),
                    'History': float(row['History']),
                    'Science': float(row['Science'])
                }
                student = Student(
                    name = row['Name'],
                    class_room = row['Class Room'],
                    scores = scores
                )
                students.append(student)
                
            print(f'Data imported from {file_list}')
    except FileNotFoundError:
        print(f'File not found {file_list}')
        
    return students
