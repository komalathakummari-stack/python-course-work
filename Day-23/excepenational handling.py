'''
try:
    a = int(input("Enter the age: "))
except ValueError:
    print("Enter the age in a digit[0-9] format")
else:
    print("age:",a)
finally:
    print("Thankyou")
'''
'''
try:
    a=int(input("enter the age: "))
    #print(12/0)
    #print(b)
    #print(12+'14')
    d={1:1,2:2,3:3,4:4}
    #print(d[5])
    l=[1,2,3]
    #print(1[10])
    
except ValueError:
    print("Enter the Age in a digit[0-9] format")
except ZeroDivisionError:
    print("can't divide with zero")
except NameError:
    print("define the var")
except TypeError:
    print("type the same datetypes")
except KeyError:
    print("ker is not present")
except IndexError:
    print("index is out of range")
else:
    print("Age:",a)
finally:
    print("Thankyou")
    
'''
'''
try:
    a=int(input("enter the age: "))
    #print(12/0)
    #print(b)
    #print(12+'14')
    d={1:1,2:2,3:3,4:4}
    #print(d[5])
    l=[1,2,3]
    #print(1[10])

except (ValueError,ZeroDivisionError,NameError,TypeError,KeyError,IndexError)as e:
    print("Error Occured:",e)
else:
    print("No Error Occured")
finally:
    print("Thankyou")

'''
'''
try:
    a=int(input("Enter the age: "))
    #print(12/0)
    #print(b)
    #print(12+'14')
    d={1:1,2:2,3:3,4:4}
    #print(d[5])
    l=[1,2,3]
    #print(1[10])

except Exception as e:
    print("Error Occured:",e)
else:
    print("No Error Occured")
finally:
    print("Thankyou")
'''
'''
try:
    amount = int(input("enter amount to withdraw: "))
    if amount < 0:
        raise Exception("enter the amount greater than zero")

except Exception as e:
    print("enter occured:",e)
else:
    print("no error occured")
finally:
    print("thankyou")

'''



























    
