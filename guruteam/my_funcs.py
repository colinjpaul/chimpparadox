def info(*numbers):  #this makes numbers a tuple
    
    print(numbers)
    return ( sum(numbers),
             sum(numbers) / len(numbers),   
             max(numbers),
             min(numbers))

total, avg, maximum, minimum = info(1,7,11,42)

print(total,avg,maximum,minimum)

nos = [1,7,11,42]
print (info (*nos))




