import csv

def export_students_to_csv(student_list, file_list='students.csv'):
    if student_list:
        with open(file_list, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Class Room', 'Spanish', 'English', 'History', 'Science', 'Average Score'])
            for student in student_list:
                name = student['Name']
                class_room = student['Class Room']
                scores = student['Scores']
                average_score = student['Average Score']
                writer.writerow([name, class_room, scores['Spanish'], scores['English'], scores['History'], scores['Science'], average_score])
            print('Data exported')
    else:
        print('There are no students registered to export')
    
def import_students_from_csv(file_list='students.csv'):
    students = []
    try:
        with open(file_list, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                name = row[0]
                class_room = row[1]
                scores = {
                    'Spanish' : row[2],
                    'English' : row[3],
                    'History' : row[4],
                    'Science' : row[5],
                }
                average_score = row[6]
                
                student_list = {
                    'Name' : name,
                    'Class Room' : class_room,
                    'Scores' : scores,
                    'Average Score' : average_score
                }
                students.append(student_list)
                
            print(f'Data imported from {file_list}')
    except FileNotFoundError:
        print(f'File not found {file}')
        
    return students