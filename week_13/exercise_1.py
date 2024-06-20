def print_parameters(func):
    def wrapper(*args):
        
        print(f'SUM of {args}')
        result = func(*args)
        print(f'Result: {result}')
        
        return result
    return wrapper


@print_parameters
def add(a, b):
    return a + b

add(5, 7)

