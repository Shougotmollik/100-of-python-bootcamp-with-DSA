# Build a list and print the iteams in the list 

dogs=[]
dogs.append('whille')
dogs.append('hootz')
dogs.append('peso')
dogs.append('goblin')

for dog in dogs:
    print(f"Hello {dog}!")
print("I love these dogs !")

print("\n These were my first two dogs :")
old_dogs=dog[:2]
for old_dog in old_dogs:
    print(old_dog)

del dogs[0]
dogs.remove('peso')
print(dogs)