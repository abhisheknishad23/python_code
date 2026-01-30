class bank:
    def __init__(self, account_num, balance):
        self.account_num = account_num
        self.__balance = balance #private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f'Deposite {amount}. New balance {self.__balance}')

    def get_balance(self):
        return self.__balance #controlled access
    
account = bank('123',1000)

account.deposit(2000)
print(account.get_balance())

#print(account.__balance)