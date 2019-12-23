class BankAccount: #defines class BankAccount

    def __init__(self, name = None, balance = None, rate = None): #creates instance for item of class BankAccount
        self.name = name
        self.balance = balance
        self.rate = rate

    def deposit(self, amount, record=False): #defines deposit method with arguments amount (amount to deposited) and record (whether the deposit should be displayed to user, initialized to no)
        if record: #If user wants it displayed
            self.balance += amount #balance of object becomes the original balance plus amount to be deposited
            print(self.name, "deposit requested", amount) #prints amount requested
            print("\tNew", self) #prints new balance
        else:
            self.balance+=amount #does not display deposit

    def withdraw(self, amount, record=False): #defines withdraw method with arguments amount (amount to be withdrawn) and record (whether the withdrawal should be displayed to user, initialized to no)
        if amount <= self.balance: #if amount to be withdrawn is less than the balance
            if record: #whether or not to be displayed
                self.balance -= amount #balance becomes the balance minus what is withdrawn
                print(self.name, "withdrawal requested", amount) #displays withdrawal requested
                print("\tNew", self) #prints new balance
            else:
                self.balance -= amount #does not display withdrawal
        else:
            if self.name=="Mortgage": #used for correct output for app3
                prev_balance = self.balance
                self.balance = 0 
            else: #does not let user withdraw more than what is in the account
                prev_balance = self.balance 
                self.balance = 0
                print(self.name, "withdrawal requested", amount)
                print("\tSorry your withdrawal is limited to", prev_balance)


    def __str__(self): #used for correct printing of the data object of the class BankAccount
        if self.rate==None:
            return "%s balance %s" % (self.name, self.balance)
        else:
            if self.name=="Mortgage":
                return "%s balance %s" % (self.name, self.balance)
            else:
                return "%s balance %s; rate %s" % (self.name, self.balance, self.rate)

    def addcompound(self): #defines addcompound method used in app2
        newbalance = self.balance*(1+self.rate/12)**12
        return newbalance

def main(): #main function for Task1 that shows how deposit and withdrawal methods work
    acc1 = BankAccount("Checking", 1000)
    print(acc1)
    acc1.deposit(250)
    acc1.deposit(250, True)
    acc1.withdraw(700, True)
    acc1.withdraw(850, True)
    print(acc1)

#main function is not called because if it is it displays in front of every app






    
