# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

contents = fh.read()
print contents.upper().rstrip()

