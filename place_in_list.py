lst = [int(i) for i in input().split()]
x = int(input())
place = []
for i in range(len(lst)):
    if x == lst[i]:
        place.append(i)
    i+=1
if len(place) == 0:
    print("Отсутствует")
else:
    print (*place)