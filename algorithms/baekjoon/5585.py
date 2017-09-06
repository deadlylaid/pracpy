coin_list=[500, 100, 50, 10, 5, 1]
a=1000-int(input())
count = 0
for i in coin_list: count+=a//i; a=a%i
print(count)
