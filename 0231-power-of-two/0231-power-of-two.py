class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if bin(n).count('1')==1 and n>=0:
          
            return True
        else:
            
            return False
        