movies = list()

movie1 = dict()
movie1['Director'] = 'James Cameron'
movie1['Title'] = 'Avatar'
movie1['Release Date'] = '18 December 2009'
movie1['Running Time'] = '162 minutes'
movie1['Rating'] = 'PG-13'
movies.append(movie1)
movie2 = dict()
movie2['Director'] = 'David Fincher'
movie2['Title'] = 'The Social Network'
movie2['Release Date'] = '01 October 2010'
movie2['Running Time'] = '120 minutes'
movie2['Rating'] = 'PG-13'
movies.append(movie2)

keys = ['Title', 'Director', 'Rating', 'Running Time']

print ('*' * 30)
print (movies)
print ('*' * 30)

for item in movies:
    print ('*' * 30)
    for key in keys:
        print (key, ': ', item[key])

print ('*' * 30)

