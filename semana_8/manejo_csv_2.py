import csv

def add_game():
    name = input('Name: ')
    genre = input('Genre: ')
    developer = input('Developer: ')
    classification = input('ESRB classification: ')
    return name, genre, developer, classification

def write_csv_file(file_path, data):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerow(['name','genre', 'developer', 'classification'])
        writer.writerows(data)
    

def main():
    video_games = []
    games = int(input('Enter the games to add: '))

    for game in range(games):
        video_games.append(add_game())
    
    write_csv_file('video_games.csv', video_games)
    
if __name__ == "__main__":
    main()