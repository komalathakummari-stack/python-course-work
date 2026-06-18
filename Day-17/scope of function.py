'''
#local access

def display():
    n=10
    print("inside:",n)

display()
'''
'''
def display():
    n=10
    print("inside:",n)

display()
print("outside:",n)
'''
'''
#global access

n=10
def display():
    print("inside:",n)

display()
print("outside:",n)
'''
'''
def display():
    global n
    n=10
    print("inside:",n)

display()
print("outside:",n)
'''
'''
def display(n):
    #global n
    n+=10
    print("inside:",n)
    
n=10
display(n)
print("outside:",n)
'''
'''
def display():
    global n
    n+=10
    print("inside:",n)
    
n=10
display()
print("outside:",n)
'''
'''
def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("inner function:",n)
    inner()
    
    print("outer function:",n)

outer()
'''
'''
s='python'
print(len)
len=5
print(len(s))
'''
'''
#int

def update(n):
    n+=10
    print("inside:",n)
    
n=10
update(n)
print("outside:",n)
'''
'''
#float

def update(n):
    n+=10
    print("inside:",n)
    
n=10.3
update(n)
print("outside:",n)
'''
'''
#complex

def update(n):
    n+=10
    print("inside:",n)
    
n=12+4j
update(n)
print("outside:",n)
'''
'''
#str

def update(n):
    n=(5)
    print("inside:",n)
    
n=(2,3,4,5)
update(n)
print("outside:",n)
'''
'''
#list

def update(n):
    n=(4,5,6)
    print("inside:",n)
    
n=[1,2,3,4,5]
update(n)
print("outside:",n)
'''
'''
def update(n):
    n+=6
    print("inside:",n)
    
n=(1:2,1:3,1:4)
update(n)
print("outside:",n)

'''
'''
#recursive syntax

def func():
    if basecondition:
        return
    func()
'''
'''
#reverse and stright mixed recursive
def func(num):
    if num == 0:
        return
    print(num,end=' ')
    func(num-1)
    print(num,end=' ')

func (5)

'''
'''
#stright recursive

def func(num):
    if num == 0:
        return
    #print(num,end=' ')
    func(num-1)
    print(num,end=' ')

func (5)
'''
'''
#reverse recursive

def func(num):
    if num == 0:
        return
    print(num,end=' ')
    func(num-1)
    
func (5)

'''
'''
#addaction
def sumofdigits(n):
    if n == 0:
        return 0
    return n + sumofdigits(n-1)

print(sumofdigits(5))
'''
'''
#multiplication

def sumofdigits(n):
    if n == 0:
        return 1
    return n * sumofdigits(n-1)

print(sumofdigits(5))
'''
'''
#power calication

def power(base,pow):
    if pow==0:
        return 1
    return base * power(base,pow-1)

print(power(2,8))
print(power(3,7))
print(power(5,8))

'''
#reverse of string


def reverseofstr(s,ind):
    if ind == 0:
        return s[0]
    return s[ind]+reverseofstr(s,ind-1)

l="python programming"
print(reverseofstr(l,len(l)-1))












































