a = int(input())

result = []
list_a = []

for _ in range(int(a)):

    b,c = input().split()

    list_a = [ int(x) for x in input().split() ]

    index = int(c)
    counter = 1
    while len(list_a) != 0:
        if index == 0:
            if list_a[index] >= max(list_a):
                print(counter)
                counter += 1
                break
            else:
                d = list_a.pop(0)
                list_a.append(d)
                index = len(list_a)-1
        else:
            if list_a[0] >= max(list_a):
                list_a.pop(0)
                counter += 1
            else:
                d = list_a.pop(0)
                list_a.append(d)
            index -= 1
