list_a = [
        'first name',
        'last_name',
        'role',
        ]
list_b = [
        'Alek',
        'Castillo',
        'Software engineer'
        ]


def unir(dictionary):
        for index in range(0, len(list_a)):
                dictionary[list_a[index]] = list_b[index]


def main():
        dictionary = {}
        unir()
        dictionary = unir(list_a, list_b)
        print(dictionary)

if __name__ == "__main__":
        main()



