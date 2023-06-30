def heapify(ar,i,n):
    largest=i
    l=2*i+1
    r=2*i+2

    if l<n and ar[l]>ar[i]:
        largest=l
    if r<n and ar[r]>ar[largest]:
        largest=r

    if largest!=i:
        ar[i],ar[largest]=ar[largest],ar[i]
        heapify(ar,largest,n)

def insert(ar,key):

    ar.append(key)

    i=len(ar)-1

    if i>=3:

        while i>0 and ar[i]>ar[i//2]:
            ar[i],ar[i//2]=ar[i//2],ar[i]
            i=i//2

def findsum(ar1,ar2,k):

    n1=len(ar1)
    n2=len(ar2)
    ar=[]
    for i in range(n1):
        for j in range(n2):
            sum=ar1[i]+ar2[j]
            insert(ar,sum)
            if len(ar)==3:
                heapify(ar,0,len(ar))
    n=len(ar)-1
    for i in range(k):

        max=ar[0]
        ar[0]=ar[n]
        n=n-1

        heapify(ar,0,n)

        print(max)
A = [ 4, 2, 5, 1 ] 
B = [ 8, 0, 5, 3 ]
findsum(A,B,3)






