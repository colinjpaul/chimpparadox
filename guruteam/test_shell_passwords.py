
import pdb
pdb.set_trace()
import collections


file_name = "C:\\Users\\paulc1\\Desktop\\VCE_Course\\data\\test_file_1.txt"
fhand = open(file_name)

count = dict()
for line in fhand:
    words = line.split(':')
    country = words[2]

    print (country)
    
    for word in words:
        count[country] = count.get(word, 0) + 1

print (count)

lst = list()
for key, val in count.items():
    lst.append((val, key))

lst.sort(reverse=True)

for val, key in lst[:10]:
    print (key, val)


#shorter version

##c = {'a': 10, 'b':1, 'c': 22}
##
##print sorted([(v, k) for k, v in c.items()])



##
##lst = list()
##
##for key, val in count.items():
##    lst.append((val, key))
##
##lst.sort()
##
##print (lst)






##for val, key in list():
##    print (key, val)


##for line in handle:
##    line = line.rstrip()
##    words = line.split(':')
##    print (words)
##
##    print (words[2])

##    count[
##    print (count[words[2]])

##  count[words[2]] = counts.get(words[2], 0) + 1
##    for word, count in counts.items():
##        if  big_count is None or count > big_count:
##            shell_list.append((word, count))
##
##print (sorted(shell_list))
    




        
   

    






