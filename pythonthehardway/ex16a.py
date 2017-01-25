from sys import argv

script, filename = argv

print "We're going to erase %r " %filename
print "To cancel hit CTRL-C "
print "To carry on deleting, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now provide input for each of the following three lines"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Now will write those to file"

target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)
# target.write('\n')

print "Finally we close it"
target.close()

