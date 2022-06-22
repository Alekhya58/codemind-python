n=int(input())
a=list(map(int,input().split()))
k=n//2
j=[]
for i in a[n:k-1:-1]:
    j.append(i)
for i in a[:k:]:
   j.append(i)
print(*j)