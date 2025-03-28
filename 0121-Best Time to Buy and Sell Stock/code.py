class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum=1111111
        res=0

        for i in prices:
            minimum=min(i,minimum)
            res=max(res,i-minimum)
        return res
        