ailen_0={'color': 'green','points':5}

#getting the value associate with a key 

print(ailen_0['color'])
print(ailen_0['points'])

#getting the value with get()

alien_0={'color':'green'}

alien_color=ailen_0.get('color')
ailen_points=alien_0.get('points',0)

print(alien_color)
print(ailen_points)