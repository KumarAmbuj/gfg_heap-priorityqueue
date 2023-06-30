def heapify(arr,i,n):
    largest=i
    l=2*i+1
    r=2*i+2

    if l<n and arr[l]>arr[i]:
        largest=l
    if r<n and arr[r]>arr[largest]:
        largest=r

    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,largest,n)
def merge(arr1,arr2):
    n=len(arr1)
    m=len(arr2)

    merged=[0]*(m+n)

    for i in range(n):
        merged[i]=arr1[i]
    for i in range(m):
        merged[n+i]=arr2[i]

    n=len(merged)-1
    for i in range((n-1)//2,-1,-1):
        heapify(merged,i,n)
    print(merged)
a = [10, 5, 6, 2]
b = [12, 7, 9]
merge(a,b)