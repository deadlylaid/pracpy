a = int(input())
b = list(map(int, input().split()))
c = max(b)
result = 0
for i in b:
    result += i/c * 100
k = round(result/a, 4)
print("%.2f"%(k))
