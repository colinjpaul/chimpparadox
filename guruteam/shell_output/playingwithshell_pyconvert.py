Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py =======
Traceback (most recent call last):
  File "C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py", line 23, in <module>
    with AutoSave(d, 'data2.json'):
  File "C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py", line 7, in __enter__
    self.fo = open(AutoSave.file_n, 'w') # will find autosave as in column 1
AttributeError: type object 'AutoSave' has no attribute 'file_n'
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py =======
Traceback (most recent call last):
  File "C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py", line 23, in <module>
    with AutoSave(d, 'data2.json'):
  File "C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py", line 7, in __enter__
    self.fo = open(AutoSave.file_n, 'w') # will find autosave as in column 1
AttributeError: type object 'AutoSave' has no attribute 'file_n'
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py =======
Traceback (most recent call last):
  File "C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py", line 29, in <module>
    print(file_name)
NameError: name 'file_name' is not defined
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py =======
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py =======
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py =======
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py =======
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py =======
>>> from collections import Counter
>>> Counter('abracadabra')
Counter({'a': 5, 'b': 2, 'r': 2, 'd': 1, 'c': 1})
>>> n = ['ann', 'dave', 'ann', 'mick']
>>> Counter(n)
Counter({'ann': 2, 'dave': 1, 'mick': 1})
>>> counter(n)['ann']
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    counter(n)['ann']
NameError: name 'counter' is not defined
>>> Counter(n)['ann']
2
>>> Counter(n)['mick']
1
>>> Counter(n)['jom']
0
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py =======
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py =======
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py =======
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py =======
<class 'ZeroDivisionError'>
Traceback (most recent call last):
  File "C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py", line 24, in <module>
    10 / 0 # exit will be called here; otherwise at end
ZeroDivisionError: division by zero
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/test_ctx_mgr_v2.py =======
None
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py =======
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py =======
always done
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py =======
some problem
always done
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py =======
<class 'ZeroDivisionError'>
always done
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py =======
<class 'FileNotFoundError'>
always done
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py =======
just IO error
always done
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py =======
just div by 0 error
always done
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py =======
just div by 0 error
always done
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py =======
just index error
always done
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py =======
programmer error
always done
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py =======
<class 'NameError'>
some problem
always done
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py =======
VCE error
always done
>>> dir()
['VCEError', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'sys', 'x']
>>> 
=============================== RESTART: Shell ===============================
>>> dir(__built_ins__)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dir(__built_ins__)
NameError: name '__built_ins__' is not defined
>>> dir(__builtins)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    dir(__builtins)
NameError: name '__builtins' is not defined
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py =======
VCE error
temp too high!
always done
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py =======
VCE error
temp too high!
<traceback object at 0x02F8D710>
always done
>>> dir(traceback)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    dir(traceback)
NameError: name 'traceback' is not defined
>>> import traceback
>>> dir(traceback)
['FrameSummary', 'StackSummary', 'TracebackException', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_cause_message', '_context_message', '_format_final_exc_line', '_some_str', 'clear_frames', 'collections', 'extract_stack', 'extract_tb', 'format_exc', 'format_exception', 'format_exception_only', 'format_list', 'format_stack', 'format_tb', 'itertools', 'linecache', 'print_exc', 'print_exception', 'print_last', 'print_list', 'print_stack', 'print_tb', 'sys', 'walk_stack', 'walk_tb']
>>> 
======= RESTART: C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py =======
VCE error
temp too high!
always done
Traceback (most recent call last):
  File "C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py", line 14, in <module>
    raise VCEError('temp too high!')
VCEError: temp too high!

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/paulc1/Desktop/VCE_Course/exception_stuff.py", line 21, in <module>
    print(traceback.print_stack(exc_tb))
  File "C:\Users\paulc1\AppData\Local\Programs\Python\Python35-32\lib\traceback.py", line 184, in print_stack
    print_list(extract_stack(f, limit=limit), file=file)
  File "C:\Users\paulc1\AppData\Local\Programs\Python\Python35-32\lib\traceback.py", line 201, in extract_stack
    stack = StackSummary.extract(walk_stack(f), limit=limit)
  File "C:\Users\paulc1\AppData\Local\Programs\Python\Python35-32\lib\traceback.py", line 329, in extract
    for f, lineno in frame_gen:
  File "C:\Users\paulc1\AppData\Local\Programs\Python\Python35-32\lib\traceback.py", line 285, in walk_stack
    yield f, f.f_lineno
AttributeError: 'traceback' object has no attribute 'f_lineno'
>>> 
=============================== RESTART: Shell ===============================
>>> n = [1, 7, 11, 42]
>>> map(lambda x: x*1.22, n)
<map object at 0x02FA7EF0>
>>> list (map(lambda x:x*1.22, n))
[1.22, 8.54, 13.42, 51.24]
>>> map(lambda x,y:x*1.22, m, n))
SyntaxError: invalid syntax
>>>  m = [10, 20, 30, 40]
 
SyntaxError: unexpected indent
>>> m = [10, 20, 30, 40]
>>> map(lambda x,y:x*y, m, n))
SyntaxError: invalid syntax
>>> map(lambda x,y:x*y, m, n)
<map object at 0x02FA7F10>
>>> list(map(lambda x,y:x*y, m, n))
[10, 140, 330, 1680]
>>> list(zip(m,n))
[(10, 1), (20, 7), (30, 11), (40, 42)]
>>> from itertools import zip_longest
>>> list(zip_longest(m,n))
[(10, 1), (20, 7), (30, 11), (40, 42)]
>>> m = [10, 20, 30]
>>> list(zip_longest(m,n))
[(10, 1), (20, 7), (30, 11), (None, 42)]
>>> [    x * 1.22   for x in n]
[1.22, 8.54, 13.42, 51.24]
>>> for item in [    x * 1.22   for x in n]:
	print(item)

	
1.22
8.54
13.42
51.24
>>> for item in [    x * 1.22   for x in n]:
