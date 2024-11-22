class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        r,l=0,0

        while l!=len(nums):
            if nums[l]!=0:
                temp=nums[l]
                nums[l]=nums[r]
                nums[r]=temp
                r=r+1
            l=l+1
        