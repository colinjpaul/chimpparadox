##import pdb
##pdb.set_trace()


## meta class module
class MyChecker(type):   #this would normally be 'object'
    def __new__(cls, name, bases, attr):      #cls is like 'self' for classes
        if '__init__' not in attr:
            raise Exception('must have __init__')
        return type.__new__(cls, name, bases, attr)

class DocChecker(type):   #this would normally be 'object'
    def __new__(cls, name, bases, attr):      #cls is like 'self' for classes
        if '__init__' not in attr:
            raise Exception('must have __init__')
        return type.__new__(cls, name, bases, attr)
        


class C(metaclass=MyChecker):
    """C is a test class
    has a no arg ctor
    """
    def __init__(self):
        self.mol = 42
        """The initialiser sets up
        the mol
        """
    

#Metaclasses allow us to catch issues like the above where we only have
#one underscore

obj = C()

