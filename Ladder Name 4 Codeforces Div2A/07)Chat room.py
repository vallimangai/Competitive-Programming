s=input()
k="hello"
j=0
o=0
for i in s:
    o=o+1
    if(i==k[j]):
        j=j+1
    if(j==5):
        break
if(j==5):
    print("YES")
else:
    print("NO")
