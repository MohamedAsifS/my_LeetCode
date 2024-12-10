class Solution:
    def arrangeCoins(self, n: int) -> int:
        m=n
        res=0
        for i in range(1,n+1):
            if m >=i:
                m-=i 
                res+=1
            else:
                break
        return res