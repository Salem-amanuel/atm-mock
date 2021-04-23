class budget:
    #pass

#obj = budget()
#print(type(obj))

   #attributes
#amount
#category

    #amount = 0

    #def __init__(self):
        #   self.category = ["food", "clothing", "entertainment"]

    # or

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

#methods
    def deposit(self):
        return "This is a deposit method"

    def check_balance(self):
        pass

    def withdraw(self):
        pass

    def transfer(self):
        pass



# instance of objects
category = budget("clothing", 1000)
category_1 = budget("food", 1000)
category_2 = budget("entertainment", 1000)

# to use methods we instantiate the objects

print(category.deposit())
