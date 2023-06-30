def partition(arr,p,r):
    x=arr[r]
    i=p-1

    for j in range(p,r):
        if arr[j]<=x:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[r]=arr[r],arr[i+1]
    return i+1

def quicksort(arr,p,r):
    if p<r:
        q=partition(arr,p,r)
        quicksort(arr,p,q-1)
        quicksort(arr,q+1,r)



def fun(arr,m):

    quicksort(arr,0,len(arr)-1)
    print(arr)
    j=len(arr)-1
    min=0
    max=0
    for i in range(m):
        max=max+arr[j]
        j=j-1

        min=min+arr[i]

    diff=max-min
    return diff
arr = [5,3,2,4,1]
print(fun(arr,4))

