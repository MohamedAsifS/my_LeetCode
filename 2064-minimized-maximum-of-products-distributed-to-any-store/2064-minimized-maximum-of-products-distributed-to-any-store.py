class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def helper(x):
            store=0
            for i in quantities:
                store+=math.ceil(i/x)
            return  store <= n
        

        l,r=1,max(quantities)
        res=0

        while l <= r:
            m=(l+r)//2
            if helper(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res



        
        