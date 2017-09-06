c = [[1, 0], [0,1]]
def fibonacci(n):

    if n==0:
        return [1,0]
    elif n==1:
        return [0,1]
    elif len(c) > n:
        return c[n]
    elif len(c) <= n:
        a=fibonacci(n-1)[0]+fibonacci(n-2)[0]
        b=fibonacci(n-1)[1]+fibonacci(n-2)[1]
        c.append([a,b])
        return c[n]

for _ in range(int(input())):
        result = fibonacci(int(input()))
        print('{} {}'.format(result[0], result[1]))
