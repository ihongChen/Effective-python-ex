# 20

## default args只會被估值一次
import time
from datetime import datetime

def log(message,when=datetime.now()):
    print "{}:{}".format(when,message)

log('hi')
log('hi')

def log2(message,when=None):
    '''log a message with a timestamp

    Args:
        message: message to print
        when: datetime of when the message occurred.
            default to the present time
    '''
    when = datetime.now()
    print '{}:{}'.format(when,message)
log2('hi there')
time.sleep(5)
log2('hi there')

## 如果引數可變，使用預設為None是非常重要的
import json
def decode(data,default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['stuff'] = 5
print foo # foo : {'stuff':5}
bar =decode('also bad')
bar['meet'] =  2
print bar # bar : {'stuff':5 , 'meet':2}

assert foo is bar


def decode(data,default=None):
    '''Load json data from a string
    Args:
        data: JSON data to decode
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    '''
    if default is None :
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad data')
bar['meet'] = 1
print foo,bar # {'stuff':5} , {'meet':1}
