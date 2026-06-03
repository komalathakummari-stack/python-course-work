name=input()
rollno=int(input())
s1=int(input())
s2=int(input())
s3=int(input())

total=s1+s2+s3
avg=total/3

print(f'student name:{name}')
print(f'roll number:{rollno}')
print(f'total marks:{total}')
print(f'average marks:{avg}')




s=input()
print('total characters:',len(s))
print('first character:',s[0])
print('last character:',s[-1])
print('uppercase:',s.upper())
print('reversed string:',s[::-1])


a,b,c=list(map(int,input().split()))


print('sum:',a+b+c)
print('average:',(a+b+c)/3)
print('product:',a*b*c)
            
