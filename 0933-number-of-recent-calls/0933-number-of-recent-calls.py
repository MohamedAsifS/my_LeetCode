class RecentCounter:

    def __init__(self):
        self.array=Deque()
     
        

    def ping(self, t: int) -> int:
        self.array.append(t)
        while self.array and self.array[0]<t-3000:
            self.array.popleft()
        
        return len(self.array)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)