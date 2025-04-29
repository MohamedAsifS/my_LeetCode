class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
        check=set()

        for i in range(1,len(nums)):
            s=nums[i-1]+nums[i]
            if s in check:
                return True
            check.add(s)
        return False

