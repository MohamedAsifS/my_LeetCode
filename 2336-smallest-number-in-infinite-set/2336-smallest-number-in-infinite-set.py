class SmallestInfiniteSet:

    def __init__(self):
        self.data=list(range(1,1001))
        heapq.heapify(self.data)
        

    def popSmallest(self) -> int:
        return heapq.heappop(self.data)

    def addBack(self, num: int) -> None:
        k=set(self.data)
        if num not in k:
            heapq.heappush(self.data,num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)