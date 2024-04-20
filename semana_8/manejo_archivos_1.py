def align_and_copy_songs(original_file, new_file):
    with open(original_file, 'r') as file:
        songs = file.readlines()
        print(songs)
        
    sorted_songs = sorted(songs)

    with open(new_file, 'w') as file:
        for song in sorted_songs:
            file.write(song)
            print(song)

align_and_copy_songs("songs.txt", "new_songs.txt")



