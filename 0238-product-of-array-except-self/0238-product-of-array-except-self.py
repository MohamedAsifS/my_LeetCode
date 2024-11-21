class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        postfix=[1]*len(nums)
        mul=1

        for i in range(len(nums)):
           prefix[i]=mul
           mul*=nums[i]
        mul=1
        for i in range(len(nums)-1,-1,-1):
            postfix[i]=mul
            mul*=nums[i]
        
        for i in range(len(nums)):
            nums[i]=prefix[i]*postfix[i]
        return nums
        



           

        
        
        