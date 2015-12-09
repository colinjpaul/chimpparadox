
def multiples_of_3_or_5():
    for number in range(10):
        if not number % 3 or not number % 5:
            yield number
print(sum(multiples_of_3_or_5()))

print ("puzzles")





