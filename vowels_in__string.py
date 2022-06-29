n=input()
x=list(n)
c=0
b=[]
for i in x:
    if i in 'AEIOUaeiou' and i not in b:
        c+=1
        b+=[i]
        print(i,end=' ')
if(c==0):
    print('-1')