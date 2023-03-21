name=['ben','ten','ant','shougot','mollik','github','google','microsoft']

#using a loop to generate a list of aquare numbers 

squares=[]
for x in range(1,11):
    square=x**2
    squares.append(square)
print(squares)


#using a comprehension to generate a list of square numbers 

squares=[x**2 for x in range(1,11)]
print(squares)

#using a loop to convert a list of names to names to upper case 

names=['ben','ten','ant','shougot','mollik','github','google','microsoft']

upper_names=[]
for name in names:
    upper_names.append(name.upper())
print(upper_names)


#using a comprehesion to convert a list of names to upper case 

upper_names=[name.upper()for name in names]

print(upper_names)