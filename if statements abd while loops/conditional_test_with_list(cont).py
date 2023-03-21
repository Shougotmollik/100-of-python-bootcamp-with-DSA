#testing if a value is not in a list 

banned_users=['ann','chad','dee']
user='eric'

if user not in banned_users:
    print("You can play")

#checking if a list is empty 

players=[]

if players:
    for player in players:
        print(f"{player}" + player.title())
else:
    print("we have no player yet !")

