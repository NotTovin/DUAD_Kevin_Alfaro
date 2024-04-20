def uppers_lowers(text):
    total_upper = 0
    total_lower = 0
    for letter in text:
        if letter != letter.lower():
            total_upper += 1
        else:
            total_lower += 1
    print(f'There are {total_upper} upper cases and {total_lower} lower cases')


def main():
    text = "I love Nación Sushi"
    uppers_lowers(text)

if __name__ == "__main__":
    main()