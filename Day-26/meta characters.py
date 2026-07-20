'''
import re

pattern = r'h.t\b'
text = 'hot hit het hrt hat hate hood heart hjt h$t'

res = re.findall(pattern,text)
print(res)
'''
'''
import re

pattern = r'^h'
text = 'hot hit het hrt hat hate hood heart hjt h$t'

res = re.findall(pattern,text)
print(res)
'''
'''
import re

pattern = r't$'
text = 'hot hit het hrt hat hate hood heart hjt h$t'

res = re.findall(pattern,text)
print(res)
'''
'''
import re

pattern = r'to?\b'
text = 'too to t toooooooo toooooooooooo'

res = re.findall(pattern,text)
print(res)
'''
'''
import re

pattern = r'[a-z]{4,5}'
text = 'qerr iuytr sdfghj zxcvb kjhguy sdfgh cvbnm wert'

res = re.findall(pattern,text)
print(res)
'''

import re

pattern = r'(python)'
text = 'pyth pythn python puthon pythan'

res = re.findall(pattern,text)
print(res)



































