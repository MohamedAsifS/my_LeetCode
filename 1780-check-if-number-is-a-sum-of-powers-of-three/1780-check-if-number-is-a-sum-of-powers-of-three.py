class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        res=""
        while n != 0:
            if n%3==2:
                return False
            n//=3
        return True
        
        