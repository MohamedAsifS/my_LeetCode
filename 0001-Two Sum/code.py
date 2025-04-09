class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      res={}

      for i in range(len(nums)):
       
        if target-nums[i] in res.keys():
            return [res[target-nums[i]],i]
        res[nums[i]]=i
        