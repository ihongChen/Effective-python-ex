
class FrequencyList(list):
    def __init__(self,members):
        super(FrequencyList,self).__init__(members)

    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item,0)
            counts[item] += 1
        return counts

foo = FrequencyList(['a','b','a','c','b','a','d'])
print 'length is {}'.format(len(foo)) # length is 7
print 'frequency:',foo.frequency() # frequency: {a:3,b:2,c:1,'d':1}
foo.pop()
print 'After pop:',repr(foo)


##
bar = [1,2,3]
bar[0]
bar.__getitem__(0)
