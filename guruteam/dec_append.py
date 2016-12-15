import sys
import os

os.environ['USERNAME'] = 'paulc1'

fn = r'C:\Users\paulc1\Desktop\VCE_Course\data\test_file_2.txt'

def logger(func):
    def ifunc():    
        print('calling',func.__name__)
        func()
        print('writing to file')
        f = open(fn, 'at')
        content = 'function called'
        f.write(content)
        
    return ifunc

def auth(func):
    def ifunc():
        if os.environ['USERNAME'] == 'paulc1':
            func()
            print('allowed', func.__name__)
    return ifunc


#@logger
#@auth
def foo():
    print('foo writing to file')

@logger
#@auth
def bar():
    print('bar writing to file')

foo()
bar()







    
