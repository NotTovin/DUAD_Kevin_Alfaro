class BankAccount():
    balance = 0.0
    
    def add_money(self, amount):
        if amount > 0:
            self.balance +=  amount
            print(f"You have added ${amount} to the account")
            print(f"New total amount is ${amount}")
        else:
            print('You must add money to the account')
    
    def subtract_money(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"You have substracted ${amount} to the account")
                print(f"New total amount is ${self.balance}")
            else:
                print('Insufficient funds')
        else:
            print('You must subtract a possitive amount')
    

class SavingsAccount(BankAccount):
    min_balance = 0
    
    def subtract_money(self, amount):
        if amount > 0:
            if self.balance - amount >= self.min_balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Withdrawal would bring balance below minimum balance.")
        else:
            print("Withdrawal amount must be positive.")


my_savings = SavingsAccount()
my_savings.add_money(100)
my_savings.subtract_money(80)
