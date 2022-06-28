a=b=c=d=0
for i in input():
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        a+=1
    elif((i>='a'and i<='z')or(i>='A'and i<='Z')):
        b+=1
    elif i.isdigit():
        c+=1
    elif(i==' '):
        d+=1
print('Vowels:',a)
print('Consonants:',b)
print('Digits:',c)
print('White spaces:',d)