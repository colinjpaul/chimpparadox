def evens():
    def colin():
        print('in here')
    yield colin
    yield 42

go = evens()
