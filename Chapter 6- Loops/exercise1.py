print ("\tWlecome to Pizza Hot!")  
print ("Once done, enter 'quit'")
while True:
    pizza = str(input("What would you like on your pizza? "))
    if pizza != 'quit':
        print("\tYou have added " + pizza + " to your toppings")
    else:
        break
