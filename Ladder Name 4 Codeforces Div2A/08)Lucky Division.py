n=int(input())
k=[4,7,47,74,44,77,444,447,474,477,777,774,747,7444]
f=0
for i in k:
    if(n%i==0):
        f=1
        print("YES")
        break;
if(f==0):
    print("NO")
