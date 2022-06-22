n=int(input())
a=[]
sum=0
for i in range (n):
    e=int(input())
    a.append(e)
t=int(input())
for i in range(n):
    if a[i]>t:
        sum+=2
    else:
        sum+=1
print(sum)