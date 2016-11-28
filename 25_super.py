# 使用super初始化父類別, 多重繼承如不使用會出現異常現象

class MyBaseClass(object):
    def __init__(self,value):
        self.value = value

class TimesFiveCorrect(MyBaseClass):
    def __init__(self,value):
        super(TimesFiveCorrect,self).__init__(value) # py3中: super().__init__(value)
        self.value *= 5

class PlusTwoCorrect(MyBaseClass):
    def __init__(self,value):
        super(PlusTwoCorrect,self).__init__(value)
        self.value += 2

class GoodWay(TimesFiveCorrect,PlusTwoCorrect):
    def __init__(self,value):
        super(GoodWay,self).__init__(value)

# temp = TimesFiveCorrect(3)
# print temp.value
# temp2 = PlusTwoCorrect(30)
# print temp2.value
foo = GoodWay(5)

print 'should be 5*(5+2) = 35 and is ',foo.value

# 觀察繼承順序
print GoodWay.mro() # Goodway -> TimesFiveCoorect -> PlusTwoCorrect -> MyBaseClass
