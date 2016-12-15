class CtxMgr:
    def __enter__(self):
        print('entering')

    def __exit__(self,x,y,z):
        print('exiting')
     


# only need an initialiser (__init__) if you have a paramter for 'CtxMgr()'
with CtxMgr():
    
    #__enter__(self):  this is done automatically
    # 'with' you have to do 'enter' and 'exit'
    print('in code block')
   
print ('at end')
