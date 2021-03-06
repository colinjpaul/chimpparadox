from collections import defaultdict


#countries = defasultdict( lambda : 0)
#below does the samas as the comment above
countries = defaultdict (int)

## context manager
with open(r'C:\Users\cjadmin\Documents\GitHub\chimpparadox\guruteam\testdata\test_locations.txt','rt')as infile:
    for entry in infile:
        entry = entry.rstrip('\n')
        fields = entry.split(':')
        country = fields[-1]
##        if country not in countries:
##        else:
##            countries[country] += 1

##      same as commented out code above
        countries[country] += 1

print('BEFORE SORT')
print(countries)
print('AFTER SORT')
print(sorted( countries, key=lambda country:countries[country], reverse=True))


#instead of lambda you could do this...

def by_frequency(country):
    return countries[country]
