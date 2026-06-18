'''
def function_name(avg):
    #stmts
    return

function_name(para)

function_name(para)
'''
'''
def wish(name):
    print(f'welcome to the python course {name}!')

wish('subbu')
wish('bhargavi')
wish('vaishnavi')
wish('pranathi')
'''
'''
def iseven(num):
    if num%2==0:
        return f"{num} - even number"
    else:
        return f"{num} - not even number"

print(iseven(12))
print(iseven(13))
'''
'''
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

num=int(input("enter the number: "))
print("factorial:",factorial(num))
'''
'''
def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num} - not prime number"
    return f"{num} - prime number"

num = int(input("enter the number: "))
print(isprime(num))
'''
'''
def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("password:",pwd)


display('komali','komali@gmail','komali@123')
display('komali@gmail','komali','komali@123')
display('komali','komali@123','komali@gmail')
'''
'''
def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("password:",pwd)


display(name='komali',email='komali@gmail',pwd='komali@123')
display(email='komali@gmail',name='komali',pwd='komali@123')
display(name='komali',pwd='komali@123',email='komali@gmail')
'''
'''
def display(name,email,pwd=''):
    print("name:",name)
    print("email:",email)
    print("password:",pwd)


display('komali','komali@gmail','komali@123')
display('komali@gmail','komali@123')
display('komali','komali@gmail')
'''
'''
def display(*names):
    print("names:",names)
    

display('komali','bhargavi','vaishnavi''pranathi')
display('bhargavi','vaishnavi','pranathi')
display('bhargavi','pranathi')
'''
'''
def display(**names):
    print("names:",names)
    

display(k1='komali',k2='bhargavi',k3='vaishnavi',k4='pranathi')
display(k1='bhargavi',k2='vaishnavi',k3='pranathi')
display(k1='bhargavi',k2='pranathi')
'''





























