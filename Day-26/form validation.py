'''
import re

pattern = r'[a-zA-Z]{2,15}( [a-zA-Z]{2,15})+$'
text = input("enter the text: ")
res = re.fullmatch(pattern,text)
print("valid format" if res else "invalid format")
'''
'''
import re

pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
text = input("enter the text: ")
res = re.fullmatch(pattern,text)
print("valid format" if res else "invalid format")
'''
'''
import re

pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
text = input("enter the text: ")
res = re.fullmatch(pattern,text)
print("valid format" if res else "invalid format")
'''
'''
import re

pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
text = input("enter the text: ")
res = re.fullmatch(pattern,text)
print("valid format" if res else "invalid format")
'''
import re

pattern = r'^[a-zA-Z0-9_]{5,15}$'
text = input("enter the text: ")
res = re.fullmatch(pattern,text)
print("valid format" if res else "invalid format")
