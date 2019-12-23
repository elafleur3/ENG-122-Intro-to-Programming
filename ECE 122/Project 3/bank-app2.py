from Bank import BankAccount #imports BankAccount class

def app2():
    print("Welcome to App2") #prints intro to app2
    print("===============")
    print( )
    saving, rate = input("Enter initial balance and interest rate for saving account: ").split() #assigns multiple inputs from user inputs to corresponding variables
    saving, rate = float(saving), float(rate) #floats inputs from user
    savingacc = BankAccount("Saving", saving, rate) #initializes object of class BankAccount called saving account
    print(savingacc) #prints balance of saving account
    print( )
    print("How many years will it take to triple my balance?")
    stop = savingacc.balance*3 #variable for telling loop when to stop
    year = 0 #variable for number of years until a certain goal is reached
    running = True #variable for while loop
    while running==True: #loop until variable running is set to false
        if savingacc.balance<stop: #if the balance is less than tripled
            newbalance = savingacc.addcompound() #addcompound function is called to add balance of account
            savingacc.deposit(newbalance-savingacc.balance) #amount is deposited into saving account
            year += 1 #year is raised by 1
        else:
            running = False #stops while loop
    print("You will triple your initial balance after ", year, "Years!") 
    print(savingacc)
    print( )
    print("Would this be better if I keep contributing 5% of my initial amount every year?")
    savingacc = BankAccount("Saving", saving, rate) #re-initializes saving account data object
    running = True
    year = 0
    fivepercent = savingacc.balance*.05 #variable for five perecent of balance
    while running==True:
        if savingacc.balance<stop:
            newbalance = savingacc.addcompound()
            savingacc.deposit(newbalance-savingacc.balance)
            savingacc.deposit(fivepercent) #also deposits five percent of initial balance
            year += 1
        else:
            running = False
    print("You will triple your initial balance after ", year, "Years!")
    print(savingacc)
    print( )
    print("Would this be even better if in addition my interest rate grows up by 0.5% every year?")
    savingacc = BankAccount("Saving", saving, rate) #once again re-initializes the variables
    running = True
    year = 0
    while running==True:
        if savingacc.balance<stop:
            if year!=0: #if statement for first year of loop
                savingacc.rate += savingacc.rate*.005
            newbalance = savingacc.addcompound()
            savingacc.deposit(newbalance-savingacc.balance)
            savingacc.deposit(fivepercent)
            year += 1
        else:
            running = False
    print("You will triple your initial balance after ", year, "Years!")
    print(savingacc)

app2()
