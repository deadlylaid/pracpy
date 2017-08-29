a = int(input())

list_b = { 1:[1], 2:[2,4,8,6], 3:[3,9,7,1], 4:[4,6], 5:[5], 6:[6], 7:[7,9,3,1], 8:[8,4,2,6], 9:[9,1], 0:[10] }
for _ in range(a):
    a, b = map(int, input().split())

    c = a%10
    if c == 1:
        print(1)
    else:
        d = b%len(list_b[c])
        if d == 0:
            e = list_b[c].pop()
            list_b[c].append(e)
            print(e)
        else:
            print(list_b[c][d-1])
