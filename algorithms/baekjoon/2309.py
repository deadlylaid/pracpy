list_a = []
total= 0
for i in range(9):
    A = input()
    list_a.append(int(A))
    total+=int(A)

for j in list_a[0:]:
    for k in list_a[0:]:
        if j==k:
            continue
        elif total -(j+k)==100:
            list_a.remove(j)
            list_a.remove(k)

list_a.sort()
for l in list_a[0:]:
    print(l)
