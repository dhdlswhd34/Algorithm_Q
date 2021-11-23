from os import replace
import re
f = open('C:/Users/user/Documents/Algorithm_Q/DP_P/name.txt', 'r', encoding='utf-8')

text = f.read()

text = text.split(')')

print(text)

for value in text:
    value = value.replace('\t', '_')
    value = value.replace('\n', '')
    value = value.replace('좌장:', '_')
    print(value+')')
f.close()