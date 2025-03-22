class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        count=0
        res=nums[0]
        for i in nums:
           if count < 0:
              count=0
           count+=i

           
           res=max(res,count)
        return res
        