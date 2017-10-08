a=['c=','c-','dz=','d-','lj','nj','s=','z=']
text=input()
result=len(text)
for i in a:
    result-=text.count(i)
print(result)
