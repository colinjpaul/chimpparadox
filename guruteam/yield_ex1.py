def evens():
    val = 0
    while True:
        yield val
        val += 2

go = evens()

##
##def foo():
##    print('at start')
##    yield 1
##    yield 7
##    yield 11
##
##go = foo()  #this is asking for a generator (an initialiser.  on first go this won't print 'at start' string in 'def foo()'
##
