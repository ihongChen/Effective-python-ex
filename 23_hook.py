# 23 利用函數作為簡單的介面,而非使用類別

#

from collections import defaultdict

## 1.

def log_missing():
    print 'Key added'
    return 0

current = {'green':12,'red':3}
increments = [
    ('red',5),
    ('blue',17),
    ('orange',10)
    ]
result = defaultdict(log_missing,current)

print 'Before:',dict(result)
for key,amount in increments:
    result[key] += amount
print 'After:',dict(result)

## 2. stateful
class CountMissing:
    def __init__(self):
        self.added = 0
    def missing(self):
        self.added += 1
        return 0
counter = CountMissing()
result = defaultdict(counter.missing,current)
for key,amount in increments:
    result[key] += amount
assert counter.added==2


## 3. __call__
class BetterCountMissing(object):
    def __init__(self):
        self.added = 0
    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
result = defaultdict(counter,current) # 此等同於2.實現類別方法 counter.missing

for key,amount in increments:
    result[key] += amount
assert counter.added == 2
