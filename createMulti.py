import random
import string

string.digits = '01234'
string.letters = 'ABCDEF'

n = len(string.digits * 2 + string.letters * 2)
print(n)
o = []

print(''.join(random.sample(string.digits * 2 + string.letters * 2, 22)))

for i in range(10):
    o.append(''.join(random.sample(string.digits * 2 + string.letters * 2, 22)))

print(o)
