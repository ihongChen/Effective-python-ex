# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:12:16 2017

@author: 116952
"""
#%%
#==============================================================================
# 01 python version 
#==============================================================================

import sys 
print(sys.version_info)
print(sys.version)

# %%
#==============================================================================
#  02 pep8 
#==============================================================================
# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
# More indentation included to distinguish this from the rest.

def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
    
# Hanging indents should add a level.

foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# No extra indentation.
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.

if (this_is_one_thing and
    that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.

if (this_is_one_thing
        and that_is_another_thing):
    do_something()
    
    
# %%

#==============================================================================
# 03. bytes,str,unicode 
#==============================================================================

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf8")
    else:
        value = bytes_or_str
    return value # instance of str

print('你好'.encode('utf8'))
print(to_str('你好'.encode('utf8')))


def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf8")
    else:
        value = bytes_or_str
    return value # instance of bytes

print('你好')    
print(to_bytes('你好'))    
    

### bytes 永遠不等於 str ## 
' ' == b' '
'1' == b'1'

### 寫入資料會有encoding 問題, python3中open預設使用 encoding = 'utf8'
import os
random_bytes = os.urandom(10)
with open('./tmp/random.bin', 'wb') as f:
    f.write(os.urandom(10))
    
    
# from base64 import b64encode
# token = b64encode(random_bytes).decode('utf-8')

# %%
#==============================================================================
# 04. 輔助函數
#==============================================================================

from urllib.parse import parse_qs
values = parse_qs('red=5&blue=0&green=',
                  keep_blank_values=True)

print(values)

red = values.get('red',[''])[0]
red = int(values.get('red',[''])[0] or 0) ##愈來愈難讀

def get_first_int(values, key, default = 0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])        
    else:
        found = default
    return found 
        
# %%
#==============================================================================
# 07. 串列概括式, not use map,filter
#==============================================================================
a = [1,2,3,4,5,6,7,8,9,10]
squares = [x**2 for x in a]
print(squares)

squares =map(lambda x: x**2, a)
even_squares = [x**2 for x in a if x%2 ==0]

# %%
# =============================================================================
# 09. Yield 
# =============================================================================

it = (len(x) for x in open('./16_text.txt'))
print(it)
next(it)
[e for e in it]
#%% 
# =============================================================================
# 11. zip
# =============================================================================

names = ['Cecilia','Lise','Marie']
letters = [len(n) for n in names]
max_letters = 0
for name,count in zip(names,letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
print("longest name :{},\tmax_length:{}".format(
        longest_name,max_letters))

# =============================================================================
# 13. try, except, else, finally
# =============================================================================
try:
    pass
except ValueError:
    pass
else:
    pass
finally:
    pass

