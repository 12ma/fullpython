tc=int(input())
for i in range(tc):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    while all(j!=0 for j in l):
            for k in l:
                    if k%2!=0:
                            k=k-1
                            count=count+1
                            print(count)


            if all(m%2==0 and m!=0 for m in l):
                    l=[o/2 for o in l]
                    count=count+1


        
    print(count)        
    
