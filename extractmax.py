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

a=[100,50,20,1,3,10,5]
print(a)
def findmax(a,n):



    max=a[0]
    a[0]=a[n-1]
    b=a.pop()
    heapify(a,0,n-1)
    return max
a=[100,50,20,1,3,10,5]
print(findmax(a,len(a)))
print(a)
print(findmax(a,len(a)))
print(findmax(a,len(a)))
