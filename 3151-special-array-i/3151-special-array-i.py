class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        eve_res=0
        odd_res=0
        for i in nums:
            if i%2==0 and  eve_res==1:
                   return False
            elif i%2==0 :
                 odd_res=0
                 eve_res=1
            elif i%2==1 and  odd_res==1:
                return False
            else:
                odd_res=1
                eve_res=0
        return True


                
            
            
        