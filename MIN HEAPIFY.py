def minheapify(a,i,n):

    min=i
    l=2*i+1
    r=2*i+2

    if l<n and a[l]<a[i]:
        min=l
    if r<n and a[r]<a[min]:
        min =r

    if min!=i:
        a[i],a[min]=a[min],a[i]
        minheapify(a,min,n)

a=[100,20,50,3,10,5,1]
minheapify(a,0,len(a))
print(a)
