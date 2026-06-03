Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python programming'
len(s)
18
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
min(s)
' '
max(s)
'y'
ord('a')
97
ord('a')
97
ord('A')
65
ord('0')
48
ord('')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    ord('')
TypeError: ord() expected a character, but string of length 0 found
ord(' ')
32
chr(98)
'b'
chr(120)
'x'
chr(36)
'$'
char(50)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    char(50)
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(50)
'2'
chr(37)
'%'
chr(37)
'%'
s='python Programming'
s.upper
<built-in method upper of str object at 0x000001538FC4A5B0>
s.upper()
'PYTHON PROGRAMMING'
s.lower()
'python programming'
s.captilize
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.captilize
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
s.capitalize()
'Python programming'
s.title()
'Python Programming'
s.swapcase()
'PYTHON pROGRAMMING'
s
'python Programming'
s.center(28,'-')
'-----python Programming-----'
s.ljust(28,'-')
'python Programming----------'
s.rjust(28,'-')
'----------python Programming'
'123'.zfill(5)
'00123'
'123'.zfill(10)
'0000000123'
'123'.zfill(3)
'123'
'123'.zfill(2)
'123'
s.find('g')
10
s.rfind('o')
9
s.find('z')
-1
s.index('o')
4
s.rindex('z')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s.rindex('z')
ValueError: substring not found
s.count('a')
1
s.count('y')
1
s.count('n')
2
s.count('g')
2
s
'python Programming'
s,replace('python','123456')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s,replace('python','123456')
NameError: name 'replace' is not defined
s.replace('python','123456')
'123456 Programming'
s.maketrans('python'.'123456')
SyntaxError: invalid syntax
s.maketrans(s.maketrans('python'.'123456'))
SyntaxError: invalid syntax
s.maketrans(s.maketrans('python','123456'))
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.maketrans('python','123456')
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.translate(s.translate('python','123456'))
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s.translate(s.translate('python','123456'))
TypeError: str.translate() takes exactly one argument (2 given)
s.translate(s.maketrans('python','123456'))
'123456 Pr5grammi6g'
s='java,python,javascript,c,c++'
s.split(,)
SyntaxError: invalid syntax
s.split(',')
['java', 'python', 'javascript', 'c', 'c++']
s.split(',',2)
['java', 'python', 'javascript,c,c++']
s.rsplit(',',2)
['java,python,javascript', 'c', 'c++']
g='fgtre'
>>> g='nbvtre'
>>> g'ghjuytr'
SyntaxError: invalid syntax
>>> g='ghjuytr'
>>> jhytred
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    jhytred
NameError: name 'jhytred' is not defined
>>> g='fgtre'
... g='''nbvtre'''
... g='''ghjuytr
SyntaxError: multiple statements found while compiling a single statement
>>> 
... g='fgtre'
... g='''nbvtre'''
... g='''ghjuytr'''
SyntaxError: multiple statements found while compiling a single statement
>>> g='fgtre'
... g='''nbvtre'''
... g='''ghjuytr
SyntaxError: multiple statements found while compiling a single statement
>>> g='fgtre'
... 
... g='''nbvtre'''
... 
... g='''ghjuytr
SyntaxError: multiple statements found while compiling a single statement
>>> g= 'ghytrr'
... 
... g='''nskuywgg'''
... 
... g='''qjwgsgvs
SyntaxError: multiple statements found while compiling a single statement
>>> s
'java,python,javascript,c,c++'
>>> s.partition(',')
('java', ',', 'python,javascript,c,c++')
>>> s.rpartition(',')
('java,python,javascript,c', ',', 'c++')
>>> t="Hello ❤"
>>> t.encode()
b'Hello \xe2\x9d\xa4'
>>> 
>>> b'Hello \xe2\x9d\xa4'.decode()
'Hello ❤'
