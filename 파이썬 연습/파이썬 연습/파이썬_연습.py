a='My  naMe  is  Son  Chang  Ha:  my  pin  is  000125-3!!!!!!.'
b=" ".join(a.split())
c=b.replace(":",",")
d=c.replace("naMe","name") 
f=d.replace("my","My")
g=f.replace("3!!!!!!","3")
print(g)
