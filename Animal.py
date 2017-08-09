#Animal
'''
Create an Animal class and give it the below attributes and methods. Extend the Animal class to two 
child classes, Dog and Dragon.

Animal Class
Attributes:

• name

• health
Methods:

• walk: decreases health by one

• run: health decreases by five

• display health: print to the terminal the animal's health.
Create an instance of the Animal, have it walk() three times, run() twice, and finally displayHealth() 
to confirm that the health attribute has changed.

Dog Class
• inherits everything from Animal
Attributes:

• default health of 150
Methods:

• pet: increases health by 5
Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().

Dragon Class
• inherits everything from Animal
Attributes:

• default health of 170
Methods:

• fly: decreases health by 10

• display health: prints health by calling the parent method and prints "I am a Dragon"
Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, and its 
displayHealth() is not saying 'this is a dragon!'. Also confirm that your Dog class can not fly().
'''

class Animal(object):
    def __init__ (self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health = self.health - 1
        return self
    
    def run(self):
        self.health = self.health - 5
        return self
    
    def display_health(self):
        print "My Name is " + str(self.name)
        print "My health is " + str(self.health)


class Dog(Animal):
    def __init__ (self, name):
        super(Dog, self).__init__(name)
        self.health = 150
 
    def pet(self):
        self.health = self.health + 5
        return self


class Dragon(Animal):
    def __init__ (self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health = self.health - 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"


animal1 = Animal('Cheetah')
animal1.walk().walk().walk().run().run()
animal1.display_health()

dog1 = Dog('Buster')
dog1.walk().walk().walk().run().run().display_health()

dragon1 = Dragon('Puff')
dragon1.fly().display_health()






