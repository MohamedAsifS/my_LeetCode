class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        intial=nums[0]
        res=[]
        res.append(intial)
        for i in range(1,len(nums)):
            intial+=nums[i]
            res.append(intial)
        return res
        