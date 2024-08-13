s = [int(i) for i in input().split()]
s_new = []
s.sort()
cnt = 1
i = 0
if len(s) != 1:
    for i in range(len(s)):
        if 0 <= i < (len(s) - 1):
            if (s[i] == s[i+1] and i != (len(s)-1)):
                cnt+=1
            else:
                if cnt > 1:
                    s_new.append(s[i])
                cnt = 1
        elif (i == (len(s) - 1) and s[i] == s[i-1]):
            s_new.append(s[i])
        i+=1
    print(*s_new)





