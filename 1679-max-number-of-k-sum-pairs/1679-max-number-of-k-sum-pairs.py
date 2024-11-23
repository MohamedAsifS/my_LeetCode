class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

       
        table={}
        res=0
        for i in nums:
            if i in table and table[i]>=1:
                 res+=1
                 table[i]-=1
            elif k-i not in table:
                table[k-i]=1
            elif k-i in table:
                table[k-i]+=1
          
        return res