a = int(input())
b = int(input())
c = int(input())
d = int(input())
b+=1
d+=1
print("\t", end="")
for z in range(c, d):
    print(z, end ="\t",)
print()
for i in range(a, b):
    print(i, end="\t")
    for j in range(c, d):
        print(i*j, end="\t")
    print()zhatie.py