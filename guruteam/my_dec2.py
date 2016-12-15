
def tracer(case):
    def idec(func):
        def ifunc():
            if case == 'lower':
                print('calling')
            else:        
                print('CALLING')
            func()
            if case == 'lower':
                print('exiting')
            else:
                print('EXITING')
        return ifunc
    return idec

def foo():
    print('foo')
dec = tracer('upper')
foo = dec(foo)

def bar():
    print('bar')
dec = tracer('lower')

foo()
bar()

