class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]*len(nums)
        res=[1]*len(nums)
        mul=1

        for i in range(len(nums)):
            pre[i]=mul
            mul=nums[i]*mul
      
        mul=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=mul*pre[i]
            mul=nums[i]*mul
        return res
        
        