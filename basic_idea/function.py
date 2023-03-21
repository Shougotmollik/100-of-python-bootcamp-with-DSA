# A simple function 

def greet_user():
    """Display a simple greeting"""
    print("Hello world")

greet_user()


#passing an argument 

def greet_user(username):
    """display a personalised greeting """
    print("Hello, " + username + "!")

greet_user('shougot_mollik')


#default values for parameters

def make_pizza(topping='bacon'):
    """making a single topping pizza """
    print("have a "+topping +" pizza")

make_pizza()
make_pizza("pepperoni")


#retuning a value 

def add_number (x,y):
    """add to number for return sum"""
    return x+y

sum=add_number(1090,383)
print(sum)

