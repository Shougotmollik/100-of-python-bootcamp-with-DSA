# conditional tests

# equals                  x==42
# not equal               x!=42
# greater than            x>42
# or equal to             x>=42
# less than               x<42
# or equal to             x<=42




#conditional test with lists 
bikes=['trek','redline','giant']
for truk in bikes:
    if bikes[0] =='trek' :
        print("true ")
    else:
        print("false")

#assings bolean values 
games_active=True
can_edit=False

# a simple id test 

age=18
if age >=18:
    print("you can vote !")

#if-elif-else statement 

if age <4:
    print("Ticket price 0 $")
elif age<18:
    print("tikcket price 10 $")
else:
    print("Ticket peice 15 $")