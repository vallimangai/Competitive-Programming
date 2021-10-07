s=input()
k=[]
for i in s:
    if(i!='+'):
        k.append(int(i))
else:
    k.sort()
    r=""
    for i in k:
        r=r+str(i)+'+'
    else:
        print(r[:-1])
