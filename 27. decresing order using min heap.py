def minheapify(arr,i,n):
    min =i
    l=2*i+1
    r=2*i+2

    if l<n and arr[i]>arr[l]:
        min=l
    if r<n and arr[r]<arr[min]:
        min=r

    if min!=i:
        arr[i],arr[min]=arr[min],arr[i]
        minheapify(arr,min,n)
def sorting(arr,n):

    for i in range((n-1)//2,-1,-1):
        minheapify(arr,i,n)

    for i in range(len(arr)-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        minheapify(arr,0,i)
arr = [4, 6, 3, 2, 9]
sorting(arr,len(arr))
print(arr)