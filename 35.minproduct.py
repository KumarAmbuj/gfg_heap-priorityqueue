def minheapify(arr,i,n):
    min=i
    l=2*i+1
    r=2*i+2

    if l<n and arr[i]> arr[l]:
        min=l
    if r<n and arr[r]<arr[min]:
        min=r
    if min!=i:
        arr[min],arr[i]=arr[i],arr[min]
        minheapify(arr,min,n)
def buildminheap(arr):
    n=len(arr)-1
    for i in range((n-1)//2,-1,-1):
        minheapify(arr,i,n)

def findminproduct(arr,k):

    n=len(arr)-1
    buildminheap(arr)
    prod=1
    for i in range(k):
        min=arr[0]
        arr[0],arr[n]=arr[n],arr[0]
        n=n-1
        minheapify(arr,0,n)
        prod=prod*min
    print(prod)
arr = [198, 76, 544, 123, 154, 675]
findminproduct(arr,2)