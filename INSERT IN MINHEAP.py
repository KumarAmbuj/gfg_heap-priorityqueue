
def insert(a,key):
    a.append(key)
    n=len(a)
    i=n-1
    while i>0 and a[i]<a[i//2]:
        a[i],a[i//2]=a[i//2],a[i]
        i=i//2
a=[3,20,5,50,100,10,300]
insert(a,1)
print(a)
