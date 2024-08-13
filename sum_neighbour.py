s = [int(i) for i in input().split()]
s_new=[]

if len(s) == 1:
    print(s[0])
else:
    for i in range(len(s)):
        if i == 0:
            s_new.append(s[-1]+s[1])
        elif 0 < i < (len(s)-1):
            s_new.append(s[i-1]+s[i+1])
        elif i == (len(s)-1):
            s_new.append(s[i-1] + s[0])
    print(*s_new)
