class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                nums[i-1]=nums[i-1]*2
                nums[i]=0
        l,r=0,0
        while l!=len(nums):
            if nums[l]!=0:
                temp=nums[l]
                nums[l]=nums[r]
                nums[r]=temp
                r+=1
            l+=1
        return nums

        