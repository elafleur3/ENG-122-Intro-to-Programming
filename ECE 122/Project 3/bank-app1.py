from Bank import BankAccount #imports BankAccount class to be used in this app

def app1(): #defines function of app1
    print("Welcome to App1") #prints intro to app1
    print("===============")
    print( )
    salary, checking, saving = input("Enter salary and initial balances for Checking and Saving accounts: ").split() #records multiple inputs by user and splits them into variables listed
    salary, checking, saving = float(salary), float(checking), float(saving) #floats inputs (which are strings) from user so they can be used in math equations
    checkingacc = BankAccount("Checking", checking) #initializes checking account of class BankAccount
    savingacc = BankAccount("Saving", saving) #initializes saving account of class BankAccount
    print(checkingacc) #displays current balance of checking account
    print(savingacc) #displays current balance of saving account
    print("Month--salary--expense--saving") #shows user the format for the display
    for i in range(12): #loop for 12 months
        if i==0: #if statement for firat month in loop
            print(i+1,"--",int(salary),"--",int(salary*.8),"--",int(salary*.15)) #prints numbers in correct format
            checkingacc.deposit(salary*.05) #deposits money into the checking account
            savingacc.deposit(salary*.15) #deposits amount into saving account
        else: #for rest of months in loop
            salary += salary*.002 #adds salary raise to the salary
            print(i+1,"--",int(salary),"--",int(salary*.8),"--",int(salary*.15))
            checkingacc.deposit(salary*.05)
            savingacc.deposit(salary*.15)
    print(checkingacc) #prints new balance of checking account
    print(savingacc) #prints new balance of saving account

app1()
    
    
