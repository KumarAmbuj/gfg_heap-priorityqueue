def heapify(a,i,n):
    largest=i

    l=2*i+1
    r=2*i+2

    if l<n and a[i]<a[l]:
        largest=l

    if r<n and a[r]>a[largest]:
        largest=r

    if largest!=i:
        a[i],a[largest]=a[largest],a[i]
        heapify(a,largest,n)
def buildheap(a,n):

    for i in range(((n-1)//2),-1,-1):
        heapify(a,i,n)

a=[100,50,20,1,3,10,5]
buildheap(a,len(a))
print(a)
