import csv

def export_students_to_csv(student_list, file_list='students.csv'):
    if student_list:
        with open(file_list, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Class Room', 'Scores', 'Average Score'])
            for student in student_list:
                name = student['Name']
                class_room = student['Class Room']
                scores = student['Scores']
                average_score = student['Average Score']
                writer.writerow([name, class_room, scores, average_score])
            print('Data exported')
    else:
        print('There are no students registered to export')
    
def import_students_from_csv(file_list='students.csv'):
    students = []
    
    with open(file_list, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name = row[0]
            class_room = row[1]
            scores = row[2]
            average_score = [3]
            
            student_list = {
                'Name' : name,
                'Class Room' : class_room,
                'Scores' : scores,
                'Average Score' : average_score
            }
            students.append(student_list)
            
        print(f'Data imported from {file_list}')
        
    return students