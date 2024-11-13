class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        #O(logn)

    

        nums=sorted(nums)

        print(nums)
        i=0
        j=i+1

        count=0

        for i in range(len(nums)):
           for j in range(i,len(nums)):
              if nums[i]+nums[j]>upper:
                   break
              if nums[i] + nums[j] <=upper and nums[i]+nums[j]>=lower:
                     count+=1
              
                     
             
              
           
        return count

        
        