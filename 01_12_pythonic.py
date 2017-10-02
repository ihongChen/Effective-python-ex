# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 10:12:16 2017

@author: 116952
"""
#%%
#==============================================================================
# ## python version 
#==============================================================================

import sys 
print(sys.version_info)
print(sys.version)

# %%
#==============================================================================
#  pep8 
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
# 3. bytes,str,unicode 
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
# 輔助函數
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
# 
#==============================================================================



