def app4(): #defines app4
    print("Welcome to App4") #prints intro to app4
    print("===============")
    print( )
    print("Ok I load your expenses from expense.txt") #tells user program has read expenses
    print("I have created the budget file budget.txt") #tells user the expenses have been organized in new file
    exp = open("expenses.txt", "r") #opens file expenses.txt to be read
    expenses,prices=[],[] #initializes expenses and prices lsits 
    rent, utility, phone, grocery, gas, restaurant, gym, theater, online, shopping = [],[],[],[],[],[],[],[],[],[] #initializes lists for all types of expenses
    for line in exp:# loop that reads all lines in expenses.txt file
        expense,price=line.split() #splits prices and expense type 
        expenses.append(expense) #puts expenses and prices into corresponding list
        prices.append(float(price))
    exp.close() #closes file
    for i in range(len(expenses)): #for loop that searches through the list of expense types and adds their prices to their own list
        if expenses[i]=="rent":
            rent.append(prices[i])
        elif expenses[i]=="utility":
            utility.append(prices[i])
        elif expenses[i]=="phone":
            phone.append(prices[i])
        elif expenses[i]=="grocery":
            grocery.append(prices[i])
        elif expenses[i]=="gas":
            gas.append(prices[i])
        elif expenses[i]=="restaurant":
            restaurant.append(prices[i])
        elif expenses[i]=="gym":
            gym.append(prices[i])
        elif expenses[i]=="theater":
            theater.append(prices[i])
        elif expenses[i]=="on-line":
            online.append(prices[i])
        elif expenses[i]=="shopping":
            shopping.append(prices[i])
    rent_total = str(sum(rent)) #chunk of code that sums all the prices in respective lists of prices then makes them strings so they can be written in new file
    utility_total = str(sum(utility))
    phone_total = str(sum(phone))
    grocery_total = str(sum(grocery))
    gas_total = str(sum(gas))
    restaurant_total = str(sum(restaurant))
    gym_total = str(sum(gym))
    theater_total = str(sum(theater))
    online_total = str(sum(online))
    shopping_total = str(sum(shopping))
    budget = open("budget.txt","w") #creates new file budget.txt to be written in
    budget.write("rent--") #chunk of code writes all the total prices for the specific expense type
    budget.write(rent_total)
    budget.write("\n")
    budget.write("utility--")
    budget.write(utility_total)
    budget.write("\n")
    budget.write("phone--")
    budget.write(phone_total)
    budget.write("\n")
    budget.write("grocery--")
    budget.write(grocery_total)
    budget.write("\n")
    budget.write("gas--")
    budget.write(gas_total)
    budget.write("\n")
    budget.write("restaurant--")
    budget.write(restaurant_total)
    budget.write("\n")
    budget.write("gym--")
    budget.write(gym_total)
    budget.write("\n")
    budget.write("theater--")
    budget.write(theater_total)
    budget.write("\n")
    budget.write("on-line--")
    budget.write(online_total)
    budget.write("\n")
    budget.write("shopping--")
    budget.write(shopping_total)
    budget.write("\n")
    expense_total = str(float(rent_total)+float(utility_total)+float(phone_total)+float(grocery_total)+float(gas_total)+float(restaurant_total)+float(gym_total)+float(theater_total)+float(online_total)+float(shopping_total)) #gets the total price of all expenses by making them floats then adding them
    budget.write("Total--") #prints total of expenses
    budget.write(expense_total)
    budget.close() #closes the file
            
app4()
    
