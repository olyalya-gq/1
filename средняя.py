s = open(r"C:\Users\USER\Desktop\prog\GOAL.txt").readline()
count = 0
maxicount = 0
maxi = ''
s = s.replace('G', ' ').replace('L', ' ')
s = s.split()
for i in range(len(s)):
    if 50 <= len(s[i]) <= 200:
        count += 1
        if len(s[i]) > maxicount:
            maxicount = len(s[i])
            maxi = s[i]
print(count)
print(len("G" + maxi + "L"))