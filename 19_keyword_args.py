# 19 keyword args 關鍵字引數

def remainder(number,division):
    return number % division

print remainder(20,7)
print remainder(20,division=7)
print remainder(number=20,division=7)
print remainder(division=7,20) # 錯! keyword arg要放在最後
print remainder(7,number=20) # 錯! 重複指定number

def flow_rate(weight_diff,time_diff,
                period=1, units_per_kg = 1):
    return ((float(weight_diff)/units_per_kg)/time_diff) * period

punds_per_hour = flow_rate(weight_diff=0.5,time_diff=3,period=3600,units_per_kg = 1)

print punds_per_hour

# 補充 **kwargs && *args

def table_things(**kwargs):
    for name,values in kwargs.items():
        print '{} = {}'.format(name,values)

table_things(apple='fruit',cabbage='vegetable') # apple=fruit, cabbage=vegetable

def print_three_things(a,b,c):
    print 'a={}, b={},c={}'.format(a,b,c)
my_list = ['car','bike','airplane']
print_three_things(*my_list) # a=car,b=bike,c=airplane
