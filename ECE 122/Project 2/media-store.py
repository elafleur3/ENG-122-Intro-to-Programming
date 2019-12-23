import inventory #Imports all functions from Inventory file

def MediaStore():
    mp=float(100) #Variable for max price that can be changed by user in menu
    menu=True #Variable used in while loop and determines when the loop ends
    print("Welcome to BestMedia") #Welcome message
    print("====================")
    print( )
    item0, item1, item2, item3, item4, item5, item6, item7, item8=inventory.initialize() #Gets original item inventory
    items=[item0, item1, item2, item3, item4, item5, item6, item7, item8] #Puts inventory into list form
    while menu==True:
        inventory.display_menu() #Displays starting menu
        command=int(input("Enter Command: "))
        if command==0: #Option 0 closes menu
            print("Goodbye!")
            menu=False
        elif command==1: #Option 1 displays list of items under maximum price
            print( )
            inventory.display(items,mp)
        elif command==2: #Option 2 displays some information about the inventory
            print( )
            inventory.info(items)
        elif command==3 or command==4: #Displays all books or all movies
            print( )
            inventory.display2(items,command,mp)
        elif command==5: #Allows user to search for item based on reference number
            search=str(input("Enter item reference: "))
            inventory.search_item(items,search)
            inventory.display_item(items,search)
        elif command==6: #Allows user to delete item in inventory based on reference number
            del_item=str(input("Enter item reference: "))
            inventory.search_index_item(items,del_item)
        elif command==7: #Allows user to add items to inventory
            inventory.create_item(items)
        elif command==8: #Allows user to set maximum price of items to be displayed
            mp=float(input("Enter maximum price (current=$%s): "%mp))
        else:
            print("Wrong Input!")

MediaStore()


