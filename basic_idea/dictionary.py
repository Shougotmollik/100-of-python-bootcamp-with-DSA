#a simple dictionary 
alien={'color' : 'green','points':5}
print(alien)

# Accesing a value 

print("The alien's color is " + alien['color'])

#Adding a new key_value pair
alien['x_position']=0
print(alien)

#Looping through all keY_VALUE pairs

fav_numbers={'eric':17,'ever':4}
for name,number in fav_numbers.items():
    print(name + ' loves' + str(number))

#looping through all keys 

fav_numbers={'eric':17,'ever':4}
for number in fav_numbers.values():
    print(str(number)+' loves a number')

#looping through all the values 
fav_numbers={'eric':17,'ever':4}
for number in fav_numbers.values():
    print(name +'loves a number')

#looping through all the values 

fav_numbers={'eric':17,'ever':4}
for number in fav_numbers.values():
    print(str(number) + ' is a favorite')

