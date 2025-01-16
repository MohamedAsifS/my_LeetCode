class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
      if (len(nums1)+len(nums2))%2==0:
        return 0

      res=nums2[0]
      for i in range(1,len(nums2)):
           res^=nums2[i]
      return res
        