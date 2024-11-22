class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
       l,r=0,0

       while l!=len(nums):
         if nums[l]!=0:
             temp=nums[l]
             nums[l]=nums[r]
             nums[r]=temp
             r+=1
         l+=1