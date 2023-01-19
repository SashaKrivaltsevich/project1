a=[1,2,3]
b=a
c=a
d=a.copy()
e=a.copy()
a=list(a)
b=list(b)
c=list(c)
e=d
print(a,id(a), d, id(b), c, id(c), d, id(d), e, id(e))