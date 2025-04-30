class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if (math.floor(math.log10(i))+1) % 2==0:
                count+=1
        return count