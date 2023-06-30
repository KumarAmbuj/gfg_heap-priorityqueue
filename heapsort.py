def heapify(a,n,i):
    largest=i
    l=2*i+1
    r=2*i+2

    if l<n and a[l]>a[largest]:
        largest=l
    if r<n and a[r]>a[largest]:
        largest=r

    if largest!=i:
        a[i],a[largest]=a[largest],a[i]
        heapify(a,n,largest)
def heapsort(a,n):

    for i in range((n-1)//2,-1,-1):
        heapify(a,n,i)

    for i in range(n-1,0,-1):
        a[i],a[0]=a[0],a[i]
        heapify(a,i,0)


a=[1,3,5,20,100,10,300,50]
heapsort(a,len(a))
print(a)