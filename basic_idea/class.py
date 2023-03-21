#creating a dog class 

class dog():
    """Represent  a dog """
    def __init__(self,name):
        """Intilize dog object"""
        self.name=name
    def sit(self):
        """simukating sitting"""
        print(self.name + " is sitting.")
    
my_dog=dog('peso')

print(my_dog.name + "is a search dog")
my_dog.sit()