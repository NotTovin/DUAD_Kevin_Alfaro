def sum_numbers(numbers_list):
    total = 0
    for number in numbers_list:
        total += number
    return total


def main():
    numbers_list = [4, 6, 2, 29]
    total = sum_numbers(numbers_list)
    print(total)

if __name__ == "__main__":
    main()
