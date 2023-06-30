def heapify(a,i,n):
    largest=i
    l=2*i+1
    r=2*i+2

    if l<n and a[i]<a[l]:
        largest=i
    if r<n and a[r]>a[largest]:
        largest=r

    if largest!=i:

        a[i],a[largest]=a[largest],a[i]

        heapify(a,largest,n)
    
def insert(a,key):

    a.append(key)
    n=len(a)

    i=n-1

    while i>0 and a[i]>a[i//2]:
        a[i],a[i//2]=a[i//2],a[i]
        i=i//2
a=[100,50,20,1,3,10,5]
insert(a,300)
print(a)

