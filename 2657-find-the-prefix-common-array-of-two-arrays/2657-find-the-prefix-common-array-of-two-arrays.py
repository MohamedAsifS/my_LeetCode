class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c=[]
       
        for i in range(1,len(A)+1):
            res=len(set(A[0:i])&set(B[0:i]))
           
            c.append(res)
        return c
        
            

        