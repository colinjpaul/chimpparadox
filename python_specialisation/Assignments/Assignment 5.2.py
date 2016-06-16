largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    try:
        if num == "done":
            break
        if largest == None:
            largest = int(num)
        elif int(num) > largest:
            largest = int(num)
        if smallest == None:
            smallest = int(num)
        elif int(num) < smallest:
            smallest = int(num)
    except:
        print "invalid number"


print "Maximum", largest
print "Minimum", smallest