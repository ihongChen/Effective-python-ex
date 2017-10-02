# 18 以可變位置引數減少視覺雜訊 star args (*args)

def log(message,*values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('{}:{}'.format(message,values_str))

log('hi there') # hi there
log('My numbers are',1,2,3,4,5) # My numbers are : 1,2,3,4,5

favorites = [7,3,9]
log('My favorites',*favorites) # My favorites:7,3,9

## issue: *args 被傳到函數前會先變成tuples耗用記憶體
def my_generator(x):
    for i in range(x):
        yield i

def my_func(*args):
    print args

it = my_generator(x=20)
my_func(*it) #(0,1,2,.....19) ## 若*args用在iterator上有可能耗用太多記憶體當掉!!
