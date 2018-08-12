class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes. """
        self.name = name
        self.age = age 
        
    def sit(self):
        print(self.name.title()+ " is now sitting")
        
    def roll_over(self):
        print(self.name.title()+ " rolled over!")
        
        
mydog = Dog("wiliam", 8)
print("my dog name is: " + mydog.name.title())
print("My dog is: " + str(mydog.age) + " . ")
mydog.sit()
mydog.roll_over()


class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        
    def describle_restaurant(self):
        print(self.name.title())
        print(self.type.title())
    
    def open_restaurant(self):
        print(self.name.title()+ " is open")
        
my = Restaurant("bac","Viet nam")
my.describle_restaurant()
        
        
        
        
        
        
        
        
        
        
        
        