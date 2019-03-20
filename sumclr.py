
l=list(map(int,input().split()))

for i in range(1,len(l)-1):
    
    s1,s2=0,0
    for j in range(0,i):
        s1=s1+l[j]
    

    for k in range(i+1,len(l)):
        s2=s2+l[k]
    

    if l[i]==s1==s2:
        print(l[i])
        break
    
