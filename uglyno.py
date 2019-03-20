tc=int(input())
for i in range(tc):
    a=int(input())
    count=6
    
    b=(1,2,3,4,5,6)
    if a<=count:
        print(b[a-1])
    else:
        for j in range(7,10**4):
            for c,k in enumerate(range(2,j//2+1)):
                if j%k==0 and c<=2:
                    count=count+1
                    if count==a:
                        print(j)
                    
                    