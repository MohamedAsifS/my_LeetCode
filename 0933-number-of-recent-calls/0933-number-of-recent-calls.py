class RecentCounter:

    def __init__(self):
        self.array=[]
        self.array.append(None)
        

    def ping(self, t: int) -> int:
        start=t-3000
        end=t
        res=0
        self.array.append(t)
        for i in range(1,len(self.array)):
                if self.array[i]>=start and self.array[i]<=end:
                    res+=1 
        
        return res

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)