Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3='float'
  
SyntaxError: '[' was never closed
d[12.3]='float'
  
d
  
{1: 'int', 12.3: 'float'}
d['demo']='str'
  
d
  
{1: 'int', 12.3: 'float', 'demo': 'str'}
d[2+3j]='complex'
  
d
  
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex'}
d91,2,3,4)='tuple'
SyntaxError: unmatched ')'
d(1,2,3,4)='tuple'
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
d[(1,2,3,4)]='tuple'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex', (1, 2, 3, 4): 'tuple'}
d[false]='bool'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d[false]='bool'
NameError: name 'false' is not defined. Did you mean: 'False'?
d[False]='bool'
d
{1: 'int', 12.3: 'float', 'demo': 'str', (2+3j): 'complex', (1, 2, 3, 4): 'tuple', False: 'bool'}
d={}
d
{}
d[1]=1
d
{1: 1}
d[23]=23.4
d
{1: 1, 23: 23.4}
d[23]=23.4
d[3]='werty'
d[4]=4+7j
d[5]=[1,2,3]
d[6]=(1,2,3)
d[7]={1,3}
d[8]={1:1,2:2}
d[9]=False
d
{1: 1, 23: 23.4, 3: 'werty', 4: (4+7j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 3}, 8: {1: 1, 2: 2}, 9: False}
d=
SyntaxError: invalid syntax
d={}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1:2,2:4,3:6,5:10,6:12}
d[4]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    d[4]
KeyError: 4
d[3]
6
d[5]
10
d[6]
12
d[1]
2
d={'komalatha':89,'bhargavi':76,'subbu':90,'nagendra':76,'dinesh':50}
d['bhargavi']
76
d['subbu']
90
d['komalatha']
89
d['sahith']
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    d['sahith']
KeyError: 'sahith'
d={'komalatha':89,'bhargavi':76,'subbu':90,'nagendra':76,'dinesh':50}
d
{'komalatha': 89, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 50}
d.get('sahith')
d.get('dinesh')
50
d.get('akhil','user not found')
'user not found'
d.get('subbu','user not found')
90
'dinesh' in d
True
'sahith not in d
SyntaxError: unterminated string literal (detected at line 1)
'sahith' not in d
True
d.keys()
dict_keys(['komalatha', 'bhargavi', 'subbu', 'nagendra', 'dinesh'])
d.values()
dict_values([89, 76, 90, 76, 50])
d.items()
dict_items([('komalatha', 89), ('bhargavi', 76), ('subbu', 90), ('nagendra', 76), ('dinesh', 50)])
sorted(d)
['bhargavi', 'dinesh', 'komalatha', 'nagendra', 'subbu']
max(d)
'subbu'
min(d)
'bhargavi'
len(d)
5
d
{'komalatha': 89, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 50}
d['dinesh]
  
SyntaxError: unterminated string literal (detected at line 1)
d['dinesh']
  
50
d['dinesh']=100
  
d
  
{'komalatha': 89, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100}
d['komalatha']=60
  
d
  
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100}
d['rishi']=87
  
d
  
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87}
d.update({'praneeth':90'manideep:80)}
          
SyntaxError: unterminated string literal (detected at line 1)
d.update({'praneeth':90'manideep':80)}
          
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
d.update({'praneeth':90'manideep':80})
          
SyntaxError: invalid syntax. Perhaps you forgot a comma?
d.update({'praneeth':90,'manideep':80})
          
d
          
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87, 'praneeth': 90, 'manideep': 80}
d.popitem()
          
('manideep', 80)
d
          
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87, 'praneeth': 90}
d.popitem()
          
('praneeth', 90)
d.popitem()
          
('rishi', 87)
d
          
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100}
>>> d.pop('subbu')
...           
90
>>> d
...           
{'komalatha': 60, 'bhargavi': 76, 'nagendra': 76, 'dinesh': 100}
>>> del d['komalatha']
...           
>>> d
...           
{'bhargavi': 76, 'nagendra': 76, 'dinesh': 100}
>>> d.clear()
...           
>>> d
...           
{}
>>> d={'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87, 'praneeth': 90, 'manideep': 80}
... d
...           
SyntaxError: multiple statements found while compiling a single statement
>>> d
...           
{}
>>> d
...           
... {'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87, 'praneeth': 90, 'manideep': 80}
... 
SyntaxError: multiple statements found while compiling a single statement
>>> d={'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87, 'praneeth': 90}
...           
>>> d
...           
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87, 'praneeth': 90}
>>> d.setdefault('rishi',0)
...           
87
>>> d
...           
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87, 'praneeth': 90}
>>> d.setdefault('sathish',0)
...           
0
>>> d
...           
{'komalatha': 60, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76, 'dinesh': 100, 'rishi': 87, 'praneeth': 90, 'sathish': 0}
