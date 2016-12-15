def foo():
    print('foo')

foo()

bar = foo
bar()

if id(foo) == id(bar):
    print('same thing')

if foo is bar:
    print('yep, same again')
