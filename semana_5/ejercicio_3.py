# my_string = "The sun's golden rays danced across the tranquil surface of the lake"

# for char in reversed(my_string):
#     print(char)
smallest = None
print("Before:", smallest)
for itervar in [11, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)