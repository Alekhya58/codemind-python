n=int(input())
i=0
c=0
while True:
    a=2**i
    if(a>=n):
        res=a-n
        break
    i+=1
b=a//2
sol=n-b
if(sol>res):
    print(res)
else:
    print(sol)
    