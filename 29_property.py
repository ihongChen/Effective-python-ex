## property
#####################################################################
# 0. 初探property用法
class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(50)
s.get_score() # 50
###################################################################
# 以上寫法有點囉唆
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be integer')
        if value<0 or value >100:
            raise ValueError('score must between 0 to 100.')
        self._score = value

s = Student()
s.score = 50
s.score

# 1.
class Resistor(object):
    def __init__(self,ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0
r1 = Resistor(50e3)
r1.ohms = 10e3
print r1.ohms

r1.ohms += 5e3

# 2. @property
# 設定r2.voltage時會同時更動r2.current
class VoltageResistance(Resistor):
    def __init__(self,ohms):
        super(VoltageResistance,self).__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self,voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


r2 = VoltageResistance(1e3)
print 'Before: %5r amps ' %r2.current
r2.voltage = 10
print 'After: %5r amps' %r2.current


## 3. type checking
class BoundedResistance(Resistor):
    def __init__(self,ohms):
        super(BoundedResistance,self).__init__(ohms)

    @property
    def ohms(self):
        return self._ohms
    @ohms.setter
    def ohms(self,ohms):
        if ohms <= 0:
            raise ValueError('%f ohms must be >0 '%ohms)
        self._ohms = ohms

r3 = BoundedResistance(1e3)
r3.ohms
r3.ohms = -10  # ValueError raise, 因為
               # BoundedResistance.__init__ 呼叫 Resistor.__init__而會作 self.ohms=-5
