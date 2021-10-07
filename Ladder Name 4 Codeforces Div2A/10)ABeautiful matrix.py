n=5
i=0
s=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
while(i<n):
    k=input().split(" ")
    for j in range(0,n):
        s[i][j]=int(k[j])
    i=i+1
for i in range(0,n):
    for j in range(0,n):
        if(s[i][j]==1):
            print(abs(2-i)+abs(2-j))
