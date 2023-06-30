def isheap(arr,i,n):

    if i>int((n-2)/2):
        return True

    if arr[i]>arr[2*i+1] and arr[i]>arr[2*i+2] and isheap(arr,2*i+1,n) and isheap(arr,2*i+2,n):
        return True
    return False
arr = [90, 15, 10, 7, 12, 2, 7, 3]
print(isheap(arr,0,len(arr)-1))
