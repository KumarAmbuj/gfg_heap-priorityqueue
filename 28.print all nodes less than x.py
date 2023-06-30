class minheap():
    harr=[]
    heapsize=0
    capacity=0
    def parent(self,i):
        return (i-1)//2
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2

    def insertKey(self,key):

        self.harr.append(key)
        i=len(self.harr)-1

        while i!=0 and self.harr[self.parent(i)]>self.harr[i]:
            self.harr[self.parent(i)],self.harr[i]=self.harr[i],self.harr[self.parent(i)]

            i=self.parent(i)
    def printsmaller(self,x,pos):
        if pos>= len(self.harr):
            return
        if self.harr[pos]<=x:
            print(self.harr[pos],end=' ')
        self.printsmaller(x,self.left(pos))
        self.printsmaller(x,self.right(pos))

h=minheap()


h.insertKey(3);
h.insertKey(2);
h.insertKey(15);
h.insertKey(5);
h.insertKey(4);
h.insertKey(45);
h.insertKey(80);
h.insertKey(6);
h.insertKey(150);
h.insertKey(77);
h.insertKey(120);

h.printsmaller(100,0)




