import re

x = 'My 2 favourite numbers are 7 and 13'
y = re.findall('[0-9]+',x)

print y

y = re.findall('[AEIOU]+',x)
print y

#continue from 16:17 regex part 1