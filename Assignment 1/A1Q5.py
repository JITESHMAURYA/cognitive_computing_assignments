x=[1,6,4,2,7]
print(max(x))
print(min(x))

y={1:"Jitesh",2:"the",3:"great"}
print(y[1])

x.sort()
print(x)
x.sort(reverse=True)
print(x)

z={4:"world",5:"leader"}
newdict=y|z
print(newdict)
y.update(z)
print(y)
