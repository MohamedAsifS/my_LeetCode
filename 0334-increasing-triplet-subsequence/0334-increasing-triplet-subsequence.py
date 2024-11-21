class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        h1=float('inf')
        h2=float('inf')

        for i in nums:
            if i <=h1:
                h1=i
            elif i<=h2:
                h2=i
            else:
                return True
        return False
        
