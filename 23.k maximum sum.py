def findsum(ar1,ar2,k):
    n1=len(ar1)
    n2=len(ar2)
    ar=[]
    for i in range(n1):
        for j in range(n2):
            sum=ar1[i]+ar2[j]
            insert(ar,sum)

    for i in range(k):
        print(ar[i])


def insert(ar,sum):
    key=sum
    ar.append(sum)

    if len(ar)>1:

        j=len(ar)-2

        while j>=0 and ar[j]<key:
            ar[j+1]=ar[j]
            j=j-1
        ar[j+1]=key


A = [ 4, 2, 5, 1 ]
B = [ 8, 0, 5, 3 ]
findsum(A,B,3)
