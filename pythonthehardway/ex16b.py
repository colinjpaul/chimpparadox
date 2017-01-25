from sys import argv

script, filename = argv

print "We're going to read %r " %filename
print "To cancel hit CTRL-C "
print "To carry on reading, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'r')

print (target.read())

print "Finally we close it"
target.close()

