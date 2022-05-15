n,a,b=map(int,input().split())
c=0
for i in range(n,a+1):
    if i%b==0:
        c+=1
print(c)
    