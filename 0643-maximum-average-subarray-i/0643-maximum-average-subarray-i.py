class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        l=0
        res=float(-inf)
        sum=0
     
        n=k
        for r in range(len(nums)):
            sum+=nums[r]
            if r==(k-1):
              
                 res=max(res,sum)
              
                
                 sum-=nums[l]
                 l=l+1
                 k=k+1
      
        return res/n
       
            
