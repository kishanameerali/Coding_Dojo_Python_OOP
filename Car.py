#Car
'''
Create a class called  Car. In the__init__(), allow the user to specify the following attributes: 
price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. 
Otherwise, set the tax to be 12%. 

Create six different instances of the class Car. In the class have a method called display_all() that 
returns all the information about the car as a string. In your __init__(), call this display_all() 
method to display information about the car once the attributes have been defined.
'''

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        
        self.display_all()
        
    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + "mpg"
        print "Tax: " + str(self.tax)

Car1 = Car(1000, 35, 'Full', 15)
Car2 = Car(2000, 5, 'Not Full', 105)
Car3 = Car(3000, 15, 'Kind of Full', 95)
Car4 = Car(4000, 25, 'Almost Full', 25)
Car5 = Car(20000, 60, 'Empty', 10)
Car6 = Car(40000, 55, 'Full', 33)
    
