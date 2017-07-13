items = [1, 2, 3, 4, 5]

''' Long Way
squared = []
for i in items:
    squared.append(i**2)
'''

# Better way
squared = list(map(lambda x: x**2, items))


