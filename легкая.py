f = open(r'C:\Users\USER\Desktop\prog\текст.txt', encoding = 'utf-8')
n = int(f.readline())
count = 0
for i in range(n):
    s = f.readline()
    if len(s) != 0 and 'Й' not in s and 'й' not in s:
        count += 1
print(count)









    



    
