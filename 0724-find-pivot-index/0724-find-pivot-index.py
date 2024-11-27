class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

       left,right=0,sum(nums)

       for i,j in enumerate(nums):
           right-=j
           if right==left:
                return i
           left+=j
       return -1
        