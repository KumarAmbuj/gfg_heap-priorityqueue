def maxheapify(a,i,n):
    largest = i
    l=2*i+1
    r=2*i+2



    if l < n and a[i] < a[l]:
        largest=l


    if r<n and a[r]>a[largest]:
        largest=r

    if largest!=i:
        a[i],a[largest]=a[largest],a[i]
        maxheapify(a, largest, n)



a=[1,3,6,5,9,8]
maxheapify(a,0,len(a))
print(a)