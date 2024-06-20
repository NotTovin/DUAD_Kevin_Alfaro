from datetime import datetime
class User():
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
    
    @property
    def age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth
        return age
    

def legal_age(func):
    def wrapper(user, *arg):
        if user.age < 18:
            raise Exception('User is not +18 year old')
        return func(user, *arg)
    return wrapper

@legal_age
def access(user):
    return 'Access granted'
    

user = User(1990)
print(access(user))


