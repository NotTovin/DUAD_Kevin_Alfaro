def check_if_number(func):
    def wrapper(*args):
        
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f'{arg} is not a number')
        return func(*args)
    
    return wrapper

@check_if_number
def multiply(a, b):
    return a * b

print(multiply(6, 7))      
print(multiply(5, 't'))
