from collections import OrderedDict
class Solution:

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

       res=0

       count=defaultdict(int)

       sum=0

       l=0

       for r in range(len(nums)):
          sum+=nums[r]
          count[nums[r]]+=1

          if r-l+1 >k:
            sum-=nums[l]
            count[nums[l]]-=1
            if count[nums[l]]==0:
                count.pop(nums[l])
            l+=1
          if len(count)==k and r-l+1==k:
            res=max(res,sum)
       return res