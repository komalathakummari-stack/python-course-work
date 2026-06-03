Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=' hello world '
s
' hello world '
s.strip()
'hello world'
s.lstrip()
'hello world '
s.rstrip()
' hello world'
s='string.py'
s
'string.py'
s.startswith('str')
True
s.startswith('gfs')
False
s.endswith('py')
True
s.endswith('ing')
False
'shytgf'.isalpha()
True
'afuhtgb1234'.isalpha()
False
'adtgrfj123@#$%'.isalpha()
False
'qwwuyhgf12345'.isalnum()
True
'12344'.isalnum()
True
'ARFDSEabchddr12345'.isalnum()
True
'qmajhsgst'.islower()
True
'qjqhwttwqikjw12345@#$%'.islower()
True
'adffgASDGG1233!@#$'.islower()
False
'ASDTRF1234!@#$'.isupper
<built-in method isupper of str object at 0x000001B10BA509B0>
'ASDFGUUK12345@#$'.isupper()
True
' '.isspace()
True
'dfgjuujyf      '.isspace()
False
'py_python'.isidentifier()
True
'py@123'.isidentifier()
False
1=[]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l=[]
l=list
l=list()
type(l)
<class 'list'>
l=[10,20,30,40,50]
l*9
[10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
l+3
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    l+3
TypeError: can only concatenate list (not "int") to list
l=[10,20,30,40,50]
m=[30,46,29,39,32]
l+m
[10, 20, 30, 40, 50, 30, 46, 29, 39, 32]
l*m
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    l*m
TypeError: can't multiply sequence by non-int of type 'list'
l*5
[10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
l=[1,2,3,4,5]
l[3]
4
l[4]
5
l[5]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    l[5]
IndexError: list index out of range
l[::2]
[1, 3, 5]
l[:-1]
[1, 2, 3, 4]
l[1:2:4]
[2]
l[:-1::2]
SyntaxError: invalid syntax
l[:-1:2]
[1, 3]
l[-3::-1]
[3, 2, 1]
l
[1, 2, 3, 4, 5]
2 in l
True
6 in l
False
4 in l
True
3not in l
False
8 not in l
True
5 in l
True
6709 in l
False
l
[1, 2, 3, 4, 5]
id[l]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    id[l]
TypeError: 'builtin_function_or_method' object is not subscriptable
id[1]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    id[1]
TypeError: 'builtin_function_or_method' object is not subscriptable
l[4]
5
id(l)
1859916218304
l[4]
5
l
[1, 2, 3, 4, 5]
l.append(6)
l
[1, 2, 3, 4, 5, 6]
l.append(10)
l
[1, 2, 3, 4, 5, 6, 10]
l.insert(1,4)
l
[1, 4, 2, 3, 4, 5, 6, 10]
l.insert(6,7)
l
[1, 4, 2, 3, 4, 5, 7, 6, 10]
l.extend([20,30,40])
l
[1, 4, 2, 3, 4, 5, 7, 6, 10, 20, 30, 40]
l.extend([50])
l
[1, 4, 2, 3, 4, 5, 7, 6, 10, 20, 30, 40, 50]
l.pop()
50
l
[1, 4, 2, 3, 4, 5, 7, 6, 10, 20, 30, 40]
l.pop(5)
5
l
[1, 4, 2, 3, 4, 7, 6, 10, 20, 30, 40]
l.remove()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    l.remove()
TypeError: list.remove() takes exactly one argument (0 given)
l.remove(2)
l
[1, 4, 3, 4, 7, 6, 10, 20, 30, 40]
l.del(1)
SyntaxError: invalid syntax
l.del[1]
SyntaxError: invalid syntax
del[2]
SyntaxError: cannot delete literal
dell[2]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    dell[2]
NameError: name 'dell' is not defined
del l[2]
l
[1, 4, 4, 7, 6, 10, 20, 30, 40]
del l[1]
l
[1, 4, 7, 6, 10, 20, 30, 40]
del l[7]
l
[1, 4, 7, 6, 10, 20, 30]
l.clear()
l
[]
id
<built-in function id>
id[]
SyntaxError: invalid syntax
id()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    id()
TypeError: id() takes exactly one argument (0 given)
l
[]
l=[1, 2, 3, 4, 5]
l
[1, 2, 3, 4, 5]
>>> sorted(l)
[1, 2, 3, 4, 5]
>>> l.sort()
>>> l
[1, 2, 3, 4, 5]
>>> min(l)
1
>>> max(l)
5
>>> l.revers()
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    l.revers()
AttributeError: 'list' object has no attribute 'revers'. Did you mean: 'reverse'?
>>> l.reverse()
>>> l
[5, 4, 3, 2, 1]
>>> sorted(l,reverse=True)
[5, 4, 3, 2, 1]
>>> l.index(2)
3
>>> l.index(1)
4
>>> l.count(3)
1
>>> l.count(1)
1
>>> l.count(5)
1
>>> l.count(6)
0
>>> l
[5, 4, 3, 2, 1]
>>> len(l)
5
>>> sum(l)
15
>>> # 0 0.0 '' [] () set() false
>>> any([1,2,3,4,0,0,0,0,0])
True
>>> all([1,2,3,4,5,5,0,0,0,0,0])
False
>>> all([0,0,0,0,0,0])
False
>>> all([1,2,3,4,5])
True
