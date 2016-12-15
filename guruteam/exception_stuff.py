import sys
class VCEError(Exception):
    pass

try:
    #10/0  #div by 0 error
    #open('xxx') # file error

    #li = []
    #print(li[100])  # index error

    x = 101
    if x > 100:
        raise VCEError('temp too high!')

except VCEError:
    import traceback
    print ('VCE error')
    exc_type, exc_obj, exc_tb = sys.exc_info()
    print(exc_obj)
    print(traceback.print_stack(exc_tb))
    

except IOError:
    print('just IO error')
    exc_type, exc_obj, exc_tb = sys.exc_info()

except (ZeroDivisionError, IndexError):
    print('programmer error')
    
except Exception:
    exc_type, y, z = sys.exc_info()
    print(exc_type)
    print('some problem')
    
finally:
    print('always done')
