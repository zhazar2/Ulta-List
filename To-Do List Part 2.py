#To-Do List Part 2
#Zehra Hazar
#1/18/2024

#Initalize
UltaList = []

#Functions
def addItem ():
    newItem = input("What item would you like to add?")
    UltaList.append(newItem)

def viewList():
    print(UltaList)

def completedItem():
    boughtItem = input("What item did you buy?")
    index = UltaList.index(boughtItem)
    UltaList[index] = boughtItem + "[X]"

def removeItem():
    deleteItem = input("What item did you want to remove? If you bought it, add '[X]' right next to the item")
    UltaList.remove(deleteItem) 

def removeAllItems():
    UltaList.clear()

def sortList():
    UltaList.sort()

def numberItems():
    print ("Number of items in the list = ", len(UltaList))

def finalList():
    Track = True
    while Track:
        print("Welcome to your personal Ulta List!")
        print("Please choose an action you would like to do? (Type a number between 1-5)")
        print("1. Add an Item \n2. View your List \n3. Mark an Item As Bought \n4. Remove an Item \n5. Remove all Items \n6. Sort the Items Alphabetically \n7. Print # of Items in List \n8. Quit program ")
        option = int(input("Option:"))
        if (option == 1):
            addItem()
        elif (option == 2):
            viewList()
        elif (option == 3):
            completedItem()
        elif (option == 4):
            removeItem()
        elif (option == 5):
            removeAllItems()
        elif (option == 6):
            sortList()
        elif (option == 7):
            numberItems()
        elif (option == 8):
            Track = False
            print("Goodbye!")
            quit()

#Main
finalList()