d=0
for _ in range(5):
    a=int(input())
    if a<40:
        a=40
    d+=a
print(int(d/5))
