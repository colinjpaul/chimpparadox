name = raw_input("Enter file name: ")
if len(name) < 1:
    name = "C://Users//paulc1//Documents//GitHub//chimpparadox//testfiles/mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()

    if len(words[0]) != 4:
        continue
    word = words[5]
    hour = word[0:2]












