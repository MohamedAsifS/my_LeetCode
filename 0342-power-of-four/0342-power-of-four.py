class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n < 0:
            return False
       
        
        if bin(n).count('1')==1 and bin(n)[2:][::-1].index("1")%2==0:
            return True
        return False
        