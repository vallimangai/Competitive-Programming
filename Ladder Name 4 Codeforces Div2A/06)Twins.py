n=input()
n=int(n)
s=input().split(" ")
for i in range(n):
    s[i]=int(s[i])
s.sort(reverse=True)
ts=sum(s)
ms=0
k=0
for i in s:
    if(not(ms>ts)):
        ts=ts-i
        ms=ms+i
        k=k+1
    else:
        break
 
print(k)
