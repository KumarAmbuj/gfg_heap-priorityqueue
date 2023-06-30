def minheapify(a,i,n):
    min=i

    l=2*i+1
    r=2*i+2

    if l<n and a[l]<a[r]:
        min=l
    if r<n and a[r]<a[min]:
        min=r

    if min!=i:
        a[i],a[min]=a[min],a[i]
        minheapify(a,min,n)
def findmin(a,n):
    min=a[0]

    a[0]=a[n-1]
    b=a.pop()

    n=n-1
    minheapify(a,0,n)
    return min

a=[1,20,3,50,100,10,5,300]
min=findmin(a,len(a))
print(min)
print(a)