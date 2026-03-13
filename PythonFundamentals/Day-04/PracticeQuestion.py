class Account:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount 
        print(f"Added {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if self.__balance < amount:
            print("Insufficient balance available")
        else:
            self.__balance -= amount
            print(f"Remaining balance is: {self.__balance}")
    
    def getBalance(self):
        return self.__balance

p1 = Account("Sonu", 100)
p1.deposit(60)
p1.withdraw(50)
print("Available blance is ",p1.getBalance())

p2=Account("Lalit",50)
p2.withdraw(20)
p2.deposit(100)

class SavingsAccount(Account):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)  
        self.rate = rate     

    def add_interest(self):
       interest=self.getBalance()*(self.rate/100)
       self.deposit(interest)


sap1=SavingsAccount("Saver",0,5)
sap1.deposit(800)
print(sap1.getBalance())
sap1.add_interest()