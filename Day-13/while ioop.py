'''
pin=1234
for i in range(5):
    e_pin=int(input("enter the pin: "))
    if e_pin==pin:
        print("unlock the phone")
        break
    else:
        print("incorrect pin")
else:
        print("try again, after 60seconds")

l=[2,3,5,6,8,10,34,12]
search=int(input("enter the element: "))

for i in range(len(l)):
    if l[i]==search:
        print(f'{search} is found at index-{i}')
        break
else:
    print(f'{search} is not found')

password=int(input("enter the password: "))
if len(password)>=8:
    s=set()
    for i in password:
        if i.isupper():
           s.add('u')
        elif i.islower():
           s.add('l')
        elif i.isdigit():
           s.add('d')
        else:
           s.add('s')
    if len(s)==4:
        print("strong password")
    else:
        print("weak password")
else:
    print("weak password")

Status = None
assert Status != None, "You need to update the Status"
print(Status)

name='abc'
batch=55
age=21
assert(name!=None and batch!=None and age!=None),"You need to update the data"
print(name,batch,age)

i=2
while i<11:
    print(i)
    i+=1

i=2
while i<21:
    print(i)
    i+=2

i=10
while i>0:
    print(i)
    i-=1

i=5
while i<51:
    print(i)
    i+=5

l=[1,2,3,4,5,6,7,8,9]
i=0
while i<len(l):
    print(l[i])
    i+=1

l='python programming'
i=0
while i<len(l):
    print(l[i])
    i+=1

l='adapu vijaya bhragavi'
i=0
while i<len(l):
    print(l[i])
    i+=1
    
l=(1,3,5,6,57,87,9)
i=0
while i<len(l):
    print(l[i])
    i+=1

l=[1,2,0,0,0,0,6,6,5,7,3,2,2,2,2,2,6,0,0,0,0,0,12,34,6,8,0,0,0,0,32]
while 0 in l:
    l.remove(0)
print(l)

m=20
while m>1:
    status=input("[W]in or [C]noinue: ").upper()
    if status == 'W':
        print("you won the game")
        break
    m-=1
    print(f'{m}m are left')
else:
    print("game over")
'''
bullets=10
while m>1:
    status=input("[B]in or [C]noinue: ").upper()
    if status == 'B:
        print("you won the game")
        break
    m-=1
    print(f'{B}B are left')
else:
    print("game over")
