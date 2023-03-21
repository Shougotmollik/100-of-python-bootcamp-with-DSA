#letting the user choose when to quit

prompt="\n tell me something , and i'll"
prompt+="repeat it back to you"
prompt+="\n Enter 'quit' to end the program. "

message=""
while message !='quit':
    message=input(prompt)

    if message !='quit':
        print(message)


#using flag 

active= True
while active:
    message=input(prompt)

    if message =='quit':
        active=False
    else:
        print(message)

#using braek to exit loop 

while True:
    city =input(prompt)

    if city =='quit':
        break
    else:
        print(f"I've been to {city}")


#using continue loop 

banded_player=['messi','ronaldo','naymer','pele','gezeeman','robin']
prompt='\n Add a player to your team.'
prompt+='\n Enter "quit" when you are done.'

players=[]

while True:
    player=input(prompt)
    if player =='quit':
        break
    elif player in banded_player:
        print(f"{player} is banned")
        continue
    else:
        players.append(player)

print("\n your team :")
for player in players:
    print(player)