class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        res=""
        while n!=0:
            if n%3==2:
                return False
            if n%3==0:
                res+="0"
            else:
                res+=str(n%3)
                
            n//=3

        return res.count('1')==1 
        