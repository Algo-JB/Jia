word = input()
word = word.upper()
dic = {}

for i in word:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
re_dic = dict(map(reversed, dic.items()))
max_n = max(dic.values())

if list(dic.values()).count(max_n) > 1:
    print('?')
else:
    print(re_dic[max(re_dic.keys())])

