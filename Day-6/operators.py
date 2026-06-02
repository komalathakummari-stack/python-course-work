Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name=input()
komali
name
'komali'
name=input("Enter your name")
Enter your name:komali
name
':komali'
':komali'
':komali'
age=input("Enter ypur age")
Enter ypur age:22
age
':22'
type(gpa)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(gpa)
NameError: name 'gpa' is not defined
type(age)
<class 'str'>
gpa=float(input("Enter the cpa: "))
Enter the cpa: 8.0
gpa
8.0
type(gpa)
<class 'float'>
'komali vaishnavi bhargavi pravalika sruthi'
'komali vaishnavi bhargavi pravalika sruthi'
'komali vaishanvi bhargavi pravalika sruthi'.split(' ')
['komali', 'vaishanvi', 'bhargavi', 'pravalika', 'sruthi']
products=input("enter the product").split()
enter the product:laptop mouse charger keyboard
products
[':laptop', 'mouse', 'charger', 'keyboard']
topics=tuple(input("enter the topics: ").split())
enter the topics: token statement variables comments
topics
('token', 'statement', 'variables', 'comments')
op=set(input("enter the oper: ").split())
enter the oper: in not in is not and or not 
op
{'not', 'in', 'is', 'or', 'and'}
{'not', 'in', 'is', 'or', 'and'}
{'and', 'not', 'in', 'is', 'or'}
list(map(int,input("enter the marks: ").split()))
enter the marks: 3,4,5,78,94
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(map(int,input("enter the marks: ").split()))
ValueError: invalid literal for int() with base 10: '3,4,5,78,94'
list(map(int,input("enter the marks: ").split()))
enter the marks: 3 65 78 984
[3, 65, 78, 984]
prices=tuple(map(int,input("enter the prices: ").split()))
enter the prices: 6453 6758 9876 5674
prices
(6453, 6758, 9876, 5674)
rating=set(map(int,input("enter the prices: ").split()))
enter the prices: 4 3 4 2 3 3 
ratings
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    ratings
NameError: name 'ratings' is not defined. Did you mean: 'rating'?
rating=set(map(int,input("enter the rating: ").split()))
enter the rating: 4 2 3 3 5 5 
ratings
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    ratings
NameError: name 'ratings' is not defined. Did you mean: 'rating'?
rating
{2, 3, 4, 5}
per=list(ma(float,input("enter the per's: ").split()))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    per=list(ma(float,input("enter the per's: ").split()))
NameError: name 'ma' is not defined. Did you mean: 'max'?
per=list(map(float,input("enter the per's: ").split()))
enter the per's: 56.3 65.3 5638.4
per
[56.3, 65.3, 5638.4]
prices=list(map(float,input("enter the perces: ").split()))
enter the perces: 567 568 873 875
prices
[567.0, 568.0, 873.0, 875.0]
prices=set(map(float,input("enter the prices: ").split()))
enter the prices: 536 783 678 9836
prices
{536.0, 9836.0, 678.0, 783.0}
prices=tuple(map(float,input("enter the perces: ").split()))
enter the perces: 543 678 7654 
prices
(543.0, 678.0, 7654.0)
a,d=10,20
a
10
b
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    b
NameError: name 'b' is not defined
d
20
a,d=(10,20)
a
10
d
20
a,d=[10,20]
a
10
d
20
username,password=input("enter the username & password: ").split()
enter the username & password: codegnan c1234
username
'codegnan'
password
'c1234'
a,b,c,d=list(map(int,input("enter the 4 sides: ").split()))
enter the 4 sides: 5 7 4 5
a
5
b
7
c
4
d
5
price,discount=list(map(float,input().split()))
5647 10.0
price
5647.0
discount
10.0
a=eval(input())
6547
a
6547
a=eval(input())
4536.7465
a
4536.7465
a=eval(input())
(1,2,3,4,4,5)
a
(1, 2, 3, 4, 4, 5)
a=eval(input())
[1,3,2,4,5,6]
>>> a
[1, 3, 2, 4, 5, 6]
>>> a=eval(input())
{1,2,3,4,5}
>>> a
{1, 2, 3, 4, 5}
>>> a=eval(input())
{3:6,4:6,8:3}
>>> a
{3: 6, 4: 6, 8: 3}
>>> a=eval(input())
true
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a=eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a=eval(input())
True
>>> type(a)
<class 'bool'>
>>> s='python programming lang'
>>> s
'python programming lang'
>>> type(s)
<class 'str'>
>>> s=''
>>> s
''
>>> a='codegnan'
>>> b='pfs'
>>> a+b
'codegnanpfs'
>>> a*10
'codegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnancodegnan'
>>> a+b*10
'codegnanpfspfspfspfspfspfspfspfspfspfs'
>>> (a+b)*10
'codegnanpfscodegnanpfscodegnanpfscodegnanpfscodegnanpfscodegnanpfscodegnanpfscodegnanpfscodegnanpfscodegnanpfs'
>>> '*'*20
'********************'
>>> 'python'*6
'pythonpythonpythonpythonpythonpython'
