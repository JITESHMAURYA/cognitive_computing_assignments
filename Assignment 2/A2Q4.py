a={34,56,78,90}
b={78,45,90,23}
x=a|b
y=a&b
z=a^b
print(x)
print(y)
print(z)
p=a.issubset(b)
q=b.issubset(a)
print(p)
print(q)
val=int(input("enter a number : "))
if(val in a):
    a.remove(val)
    print(a)
else:
    print(val,"is not in team A")