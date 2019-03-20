tc=int(input())
for i in range(tc):
    n=int(input())
    if n==0:
        print("NO")
    else:
        for i in range(0,n):
            d=2**i
            if d==n:
                print("YES")
                break
            elif d>n:
                print("NO")
                break
            else:
                pass
            
            
    
        
        
                  