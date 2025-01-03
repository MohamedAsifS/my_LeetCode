class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        second_half=sum(nums)
        first_half=0
        res=0
        for i in range(len(nums)-1):
            second_half-=nums[i]
            first_half+=nums[i]
            if first_half >= second_half:
                res+=1
        return res
           

      
        