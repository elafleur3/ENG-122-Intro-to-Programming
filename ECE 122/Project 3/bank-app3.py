from Bank import BankAccount #imports BankAccount class

def app3(): #defines app3
    print("Welcome to App3") #prints intro to app3
    print("===============")
    print( )
    mortgage, rate, monthly = input("Enter amount to borrow, rate, and monthly payment: ").split() #takes user inputs and assigns them to correct variables
    mortgage, rate, monthly = float(mortgage), float(rate), float(monthly) #changes inputs to numbers to be acted on
    mortgageacc = BankAccount("Mortgage", mortgage, rate)#initializes mortgage account of class BankAccount
    print(mortgageacc) #prints balance of mortgage acount
    running = True #initializes varibales tto be used in loops
    month = 1
    year = 0
    while running==True: #while loop 
        if mortgageacc.balance>0: #if the balance of mortgage account is greateer than 0
            if month==1:  #if statement for first month of loop
                mortgageacc.withdraw(monthly-(mortgageacc.rate/12)*mortgageacc.balance) #withdraws amount from motgage account
                initprincipal = mortgage-mortgageacc.balance #defines initial principal variable
                initinterest = monthly-initprincipal #defines initial interest variable
                mort = open("Amortization.txt", "w") #creates new file Amortizaion.txt for wrtiting
                mort.write("Month--Principal paid--Interest paid") #writes in new file the correct format for the rest of the writing process
                mort.write("\n") #skips line in new file
                mort.write(str(month)) #writes the month
                mort.write("--")
                mort.write(str(initprincipal)) #writes the principal paid
                mort.write("--")
                mort.write(str(initinterest)) #writes the interst paid
                mort.close() #closes file opened earlier
                month += 1 #adds 1 to month variable
            else: #for rest of months in loop
                mortgageacc.withdraw(monthly-(mortgageacc.rate/12)*mortgageacc.balance) #withdraws amount from mortgage account
                principal = (mortgage-mortgageacc.balance) #initializes new principle tobe paid
                interest = (month*monthly)-principal #initializes new interest to be paid
                mort = open("Amortization.txt", "a") #opens file again for appending
                mort.write("\n")
                mort.write(str(month)) #writes the month
                mort.write("--")
                mort.write(str(principal))#writes principal paid
                mort.write("--")
                mort.write(str(interest)) #writes interest paid
                mort.close() #closes file
                month += 1 #adds 1 to month
                if (month % 12 == 0): #checks if a year has passed by using remainder of month divided by 12
                    year += 1 #adds 1 to year
        else:
            month -= 1 #gets rid of extra month added in loop
            running = False #stops loop
    print("You will be paying your loan after ", month, " month! (or ", float(year), " years!)") #prints how long it will take to pay off loan
    total = month*monthly #gets total paid by user
    print("You borrowed $%s but paid $%s in total (with interests)"%(mortgage,total)) #prints totals

app3()
