class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # we know kadens algorithim is used to find maximum (but its like leaving negative and take positive)

        cur_sum=0
        res=float('-inf')
        for i in nums:
            cur_sum+=i
            res=max(res,cur_sum)
            if cur_sum < 0:
                cur_sum=0
        return res
        