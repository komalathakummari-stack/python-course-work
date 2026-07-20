'''
class flipkart:
    pass

bhargavi = flipkart()
komali = flipkart()
vaishnavi = flipkart()

'''
'''
class Flipkart:
    discount = 10
    products = ['laptop','phone','mouse','charger']

    @classmethod
    def showproducts(cls):
        print(cls.products)

    def login(self,username,password):
        self.username = username
        self.password = password
        print(f'welcome to the flipkart {self.username}')

    @staticmethod
    def banner():
        print("10% discount is going on flipkart, shop now!")


pranathi = Flipkart()
pranathi.login('pranathi','pranathi@123')
pranathi.banner()
pranathi.showproducts()

Flipkart.showproducts()
Flipkart.banner()
'''
'''
class instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.followers =[]
        print(f'welcome to the instagram, {self.username}')

vamshi = instagram('vamshi','vamshi@123')
'''
'''
class instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self.followers =[]

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword

vamshi = instagram('vamshi','vamshi@123')
        
print("before username:",vamshi.username)
vamshi.username = 'praneeth'
print("after username:",vamshi.username)

print("before password:",vamshi.getpassword())
vamshi.setpassword('praneeth@123')
print("after password:",vamshi.getpassword())
'''
'''
#encapsulation


class Instagram:
    def __init__(self):
        self._post = []

    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)


komali = Instagram()

print(komali.accesspost)
komali.accesspost = 'class and object'
print(komali.accesspost)

'''
'''
# single inheritance

class whatsappv1:
    def message(self):
        print("you can send messages to people")

class whatsappv2(whatsappv1):
    def calls(self):
        print("you can do video/audio calls")

komali = whatsappv1()
print("v1 - komali")
komali.message()


bhargavi = whatsappv2()
print("v2 - bhargavi")
bhargavi.message()
bhargavi.calls()

'''
'''
# multipule inheritance

class whatsappv1:
    def message(self):
        print("you can send messages to people")

class whatsappv2:
    def calls(self):
        print("you can do video/audio calls")

class whatsappv3:
    def media(self):
        print("you can share your phots/videos")

class whatsappv4(whatsappv1,whatsappv2,whatsappv3):
    def status(self):
        print("you can share status-[24 hours]")
        

bhargavi = whatsappv4()
print("v4 - bhargavi")
bhargavi.message()
bhargavi.calls()
bhargavi.media()
bhargavi.status()
'''
'''
#multi level lnheritance

class whatsappv1:
    def message(self):
        print("you can send messages to people")

class whatsappv2(whatsappv1):
    def calls(self):
        print("you can do video/audio calls")

class whatsappv3(whatsappv2):
    def media(self):
        print("you can share your phots/videos")

class whatsappv4(whatsappv3):
    def status(self):
        print("you can share status-[24 hours]")
        

bhargavi = whatsappv4()
print("v4 - bhargavi")
bhargavi.message()
bhargavi.calls()
bhargavi.media()
bhargavi.status()
'''
'''
#hirarical level lnheritance

class whatsappv1:
    def message(self):
        print("you can send messages to people")

class whatsappv2(whatsappv1):
    def emojis(self):
        print("you can send message with emojis to pepole")

class whatsappv3(whatsappv1):
    def stickers(self):
        print("you can send messages with stickers to people")


bhargavi = whatsappv3()
print("v3 - bhargavi")
bhargavi.message()
bhargavi.stickers()

bhargavi = whatsappv2()
print("v2 - bhargavi")
bhargavi.message()
bhargavi.emojis()

'''
'''
#hybrid level lnheritance

class whatsappv1:
    def message(self):
        print("you can send messages to people")

class whatsappv2(whatsappv1):
    def emojis(self):
        print("you can send message with emojis to pepole")

class whatsappv3(whatsappv1):
    def stickers(self):
        print("you can send messages with stickers to people")

class whatsappv4(whatsappv3,whatsappv2):
    def gif(self):
        print("you can send messages with gif to people")

bhargavi = whatsappv4()
print("v4 - bhargavi")
bhargavi.emojis()
bhargavi.stickers()
bhargavi.gif()
'''
'''
#single 

class wpv1:
    def status(self):
        print("you can upload images/videos")

class wpv2(wpv1):
    def status(self):
        super().status()
        print("you can react and reply")

class wpv3(wpv2):
    def status(self):
        super().status()
        print("you can like and reshare")


komali = wpv3()
komali.status()
'''
'''
#multipule

class wpv1:
    def status(self):
        print("you can upload images/videos")

class wpv2:
    def status(self):
        super().status()
        print("you can react and reply")

class wpv3(wpv2,wpv1):
    def status(self):
        wpv1.status(self)
        wpv2.status(self)
        print("you can like and reshare")


komali = wpv3()
komali.status()

'''

'''
#polimorphism

class Hotster:
    def __init__(self,name):
        self.name = name
        print(f'Hi {self.name}, welcome to the hotater')

    def login(self):
        print("you can login")
    def dashboard(self):
        print("you can see the dashboard items")
    def search(self):
        print("you can search")
    def languages(self):
        print("you select the language")
    def playcontrollers(self):
        print("you can pause and play the video")
    def ads(self):
        print("ads will run")
    def movies(self):
        print("you can limited access for movies")
    def sports(self):
        print("limited time you can watch sports")
    def quality(self):
        print("limited quality")

subbu = Hotster('subbu')
subbu.login()
subbu.dashboard()
subbu.search()
subbu.languages()
subbu.playcontrollers()
subbu.ads()
subbu.movies()
subbu.sports()
subbu.quality()
    
'''
'''
# method overrideing

class Hotster:
    def __init__(self,name):
        self.name = name
        print(f'Hi {self.name}, welcome to the hotater')

    def login(self):
        print("you can login")
    def dashboard(self):
        print("you can see the dashboard items")
    def search(self):
        print("you can search")
    def language(self):
        print("you select the language")
    def playcontrollers(self):
        print("you can pause and play the video")

        
class PremiumHotster(Hotster):
    def __init__(self,name):
        self.name = name
        print(f'Hi {self.name}, welcome to the Premium Hotater')


    def ads(self):
        print("ads won't run")
    def movies(self):
        print("you can unlimited access for movies")
    def sports(self):
        print("you can watch sports")
    def quality(self):
        print("high quality")

subbu = PremiumHotster('subbu')
subbu.login()
subbu.dashboard()
subbu.search()
subbu.language()
subbu.playcontrollers()
subbu.ads()
subbu.movies()
subbu.sports()
subbu.quality()

'''
'''
#operator overloading

class number:
    def __init__(self,n):
        self.n = n
    def __add__(self,other):
        return self.n + other.n
    def __sub__(self,other):
        return self.n - other.n
    def __mul__(self,other):
        return self.n * other.n
    def __truediv__(self,other):
        return self.n / other.n
    def __eq__(self,other):
        return self.n == other.n
    def __lt__(self,other):
        return self.n < other.n
    def __gt__(self,other):
        return self.n > other.n
    def __str__(self):
        return str(self.n)
    

n1 = number(10)
n2 = number(20)


print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)

print(n1==n2)
print(n1<n2)
print(n1>n2)
print(n1,n2)

'''
'''
#book details

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author},Price: ${self.price}")



book1 = Book("Clean Code", "Robert Martin", 450)
book1.display_info()

'''
'''
#employ salary

class Employee:
    def __init__(self, name,base_salary):
        self.name = name
        self.base_salary = base_salary


    def calculate_annual_salary(self):
        return self.base_salary * 12


emp = Employee("John", 35000)
print("Annual Salary:", emp.calculate_annual_salary())

'''
#abstraction

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def checkbalance(self):
        print("you can checkout your balance")
    def Viewhistory(self):
        print("you can checkout your transaction")   
    def userinfo(self):
        print("you can see your details")
    def transaction(self):
        print("you can transfer money through netbanking")
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class CurrentAccount(BankAccount):
    def deposit(self):
        print("you can deposit - CA ")
    def withdraw(self):
        print("You can withdraw - CA")
        
class SavingAccount(BankAccount):
    def deposit(self):
        print("you can deposit - SA ")
    def withdraw(self):
        print("You can withdraw - SA")
        
class ZeroBalanceAccount(BankAccount):
    def deposit(self):
        print("you can deposit - ZBA ")
    def withdraw(self):
        print("You can withdraw - ZBA")
        
class FixedDeposit(BankAccount):
    def deposit(self):
        print("you can deposit - FD ")
    def withdraw(self):
        print("You can withdraw - FD")
        
class SalaryAccount(BankAccount):
    def deposit(self):
        print("you can deposit - SSA ")
    def withdraw(self):
        print("You can withdraw - SSA")

komali=ZeroBalanceAccount()
komali.deposit()
komali.withdraw()
komali.checkbalance()
komali.Viewhistory()
komali.userinfo()
komali.transaction()

bhargavi=FixedDeposit()
bhargavi.deposit()
bhargavi.withdraw()
bhargavi.checkbalance()
bhargavi.Viewhistory()
bhargavi.userinfo()
bhargavi.transaction()

komali=SalaryAccount()
komali.deposit()
komali.withdraw()
komali.checkbalance()
komali.Viewhistory()
komali.userinfo()
komali.transaction()

















































































































