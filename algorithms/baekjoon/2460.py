train = 0
max_train = 0
for _ in range(10):
    minus, plus = map(int, input().split())
    train = train - minus + plus
    if max_train < train:
        max_train = train
print(max_train)
