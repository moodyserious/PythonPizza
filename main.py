import model
import random
import time




def createObj(classname, id, flavor, size, quantity):
    obj = None

    numtopp = input("Enter the number of toppings, max:2 ")


    if numtopp == "0":
        obj = classname(id, flavor, size, quantity, toppings=None)

    elif numtopp == "1":
        topping = input("Enter the topping ")
        obj = classname(id, flavor, size, quantity, topping)

    elif numtopp == "2":
        Toppings = []
        counter = 2
        while(counter > 0):
            topping = input("Enter the topping ")
            Toppings.append(topping)
            counter-=1
            if counter == 0:
                obj = classname(id, flavor, size, quantity, Toppings)

    return obj


def buyerMode():

    obj = model.Pizza()
    print("1. Add new category to menu")
    print("2. Append a new menu in category")
    print("3. Delete a category")
    state = int(input("Enter the associated number: "))
    if state == 1:
        category = input("Enter the category: ")
        flavor = input("Enter the flavor: ")
        cost = int(input("Enter the cost: "))
        obj.addCategory(category, flavor=flavor, cost=cost)

    elif state == 2:
        category = input("Enter the category: ")
        flavor = input("Enter the flavor: ")
        cost = int(input("Enter the cost: "))
        obj.addtoMenu(category, flavor, cost)

    elif state == 3:
        category = input("Enter the category: ")
        obj.deletefromMenu(category)

    print(model.menu)

def printMenu():

    print("----------------Menu--------------")

    for y in model.menu.keys():   #-- get you key like Beef or Chicken
        print("Category: {}".format(y))
        print("-----------------------------")
        for j in model.menu.get(y):   #-- iterates over each object in array to get cost and flavor
            print("Flavor: {}     Cost: {}".format(j.get("flavor"), j.get("cost")))

    print("")


def takeOrder():

    flavor = input("Enter the flavor: ")
    size = input("Enter the size, e.g: S, M, L: ")
    quantity = int(input("Enter the quantity: "))
    id = random.randrange(176, 2000, 2)

    if "Beef" in flavor:
        obj = createObj(model.BeefPizza, id, flavor, size, quantity)
        while True:
            if obj == None:
                print("Invalid Input")
                obj = createObj(model.BeefPizza, id, flavor, size, quantity)
            else:
                break


    elif "Chicken" in flavor:
        obj = createObj(model.ChickenPizza, id, flavor, size, quantity)
        while True:
            if obj == None:
                print("Invalid Input")
                obj = createObj(model.ChickenPizza, id, flavor, size, quantity)
            else:
                break

    else:
        print("Invalid Input")


    obj.addtoCart()



    name = input("Enter your name: ")
    address = int(input("Enter the P.O.B number for delivery: "))
    custobj = model.Customers(id, name, address)
    custobj.addCustomers()


    print("----Your Order----")
    print(model.cart)
    print(model.customers)


    print("1. Cancel Order")
    print("2. Order More")
    state = int(input("Make your choice by entering the associated number: "))
    if state == 1:
        id = int(input("Enter the id: "))
        custobj.cancelOrder(id)
        print("Thank you for not shopping with us, note the sarcasm")


def Main():

    print("Select Mode: ")
    print("1. Buyer")
    print("2. Seller")
    while True:
        mode = int(input("Enter the associated number"))
        if mode == 1:
            printMenu()
            takeOrder()
            return

        elif mode == 2:
            buyerMode()
            return

        else:
            print("Invalid Input")



if __name__ == "__main__":
    Main()