#https://codeforces.com/contest/136/problem/A
n=int(input())
k=input().split(" ")
for i in range(n):
    k[i]=int(k[i])
res=[]
for i in range(n):
    res.append(str(k.index(i+1)+1))
print(' '.join(res))
