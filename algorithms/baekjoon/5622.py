alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

list_a=list(input())
count=0
for i in list_a:
    if i in alphabet[0:3]:
        count+=3
    elif i in alphabet[3:6]:
        count+=4
    elif i in alphabet[6:9]:
        count+=5
    elif i in alphabet[9:12]:
        count+=6
    elif i in alphabet[12:15]:
        count+=7
    elif i in alphabet[15:19]:
        count+=8
    elif i in alphabet[19:22]:
        count+=9
    else:
        count+=10
print(count)
