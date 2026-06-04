Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=()
t=(1,1,1,1,1)
t
(1, 1, 1, 1, 1)
t=(1,1.1,'dfcgt',[])
t
(1, 1.1, 'dfcgt', [])
t=(10,20,30,40,50)
m=(30,40,50)
t+m
(10, 20, 30, 40, 50, 30, 40, 50)
t*m
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    t*m
TypeError: can't multiply sequence by non-int of type 'tuple'
t*3
(10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50)
(t+m)*2
(10, 20, 30, 40, 50, 30, 40, 50, 10, 20, 30, 40, 50, 30, 40, 50)
t[1]
20
t[0]
10
t[6]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t[6]
IndexError: tuple index out of range
t[4]
50
m[2]
50
t
(10, 20, 30, 40, 50)
t[:1]
(10,)
t[:2]
(10, 20)
t[:4]
(10, 20, 30, 40)
t[::-1]
(50, 40, 30, 20, 10)
t[::2]
(10, 30, 50)
t[:0:5:2]
SyntaxError: invalid syntax
t[:1:4]
(10,)
t[:4:2]
(10, 30)
t[:-3:-1]
(50, 40)
t[:-1:-3]
()
t
(10, 20, 30, 40, 50)
10 in t
True
50 in t
True
60 not in t
True
40 not in t
False
t[::-3]
(50, 20)
t
(10, 20, 30, 40, 50)
s.sorted(t)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s.sorted(t)
NameError: name 's' is not defined
sorted(t)
[10, 20, 30, 40, 50]
min(t)
10
max(t)
50
sum(t)
150
t.count(t)
0
t.index(t)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    t.index(t)
ValueError: tuple.index(x): x not in tuple
t.index(10)
0
t.count(10)
1
a=(1,2,3)
a
(1, 2, 3)
x,y,z=a
x
1
y
2
z
3
t=(1,2,3,[4,5,6],7,8)
t
(1, 2, 3, [4, 5, 6], 7, 8)
t[2]
3
t[4]
7
t[3]
[4, 5, 6]
t[2]=4
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
t
(1, 2, 3, [4, 5, 6], 7, 8)
t[5]
8
t[3]
[4, 5, 6]
t[1]
2
t[3].append(10)
t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
s=set()
s={1,1,1,1,1,1}
s
{1}
s={123,453,654,789,1,4,6,34,67,89}
s
{1, 34, 67, 4, 453, 6, 654, 789, 89, 123}
s=set()
s
set()
s.add(1)
s
{1}
s.add(34.456)
s
{1, 34.456}
s.add("wert")
s
{'wert', 1, 34.456}
s.add([1,2,3,4])
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    s.add([1,2,3,4])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add({1:2,2:2})
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    s.add({1:2,2:2})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.add((1,2,3,4))
s
{'wert', 1, 34.456, (1, 2, 3, 4)}
s{false,1,'wert',(1234),12.45}
SyntaxError: invalid syntax
s{false,1,'wert',(1,2,3,4),12.45}
SyntaxError: invalid syntax
{false,1,'wert',(1,2,3,4),12.45}
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    {false,1,'wert',(1,2,3,4),12.45}
NameError: name 'false' is not defined. Did you mean: 'False'?
s
{'wert', 1, 34.456, (1, 2, 3, 4)}
s
{'wert', 1, 34.456, (1, 2, 3, 4)}
1 in s
True
2 in s
False
3 in s
False
a={1,2,3,4,5,6,7,10}
b={4,5,11,12}
a|b
{1, 2, 3, 4, 5, 6, 7, 10, 11, 12}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 10, 11, 12}
a.intersection(b)
{4, 5}
a&b
{4, 5}
a-b
{1, 2, 3, 6, 7, 10}
a^b
{1, 2, 3, 6, 7, 10, 11, 12}
a
{1, 2, 3, 4, 5, 6, 7, 10}
#{1}{2}{3}{4}{5}{1,3}{1,5}{7,10}
a<={1}
False
a>={1}
True
a
{1, 2, 3, 4, 5, 6, 7, 10}
b
{12, 11, 4, 5}
a.isdisjoint{1, 2, 3, 4, 5, 6, 7, 10}9b
SyntaxError: invalid decimal literal
a.isdisjoint(b)
False
a.isdisjoint({20,40})
True
a
{1, 2, 3, 4, 5, 6, 7, 10}
a.add(17)
a
{1, 2, 3, 4, 5, 6, 7, 10, 17}
a.add(20)
a
{1, 2, 3, 4, 5, 6, 7, 10, 17, 20}
a.update({11,13,15})
a
{1, 2, 3, 4, 5, 6, 7, 10, 11, 13, 15, 17, 20}
a.pop(1)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a.pop(1)
TypeError: set.pop() takes no arguments (1 given)
pop(1)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    pop(1)
NameError: name 'pop' is not defined. Did you mean: 'pow'?
a.pop()
1
a.pop()
2
a.remove(5)
a
{3, 4, 6, 7, 10, 11, 13, 15, 17, 20}
a.remove(11)
a
{3, 4, 6, 7, 10, 13, 15, 17, 20}
a.discard(20)
a
{3, 4, 6, 7, 10, 13, 15, 17}
a.discard(7,4)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    a.discard(7,4)
TypeError: set.discard() takes exactly one argument (2 given)
a.discard(13)
>>> a
{3, 4, 6, 7, 10, 15, 17}
>>> a.clear()
>>> a
set()
>>> a
set()
>>> a={1,3,5,37,12}
>>> b={1,3,67,78}
>>> a
{1, 3, 37, 5, 12}
>>> b
{1, 67, 3, 78}
>>> a.intersection_update(b)
>>> a
{1, 3}
>>> b
{1, 67, 3, 78}
>>> b
{1, 67, 3, 78}
>>> c=b
>>> c.add(12)
>>> c
{1, 67, 3, 12, 78}
>>> c
{1, 67, 3, 12, 78}
>>> c.pop()
1
>>> c.mix()
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    c.mix()
AttributeError: 'set' object has no attribute 'mix'
>>> max(c)
78
>>> min(c)
3
>>> d=c.copy()
>>> d
{3, 67, 12, 78}
>>> c
{67, 3, 12, 78}
>>> sorted(c)
[3, 12, 67, 78]
>>> sum(c)
160
