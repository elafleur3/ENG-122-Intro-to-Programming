from MediaItem import MediaItem #Imports MediaItem class from MediaItem file.

def display_menu(): #Function Displys Main Menu.
    print("\nMenu");
    print("====");
    print("1-List Inventory");
    print("2-Info Inventory");
    print("3-List of All Books");
    print("4-List of All Movies");
    print("5-Item Description");
    print("6-Remove Item");
    print("7-Add Item");
    print("8-Set Maximum Price");
    print("0-Exit\n");

def initialize(): #Function Initializes the base item library, and then returns the items created so they can be used later.
    item0=MediaItem("Movie","2001: A Space Odyssey",float(11.99),"TU2RL012","Stanley Kubrick","Keir Dullea",None)
    item1=MediaItem("Book","A Brief History of Time",float(10.17),"GV5N32M9",None,None,"Stephen Hawking")
    item2=MediaItem("Movie","North by Northwest",float(8.99),"1DB6HK3L","Alfred Hitchcock","Cary Grant",None)
    item3=MediaItem("Movie","The Good, The Bad and The Ugly",float(9.99),"PO5T7Y89","Segio Leone","Clint Eastwood",None)
    item4=MediaItem("Book","The Alchemist",float(6.99),"TR3FL0EW",None,None,"Paulo Coelho")
    item5=MediaItem("Book","Thus Spoke Zarathustra",float(7.81),"F2O9PIE9",None,None,"Friedrich Nietzsche")
    item6=MediaItem("Book","Jonathan Livingston Seagull",float(6.97),"R399CED1",None,None,"Richard Bach")
    item7=MediaItem("Movie","Gone with the Wind",float(4.99),"2FG6B3N9","Victor Fleming","Vivien Leigh",None)
    item8=MediaItem("Book","Gone with the Wind",float(7.99),"6Y9OPL87",None,None,"Margarett Mitchell")
    return item0, item1, item2, item3, item4, item5, item6, item7, item8,
    
def display(items,mp): #Function displays all the items in the library, given that the max price set by the user is not below the price of the item. #Function used in option 1
    print("Reference/Media/Title/Price (max=$%s)"%(mp))
    print("---------------------------")
    for i in range(len(items)):
        if mp>=items[i].price:
            print("%s %s %s $%s"%(items[i].ref,items[i].media,items[i].title,items[i].price))
    print( )

def info(items): #4 variables are initialized then used later in the function #Function used in option 2
    tp=0 #Variable for total price of library
    MostExpensive=0 #Variable for most expensive item in library
    NumBooks=0 #Variable for total number of books
    NumMovies=0 #Variable for total number of books
    for i in range(len(items)): #Loop for finding total price and maximum price
        tp=float(tp+items[i].price)
        if items[i].price>MostExpensive:
            MostExpensive=float(items[i].price)
    for i in range(len(items)): #Loop for finding total number of books and movies
        if items[i].media=="Book":
            NumBooks=(NumBooks+1)
        elif items[i].media=="Movie":
            NumMovies=(NumMovies+1)
    print("Inventory is worth $%s"%tp)
    print("Most expensive item at $%s"%MostExpensive)
    print("There are %s Book(s), and %s Movie(s)"%(NumBooks,NumMovies))
    print( )

def display2(items,command,mp): #Function displays all books or movies dependent on command entered by user
    print("Reference/Media/Title/Price (max=$%s)"%(mp))
    print("---------------------------")
    if command==3:
        for i in range(len(items)): #Loop that prints all books 
            if items[i].media=="Book":
                if mp>=items[i].price:
                    print("%s %s %s $%s"%(items[i].ref,items[i].media,items[i].title,items[i].price))
    elif command==4:
        for i in range(len(items)): #Loop that prints all movies
            if items[i].media=="Movie":
                if mp>=items[i].price:
                    print("%s %s %s $%s"%(items[i].ref,items[i].media,items[i].title,items[i].price))
    print( )

def search_item(items,search): #Function used in option 5 #Function allows user to search for item and get its info given the reference number
    found=False #Boolean variable is initialized #Boolean variable is used to determine if item is found and therefor what needs to be displayed
    for i in range(len(items)): #Loop compares user inputted reference number with reference numbers in item library
        if search==items[i].ref:
            founditem=items[i]
            found=True
    if found==True:
        return founditem #Returns item that matches reference number
    else:
        founditem=None
        return founditem #Returns a value of none for item that should have been returned
def display_item(items,search): #Function displays item that was found in the previous function that searched for the matching item
    founditem=search_item(items,search) #Retrieves variable from search_item function
    if founditem!=None:
        print("Title: %s (Ref: %s, Price: $%s);"%(founditem.title,founditem.ref,founditem.price)) #If item is found, function displays info on that item
        if founditem.media=="Book": #If statement deternines whether the found item is a book or movie then displays the correct info
            print("Author: %s"%(founditem.author))
        else:
            print("Movie Director: %s; Lead Actor: %s"%(founditem.director,founditem.lead_actor))
    else: #If no matching item was found, then the function tells the user.
        print("No such item found!")

def search_index_item(items,del_item): #Function searches for item matching reference number and then deletes that item
    found=False
    for i in range(len(items)): #Searches for item
        if del_item==items[i].ref:
            del_index=i
            found=True
    if found==True: #If item found then it is deleted
        del items[del_index]
    else: #If item is not found then user is notified
        print("No such item found!")

def create_item(items): #Function adds item to list based on user inputted info
    NIMedia=input("Book or Movie? ")
    if NIMedia=="Book": #Starts questioning for books
        NITitle=input("Enter Book Title: ")
        NIRef=input("Enter Book Reference: ")
        NIPrice=input("Enter Book Price: ")
        NIAuthor=input("Enter Author Name: ")
        NewItem=MediaItem("Book",NITitle,float(NIPrice),NIRef,None,None,NIAuthor)
        items.append(NewItem)
    elif NIMedia=="Movie": #Starts questioning for movies
        NITitle=input("Enter Movie Title: ")
        NIRef=input("Enter Movie Reference: ")
        NIPrice=input("Enter Movie Price: ")
        NIDirector=input("Enter Director Name: ")
        NILA=input("Enter Lead Actor Name: ")
        NewItem=MediaItem("Movie",NITitle,float(NIPrice),NIRef,NIDirector,NILA,None)
        items.append(NewItem)
    else: #Book or Movie was not inputted by user
        print("Wrong input!")
        
        


        
        
    


    
        
    
        
            
        
    
        
    
        
    
    
    
    










        
                     



    

