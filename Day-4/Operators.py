Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=20
b=20
a
20
a+b
40
a-b
0
a*b
400
a/b
1.0
9/2
4.5
a//b
1
a%b
0
a**b
104857600000000000000000000
9%3
0
a<b
False
a>b
False
a<=b
True
a>=b
True
a==b
True
a!=b
False
a=b
a+=b
1=4
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
y=y+10
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    y=y+10
NameError: name 'y' is not defined
y=5
y
5
y=y+10
y
15
y+=15
y
30
y-=10
y
20
y/+10
2.0
y/=10
y
2.0
y=5
y
5
y=y+10
y
15
15
15
y+=10
y
25
y-=10
y
15
y*=10
y
150
y**=10
y
5766503906250000000000
y=10
y
10
a&20==0 and b%20==0 and a>b
True
a%20==0 and a%20==0 and a>b
True
not a>b
False
#str,list,tuple,set,dict
a='python programming'
'y' in a
True
'g' not in a
False
f' in a'
' in a'
'f' in a
False
l=['python','jaya','mysql']
'java' in k
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    'java' in k
NameError: name 'k' is not defined
'java' in l
False
'javascript' non in l
SyntaxError: invalid syntax
'mysql' not in l
False
t=[1,2,3,4,5]
t in 2
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    t in 2
TypeError: argument of type 'int' is not a container or iterable
3 in t
True
6 in t
False
set={'oil':120,'sugar':40,'salt':30}
oil in s
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    oil in s
NameError: name 'oil' is not defined
'oil' in s
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    'oil' in s
NameError: name 's' is not defined
NameError: name 's' is not defined
SyntaxError: invalid syntax
d={'oil':120,'sugar':40}
'oil' in d
True
40 in d
False
l=[1,2,3,4,5]
m=[1,2,3,4,5]
l==m
True
n=m
m==l
True
n=m
n
[1, 2, 3, 4, 5]
m
[1, 2, 3, 4, 5]
1 is m
False
>>>  6 is n
...  
SyntaxError: unexpected indent
>>> 1 is n
False
>>> 2 in m
True
>>> 6 in l
False
>>> n is m
True
>>> id(l)
3107266405696
>>> id(m)
3107295434176
>>> id(n)
3107295434176
>>> l is not m
True
>>> True
True
>>> n is not l
True
>>> 8 & 14
8
>>> 8 % 7
1
>>> 8&7
0
>>> 8|7
15
>>> 10^11
1
>>> ~12
-13
>>> 15>>1
7
>>> 15>>3
1
>>> 15>>1
7
>>> 16<<2
64
>>> 4<<2
16
