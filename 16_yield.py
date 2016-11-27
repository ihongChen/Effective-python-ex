# 16 使用產生器而非回傳串列


def index_word_iter(text):
    if text:
        yield 0
    for index,letter in enumerate(text):
        if letter == ' ':
            yield index+1

def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

text = '''this is a test file,
thie is second line,
this is third line.
'''
list(index_word_iter(text))
