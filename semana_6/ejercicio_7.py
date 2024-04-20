def find_prime(number):
    if number <= 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def prime_numbers(new_list):
    primes = []
    for num in new_list:
        if find_prime(num):
            primes.append(num)
            print(f'{num} is prime')
    return primes

def main():
    list_number = [1, 4, 6, 7, 13, 9, 67]
    found_prime = prime_numbers(list_number)
    print(found_prime)  

if __name__ == "__main__":
    main()