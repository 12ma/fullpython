tc=int(input())
for i in range(tc):
    size,total=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for j in range(len(l)):
        c=c+l[j]
        for k in range(1,len(l)):
            c=c+l[k]
            if c==total:
                print(j,k)
                break