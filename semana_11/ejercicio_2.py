class Bus():
    
    
    def __init__(self, max_passenger):
        self.max_passenger = max_passenger
        self.passengers = []
    
    def add_passenger(self, person):
        if len(self.passengers) < self.max_passenger:
            self.passengers.append(person)
            print(f'{person.name} has boarded the bus')
        else:
            print('The bus is already full')
    
    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f'{person.name} has gotten off the bus ')
        else:
            print(f'{person.name} is not in the bus')
    
class Person():
    
    def __init__(self, name):
        self.name = name
        


def show_menu():
    print('Menu')
    print('1. Add passenger')
    print('2. Remove passenger')
    print('3. Exit')

def main():
    max_passengers = int(input('Enter the total passengers in the bus: '))
    bus = Bus(max_passengers)
    option = True
    
    while option:
        show_menu()
        choice = int(input('Choose your option: '))
        
        match choice:
            case 1:
                name = input('Enter the name of the passenger: ')
                person = Person(name)
                bus.add_passenger(person)
            case 2:
                name =  input('Enter the name of the passenger: ')
                person = Person(name)
                bus.remove_passenger(person)
            case 3:
                option = False
                print('Closing the app')
                exit()
        
    print('Enter a valid option')

if __name__ == "__main__":
    main() 
    