class Solution:

    def __init__(self, nums: List[int]):
        self.hash={}
        for i,j in enumerate(nums):
            if j not in self.hash:
                 self.hash[j]=[]
                 self.hash[j].append(i)
            else:
                self.hash[j].append(i)
        

    def pick(self, target: int) -> int:
        return random.choice(self.hash[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)