list_a = []
total = 0
for i in range(9):
    list_a.append(int(input()))
total = sum(list_a)

for i in range(8):
    for j in range(i+1, 9):
        if total - (list_a[i] + list_a[j]) == 100:
            number1 = list_a[i]
            number2 = list_a[j]
            list_a.remove(number1)
            list_a.remove(number2)
            break
        else:
            continue
    if len(list_a) < 9:
        break

list_a = sorted(list_a)
for i in list_a:
    print(i)
