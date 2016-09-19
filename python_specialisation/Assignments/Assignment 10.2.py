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

    # We want to exclude 'From:' (i.e. no colon)
    if len(words[0]) != 4:
        continue

    # Extract Time
    word = words[5]
    # Extract Hour
    hour = word[0:2]

    # Store how many times each 'hour' occurs
    counts[hour] = counts.get(hour, 0) + 1

    # Create list to store key, value pairs so that they can be manipulated
    lst = list()

    # Populate list

for hour, count in counts.items():
    lst.append((hour, count))

lst.sort()

for key, val in lst:
    print key, val




























