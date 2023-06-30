def maxproduct(arr):
    q=[]
    for i in range(len(arr)):
        q.append(arr[i])
        if i<2:
            print(-1)
        if i>=2:
            x = q.pop()
            y = q.pop()
            z = q.pop()

            ans = x * y * z
            print(ans)
            q.append(z)
            q.append(y)
            q.append(x)
            print(q)

arr = [ 1, 2, 3, 4, 5 ]
maxproduct(arr)
