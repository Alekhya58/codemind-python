String =str(input())
count = 0
String = String.lower()
for i in String:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count+=1
if count == 0:
    print(0)
else:
    print(count)