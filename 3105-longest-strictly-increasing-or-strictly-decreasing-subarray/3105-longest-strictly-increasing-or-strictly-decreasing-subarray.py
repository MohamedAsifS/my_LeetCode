class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ini=1
        de=1
        res=1
        for i in range(len(nums)-1):
               if nums[i] < nums[i+1]:
                    ini=1
                    de+=1
               elif nums[i] > nums[i+1]:
                    ini+=1
                    de=1
               else:
                    de,ini=1,1
               res=max(res,de,ini)
               

      
                
                
              
        return res