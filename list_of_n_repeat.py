n = int(input())
i, a = 0, 0
s = []
s_new = []
for i in range (n+1):
    s+=[i]*i
    i+=1
while a < n:
    s_new.append(s[a])
    a+=1
print(*s_new)