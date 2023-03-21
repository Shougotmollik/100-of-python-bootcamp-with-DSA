#storing a dictionaries list 

#start with empty list
users=[]


#making a new user ,and add them to the list 

new_user={
    'last':'fermi',
    'first':'enrico',
    'username':'efrmi'
}
users.append(new_user)
print(users)

#making another new user 

my_user={
    'first':'shougot',
    'last':'mollik',
    'username':'shougot mollik'
}
users.append(my_user)
print(users)


#show all informations about each user 

for user_dict in users:
    for s,m in user_dict.items():
        print(f"{s} : {m}")
    print("\n")


# without using append 

user=[
    {
    'last':'fermi',
    'first':'enrico',
    'username':'efrmi'
    },
    {
    'first':'shougot',
    'last':'mollik',
    'username':'shougot mollik'
    }
]

#showing all the info 

for user_dict1 in user:
    for a,b in user_dict1.items():
        print(f"{a} : {b}")
        print("\n")