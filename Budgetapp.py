class Category:
    
    #constructor
    def __init__(self, category, amount): 
        self.category = category
        self.amount = amount
    
    #methods
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} in {} category".format(amount, self.category)

    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)

    def check_balance(self):
        return "Your current balance is {}".format(self.amount)
        
    def withdraw(self, amount):
        self.amount -= amount
        return "You have successfully withdrawn {} in {} category".format(amount, self.category)
        
    def transfer(self, amount, catergory):
        return self.withdraw(amount) + ' ' + Category.deposit(amount)
        


food_category = category("Food", 2000)
clothing_category = category("Clothing", 2000)
car_category = category("Car Expenses", 2000)
other_bills_category = category("Other bills", 2000)
selfcare_category = category("Selfcare", 2000)

print(car_category.deposit(250))
print(car_category.budget_balance())
print(car_category.check_balance())
print(Car_category.withdraw(500))
print(car_category.transfer(500, other_bills_category))



