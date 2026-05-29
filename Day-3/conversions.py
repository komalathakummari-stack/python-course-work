Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
t=999.99
type(t)
<class 'float'>
c=112+8j
type(c)
<class 'complex'>
<class 'complex'>
SyntaxError: invalid syntax
s='fgrewx'
type(s)
<class 'str'>
>>> s='sfrew'
>>> type(s)
<class 'str'>
>>> 1=[]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> l=[]
>>> l=list()
>>> type(1)
<class 'int'>
>>> t=()
>>> t=(1,34,2,56,8)
>>> type(t)
<class 'tuple'>
>>> s=1,2,3,4)
SyntaxError: unmatched ')'
>>> s=(1,2,3,4)
>>> type(s)
<class 'tuple'>
>>> s=set()
>>> s=(345,5436,1352)
>>> a
10
>>> s
(345, 5436, 1352)
>>> {345,5436,13352)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> d={'name':'avg','age':'198','course':'hytr'}
>>> type(d)
<class 'dict'>
>>> status=true
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    status=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> status=True
>>> status=False
>>> type(status)
<class 'bool'>
>>> a=none
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a=none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> type(a)
<class 'int'>
