import math

star = ["  *   ", " * *  ", "***** "]

def MakeStar(shift):
    c = len(star)
    for i in range(c):
        star.append(star[i] + star[i])
        star[i] = ("   " * shift + star[i] + "   " * shift)

n = int(input())
space = int(math.log(int(n/3), 2))
for i in range(space):
    MakeStar(int(pow(2, i)))

for i in range(n):
    print(star[i])
