#Product
'''
Assignment: Product
The owner of a store wants a program to track products. Create a product class to fill the following 
requirements.

Product Class:
Attributes:

• Price

• Item Name

• Weight

• Brand

• Cost

• Status: default "for sale"
Methods:

• Sell: changes status to "sold"

• Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including 
sales tax

• Return: takes reason for return as a parameter and changes status accordingly. If the item is 
being returned because it is defective change status to defective and change price to 0. 
If it is being returned in the box, like new mark it as for sale. If the box has been opened set 
status to used and apply a 20% discount.

• Display Info: show all product details.
Every method that doesn't have to return something should return self so methods can be chained.
'''

class Products(object):
    def __init__ (self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = 'for sale'

    def sell(self):
        self.status = 'sold'
        return self
    
    def add_tax(self, tax):
        self.price = round((self.price + (self.price * tax)), 2)
        return self

    def return_reason(self, str):
        if str == 'defective':
            self.status = 'defective'
            self.price = 0
        if str == 'in box, like new':
            self.status = 'for sale'
        if str == 'open box':
            self.status = 'used'
            self.price = round((self.price * 0.8),2)
    
    def displayInfo(self):
        print 'Price: $' +str(self.price)
        print 'Item Name: ', self.item_name
        print 'Weight: ', self.weight
        print 'Brand: ', self.brand
        print 'Cost: ', self.cost
        print 'Status: ', self.status

product1 = Products(19.99, 'Shaver', '5lbs', 'Andis', 5)
product1.displayInfo()

product2 = Products(10.99, 'Trimmer', '1lbs', 'Oster', 2)
product2.sell().add_tax(0.13)
product2.displayInfo()

product3 = Products(49.99, 'Cleaner', '15lbs', 'Conair', 20)
product3.add_tax(0.15)
product3.displayInfo()

product4 = Products(29.99, 'Clipper', '12lbs', 'Wahl', 10)
product4.return_reason('open box')
product4.displayInfo()