import random
l=[]
for i in range(0,100):
    num=random.randint(100,900)
    l.append(num)

evenlist=[]
oddlist=[]
primelist=[]
for j in range(0,100):
    if(l[j]%2==0):
        evenlist.append(l[j])
    else:
        oddlist.append(l[j])
    flag = True
    for k in range(2,l[j]):
        if(l[j]%k==0):
            flag=False
            break
    if(flag==True):
        primelist.append(l[j])

print(evenlist)
print(oddlist)
print(primelist)

