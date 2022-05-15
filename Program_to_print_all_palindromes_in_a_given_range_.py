a=int(input())
b=int(input())
for n in range(a,b+1):
    s=0
    temp=n
    while(temp>0):
        r=temp%10
        s=s*10+r
        temp=temp//10
    if n==s:
        print("%d "%n,end='')