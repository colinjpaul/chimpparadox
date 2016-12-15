import os
os.environ['USER'] = 'Colin'

   
def logger(func):
    def ifunc():
        print('calling',func.__name__)
        func()
    return ifunc

def auth(func):
    def ifunc():
        if os.environ['USER'] == 'Colin':
            func()
            print('allowed',func.__name__)
    return ifunc
##@auth
def foo():
    print('foo')
    
@auth    
@logger
def bar():
    print('bar')

# for @ comment this two line as @ call them up
foo = auth(logger(foo))
#bar = logger(bar)

foo()
foo()
bar()
bar()



