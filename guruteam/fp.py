
def gen(name):
    def hi(name2):
        print('hi', name, name2)
        
    return hi
    #the address of a function called 'hi'
    #can only be used inside gen()


#function generated a functions and does this...
outer = gen('joe') 
outer('jones')
#outer()

outer2 = gen('sue')
outer2()


###'closure'  - 'jones' and 'sue' are examples
##


    
