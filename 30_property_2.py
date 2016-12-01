#! encoding=utf8
import datetime

## 有個會隨時間漏水的水桶，如果加水/倒水時，可以實驗如下。
class Bucket:
    def __init__(self,period):
        self.period_delta = datetime.timedelta(seconds=period)
        self.reset_time = datetime.datetime.now()
        self.quota = 0

    def __repr__(self):
        return 'Bucket(quota=%d)'% self.quota


def fill(bucket, amount):
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = datetime.datetime.now()
    bucket.quota += amount

def deduct(bucket,amount):
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False
    if bucket.quota - amount <0 :
        return False
    bucket.quota -= amount
    return True

bucket = Bucket(60)
fill(bucket, 100)
print bucket

if deduct(bucket,99):
    print 'Had 99 quota'
else:
    print 'Not enough for 99 quota'

deduct(bucket,99) # True
print bucket # Bucket(quota=1)
## 問題:沒有水桶內開始的配額

## 重新改寫(有點難!!!)

class Bucket(object):
    def __init__(self,period):
        self.period_delta = datetime.timedelta(seconds=period)
        self.reset_time = datetime.datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return 'Bucket(max_quota=%d, quota_consumed=%d)' %(self.max_quota,self.quota_consumed)

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self,amount):
        delta = self.max_quota - amount
        if amount ==0 :
            #配額因為新的週期被重設(reset)
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            # 配額因為新週期被填滿
            assert self.quota_consumed ==0
            self.max_quota = amount

        else:
            # 配額在週期中被消耗
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta

bucket = Bucket(60)
print 'Initial',bucket
fill(bucket,100)
print 'Filled',bucket

deduct(bucket,99)
print bucket
deduct(bucket,3)
print bucket
