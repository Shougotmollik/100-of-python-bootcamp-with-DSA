#make a list 
bikes=['trek','redline','giant']

#get the first item in a list 

first_bike = bikes[0]
print(first_bike)

#get the last iteam in a list 

last_bike=bikes[-1]
print(last_bike)

#looping through a list 

for bike in bikes:
    print(bike)

#adding iteams to a list 

bikes=[]
bikes.append('bajaj')
bikes.append('ktm')
bikes.append('yahama')
print(bikes)

#making numerical lists

squares =[]
for x in range (1,11):
    squares.append(x**2)
    print(x)