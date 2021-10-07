s=input().lower()
re=""
k=["a","o","y","e","u","i"]
for i in range(len(s)):
    if(s[i] not in k):
        if(len(re)==0):
            re=re+"."+s[i]+"."
        else:
            re=re+s[i]+"."
else:
    print(re[:-1])
