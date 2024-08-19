s = []
sum = 0
fin = 0
i= 0
while True:
        a = int(input())
        s+= [a]
        sum = sum + s[i]
        fin = fin+ pow(s[i], 2)
        i+=1
        if sum == 0:
                break
print(fin)



