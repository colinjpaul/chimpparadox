

#the decorator function
def tracer(func):
    def ifunc():
        print('calling')
        func()
        print('exiting')
    return ifunc

print('*' * 30)


@tracer
def foo():
    print('foo')

    
@tracer
def bar():
    print('bar')


foo()
bar()


##
##@tracer(bar)
##bar()





#@authentication
#@tracer
#@logger

#the above replaces this bit
#bar = authenticate(tracer(logger(bar))
#first one that gets applied is logger
#first one that gets called is authentication 

  
# @tracer replaces this

##foo = tracer(foo)
##foo()
##
##bar = tracer(bar)
##bar()
