tup=(45,89.5,76,45.4,89,92,58,45)
x=max(tup)
y=tup.index(x)
print(x)
print(y)

a=min(tup)
b=tup.count(a)
print(a)
print(b)

check=76 in tup
if(check==True):
    print(check)
    print(tup.index(76))
else:
    print("76 is not present")


revtup=tup[::-1]
revtup=list(revtup)
print(revtup)