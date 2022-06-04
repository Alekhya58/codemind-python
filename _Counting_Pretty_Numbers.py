n=int(input())
for j in range(n,0,-1):
    c=0
    a,b=map(int,input().split())
    for i in range(a,b+1):
        if(i==2 or i==3 or i==9):
            c+=1
        else:
            d=i%10
            if(d==2 or d==3 or d==9):
                c+=1
    print(c)