class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums=sorted(nums)
        r=0
        l=len(nums)-1
        res=0
        while r <= l:
            res=max(res,nums[r]+nums[l])
            r+=1
            l-=1
        return res

        