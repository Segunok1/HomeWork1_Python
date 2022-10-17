"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
"""
import re

with open('res.txt', 'w') as fail:
    res = 'NNNNNNNNWWvvvvvvvvvvvvvvvvFFFFFFFFFFFFFFFFFFFFLLLLLLLLLLLSSSSSSSSSSSSSSSSSSSyyyyyyyyyyyyyyhhhhhhhhhhhhhhhhhmmmmmmmmmmmmmmmmmmmoooooooooookkkkkkkkkkkttpppwwwwwwwwUUUUUUUUUUUUUpppppppppppppuuuuuuggggjjjjjjjjjjjjjjjttttttttttttttttttttuuuuuuuhhhhhhhhhhhhhhhhhbbbbbbbbbbbbbbbbbbbTTTTTTTTTTTTeeeeeeeeeeIIIIIIIIIIIIIIjjjjjjjjjjSSSSSSSSSSSSSSSSddddddddddddduuvvvvvvvvvvvvvQQQLLLLLLL' 
    fail.write(res)

with open('res.txt', 'r') as t:
    s = t.readline().strip()
with open('res1.txt', 'w') as s1:
   
    l = len(s)-1
    c = 1
    t = ''
    if len(s)==1:
        t = t +s+str(c)
    else:
        for i in range(0,l):
            if s[i]==s[i+1]:
                c +=1
            elif s[i]!=s[i+1]:
                t = t + s[i]+str(c)
                c = 1
        for j in range(l,l+1):
            if s[-1]==s[-2]:
                t = t +s[j]+str(c)
            elif s[-1]!=s[-2]:
                t = t +s[j]+str(c)
                c = 1
    print(t)
    s1.write(t)


with open('res1.txt') as t:
    s = t.readline().strip()
with open('res2.txt', 'w') as s1:
    for i in re.findall(r"\w\d+", s):
        res = "".join(i[0] * int(i[1:]))
        s1.write(res)