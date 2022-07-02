s=input()
m=(s.lower()).split()
c=0
for i in m:
    n=str(i)
    if n==n[::-1]:
        c+=1
print(c)