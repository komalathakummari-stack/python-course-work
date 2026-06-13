data={
    'bhargavi':{'status':True,'python':98,'mysql':83,'flask':79},
    'akshitha':{'status':True,'python':67,'mysql':56,'flask':85},
    'vaishnavi':{'status':True,'python':56,'mysql':45,'flask':59},
    'pravalika':{'status':False,'python':None,'mysql':None,'flask':None},
    'harshitha':{'status':True,'python':20,'mysql':36,'flask':40}
    }

name=input("enter the name: ")

if name in data:
    if data[name]['status']:
        total=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=total/3
        if avg>90:
            print(f"congtraslations{name},you got first in class!!!")
        elif avg>35:
            print(f"good {name},keep it up for the next time!!")
        elif avg>35:
            print(f"better {name},work hard next time!")
        else:
            print(f'{name},you have failed in the exam.bring your parents.')
    else:
        print(f"{name} didn't write the exam.bring your parents.")
else:
     print(f"{name}'s data is not found")
            
    
