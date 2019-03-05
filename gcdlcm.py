def gcd(x,y):
    while y:
        x,y=y,x%y
    return x
print(gcd(98,56))    
lcm=98*56//14
print(lcm)