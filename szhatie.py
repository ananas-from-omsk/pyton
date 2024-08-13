dna = input()
l = len(dna)
i = 0
cnt = 1
j = 1
dna_new = str()

if l == 1:
    c = str(cnt)
    dna_new = dna_new + dna[i] + c
    print(dna_new)
else:
    while (j != l):
        if dna[i] == dna[j]:
            cnt +=1
            if j == l - 1:
                c = str(cnt)
                dna_new=dna_new+dna[j]+c
        else:
            c = str(cnt)
            dna_new=dna_new+dna[i]+c
            cnt = 1
            if j == l - 1:
                c = str(cnt)
                dna_new=dna_new+dna[j]+c
        i+=1
        j+=1
    print(dna_new)