customers = {}
menu = {
    "Beef": [
        {"flavor": "Beef Spicy", "cost": 20},
        {"flavor" : "Beef Tikka", "cost": 30},
        {"flavor": "Beef Tandoori", "cost": 20}
    ],
    "Chicken": [
        {"flavor": "Chicken Spicy", "cost": 15},
        {"flavor": "Chicken Tandoori", "cost": 20}
    ]
}
cart = {}



class Customers:

    def __init__(self, id, name, pob):
        self.id = id
        self.name = name
        self.pob = pob


    def addCustomers(self):
        customers[self.id] = {"name": self.name, "P.O.B": self.pob}


    def cancelOrder(self, id):
        if id in customers:
            del customers[id]
        else:
            print("Incorrect id")



class Pizza:
    def __init__(self, size='S', toppings='[]'):
        self.size = size
        self.toppings = toppings

    def addCategory(self, category, **kwargs):   # add new category to menu like Vegetable
        for i in kwargs:
            menu[category] = kwargs

    def addtoMenu(self, category, flavor, cost):
        if category in menu:
            menu[category].append({"flavor": flavor, "cost": cost})

        else:
            print("Invalid Category")

    def deletefromMenu(self, category):
        if category in menu:
            del menu[category]

        else:
            print("Invalid Category")



class BeefPizza(Pizza):
    def __init__(self, id=0, flavor="Beef", size="S", quantity=0, toppings='[]'):
        Pizza.__init__(self, size, toppings)
        self.flavor = flavor
        self.id = id
        self.quantity = quantity

    def addtoCart(self):
        cart[self.id] = [{"flavor" : self.flavor, "size" : self.size,  "toppings" : self.toppings, "quantity": self.quantity, "price": self.calculateCost()}]

    def calculateCost(self):
        for i in menu.keys():
            for j in menu.get(i):
                if j.get("flavor") == self.flavor:
                    return j.get("cost") * self.quantity



class ChickenPizza(Pizza):
    def __init__(self, id=0, flavor="Chicken", size="S", quantity=0, toppings='[]'):
        Pizza.__init__(self, size, toppings)
        self.flavor = flavor
        self.id = id
        self.quantity = quantity

    def addtoCart(self):
        cart[self.id] = [{"flavor" : self.flavor, "size" : self.size,  "toppings" : self.toppings, "quantity": self.quantity, "price": self.calculateCost()}]

    def calculateCost(self):
        for i in menu.keys():
            for j in menu.get(i):
                if j.get("flavor") == self.flavor:
                    return j.get("cost") * self.quantity




