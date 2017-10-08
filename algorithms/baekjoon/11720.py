from functools import reduce
a=input()
print(reduce(lambda x,y : int(x)+int(y), list(input())))
