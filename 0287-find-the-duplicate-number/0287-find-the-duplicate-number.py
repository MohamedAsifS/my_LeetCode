class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        arr=[0]*(len(nums)+1)

        for i in nums:
            if arr[i]!=0:
                return i
            arr[i]=1
        
        
         
        
           
                
        