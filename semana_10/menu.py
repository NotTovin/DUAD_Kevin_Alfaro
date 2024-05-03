from actions import get_students_average_scores, enter_student_information, check_all_students_information,top_3_average_scores
from data import export_students_to_csv, import_students_from_csv

def display_menu():
    print("\nMenu")
    print("1. Enter the student information")
    print("2. Check all the students registered")
    print("3. Top 3 students with the best scores")
    print("4. Average score among all the students")
    print("5. Export to CSV")
    print("6. Import from CSV")
    print("7. Exit")

def show_menu():
    running = True
    students = []
    try:
        while running:
            try:
                display_menu()
                option = int(input("Please choose your option: "))
            except ValueError as ex:
                print(f'Please enter a valid option')
            match option:
                case 1:
                    enter_student_information(students)
                case 2:
                    check_all_students_information(students) 
                case 3:
                    top_3_average_scores()
                case 4:
                    get_students_average_scores(students)
                case 5:
                    export_students_to_csv()
                case 6:
                    import_students_from_csv()
                case 7:
                    running =  False
                    exit()
                case _:
                    exit()
        print('Enter a valid number!')       
    except Exception as ex:
        print(f'An unexpected error ocurred: {ex}')
