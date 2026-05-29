listcomplex(t)
Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
b=10.5
int(b)
10
complex(b)
(10.5+0j)
str(b)
'10.5'
list(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(c)
NameError: name 'c' is not defined
bool(b)
True
bool(0.0)
False
c=2+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(2+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
s='komali'
a='1245267'
b='23456.76589'
int(a)
1245267
int(s)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'komali'
int(b)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: '23456.76589'
float(s)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'komali'
float(a)
1245267.0
float(b)
23456.76589
complex(s)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
complex(a)
(1245267+0j)
complex(b)
(23456.76589+0j)
str(a)
'1245267'
str(s)
'komali'
str(b)
'23456.76589'
list(a)
['1', '2', '4', '5', '2', '6', '7']
list(a)
['1', '2', '4', '5', '2', '6', '7']
list(b)
['2', '3', '4', '5', '6', '.', '7', '6', '5', '8', '9']
tuple(a)
('1', '2', '4', '5', '2', '6', '7')
tuple(s)
('k', 'o', 'm', 'a', 'l', 'i')
tuple(b)
('2', '3', '4', '5', '6', '.', '7', '6', '5', '8', '9')
set(s)
{'a', 'o', 'm', 'l', 'k', 'i'}
set(a)
{'1', '2', '5', '7', '4', '6'}
set(b)
{'8', '.', '2', '5', '7', '9', '4', '6', '3'}
dict(a)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(s)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    dict(b)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> bool(a)
True
>>> bool(s)
True
>>> bool(b)
True
>>> a=[1,4,2,5,8,9]
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> float(a)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'list'
>>> complex(a)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    complex(a)
TypeError: complex() argument must be a string or a number, not list
>>> str(a)
'[1, 4, 2, 5, 8, 9]'
>>> tuple(a)
(1, 4, 2, 5, 8, 9)
>>> set(a)
{1, 2, 4, 5, 8, 9}
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    dict(a)
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence
>>> status=True
status(s)


