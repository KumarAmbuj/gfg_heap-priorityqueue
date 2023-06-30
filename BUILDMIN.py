def minheapify(a,i,n):
    min=i
    l=2*i+1
    r=2*i+2

    if l<n and a[l]<a[i]:
        min=l
    if r<n and a[r]<a[min]:
        min=r

    if min!=i:
        a[min],a[i]=a[i],a[min]
        minheapify(a,min,n)

def buildmin(a,n):

    for i in range((n-1)//2,-1,-1):
        minheapify(a,i,n)

a=[300,20,3,50,100,10,5,1]
buildmin(a,len(a))
print(a)