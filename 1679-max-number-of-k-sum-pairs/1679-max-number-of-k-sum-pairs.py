class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums=sorted(nums)
        l=0
        r=len(nums)-1
        res=0
        while l<r:
            if nums[l]+nums[r]==k:
                print(nums[l],nums[r])
                res+=1
            l+=1
            r-=1
        return res
        