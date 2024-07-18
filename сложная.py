f = open(r'C:\Users\USER\Desktop\prog\слова.txt', encoding = 'utf-8')
n = 1000
alf = 'йцукенгшщзхъфывапролджэячсмитьбюё'
dic = {x:0 for x in alf}

for i in range(n):
    s = f.readline()
    for j in range(len(s)):
        if s[j] in alf:
            dic[s[j]] += 1
print(dic)
val = sorted(dic.values())
k = 1
print(val)
for i in range(5):
    maxibukva = max(dic, key = dic.get)
    maxiznach = max(val)
    print(f'{k} - "{maxibukva}" - {max(val)}')
    k += 1
    dic.pop(maxibukva)
    val.remove(maxiznach)

