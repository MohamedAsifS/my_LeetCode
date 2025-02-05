class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
         
        h=set()
        for  i in nums:
            if i not in h:
                h.add(i)
            else:
                return i
           
                
        