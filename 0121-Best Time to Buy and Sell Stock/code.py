class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res=0
        price=float('inf')
        for i in prices:
            price=min(price,i)
            res=max(res,i-price)
        return res

        