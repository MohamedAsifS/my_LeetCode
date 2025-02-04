class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        res=0
        count=nums[0]

        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                count+=nums[i]
                res=max(res,count)
            else:
                count=0
                count+=nums[i]
        return res
        

        