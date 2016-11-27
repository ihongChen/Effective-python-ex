# 15 知道closures 如何與變數範圍互動

## 1. sort用法
a = [5,2,3,1,4]
a.sort() # return none, a list will be sorted
print a # [1,2,3,4,5]

## 2. closures 觀念,
def sort_priority(values,group):
    def helper(x):
        if x in group:
            return (0,x)
        return (1,x)
    values.sort(key=helper)

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}


sort_priority(numbers,group)

print numbers

## scope traverse(範疇訪視)/變數生存空間 --python2
def sort_priority_py2(values,group):
    found = [False]
    def helper(x):
        if x in group:
            found[0] = True
            return (0,x)
        return (1,x)
    values.sort(key=helper)
    return found[0]

found = sort_priority_py2(numbers,group)
print 'Found:',found
print 'numbers:',numbers


## __call__寫法 (參考作法23)

class Sorter(object):
    def __init__(self,group):
        self.group = group
        self.found = False

    def __call__(self,x):
        if x in self.group:
            self.found = True
            return (0,x)
        return (1,x)


sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True
