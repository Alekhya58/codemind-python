n=int(input())
c=0
for i in range (n):
    a=int(input())
    i=list(map(int,input().split()))
    for j in range (1,a):
        if i[j-1]>i[j]:
            c+=1
    if c==0:
        print(c)
    else:
        ma=max(i)
        mi=min(i)
        print(ma-mi)