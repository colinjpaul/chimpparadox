friends = ['Ger', 'David', 'Barry']
message = 'invite for '
print(message + friends[0])
print(message + friends[1])
print(message + friends[2])

noShow = friends.pop(1)
print(noShow + " can't make it ")

print(friends)

friends.insert(-1, 'Terence')
print(friends)

friends.append('Denis')
print(friends)

del friends[-1]

print(friends)



