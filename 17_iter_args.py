# 17 迭代引數時要小心迭代器耗盡

def normalize(numbers):
    total = sum(numbers)

    result = []
    for value in numbers:
        percent = float(value)/total
        result.append(percent)
    return result

visits = [15,35,80]
percentages = normalize(visits)
print percentages
# 1. 若要從檔案讀取資料
def read_visits(path = './17_samples.txt'):
    with open(path) as f :
        for line in f:
            yield int(line)
it = read_visits()
print normalize(it) # 為空值!!!! 讀不到!!!!


## __iter__ 類別容器的迭代器與iter內建迭代器隔離

class ReadVists(object):
    def __init__(self,data_path='./17_samples.txt'):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits = ReadVists()
percentages = normalize(visits)
print percentages


## 判斷是否為迭代器本身

def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):
        raise TypeError("Must supply a container") # 必須為容器
    total = sum(numbers)
    result = []

    for value in numbers:
        percent = float(value) / total
        result.append(percent)
    return result

visits = [15,35,80]
normalize_defensive(visits) # ok
visits = ReadVists()
normalize_defensive(visits) # ok
it = iter(visits)
normalize_defensive(it) # exception
