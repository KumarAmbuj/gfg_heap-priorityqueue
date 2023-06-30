def heapify(a,i,n):
    largest=i
    l=2*i+1
    r=2*i+2

    if l<n and a[l]>a[i]:
        largest=l
    if r<n and a[r]>a[largest]:
        largest=r

    if largest!=i:
        a[i],a[largest]=a[largest],a[i]
        heapify(a,largest,n)
def heapsort(a,n):
    for i in range((n-1)//2,-1,-1):
        heapify(a,i,n)

    for i in range(n-1,0,-1):
        a[i],a[0]=a[0],a[i]
        heapify(a,0,i)
a = [1, 23, 12, 9, 30, 2, 50 ]
heapsort(a,len(a))
print(a)

for i in range(3):
    print(a[len(a)-1-i])
