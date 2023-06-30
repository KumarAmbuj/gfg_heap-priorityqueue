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
def mintomax(arr):
    n=len(arr)-1

    for i in range((n-1)//2,-1,-1):
        heapify(arr,i,n)
    print(arr)
arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
mintomax(arr)