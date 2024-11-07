class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
          
          bit=[0]*32

          for i in candidates:
            temp_changer=bin(i)[2:]
           
            for count,i in enumerate(reversed(temp_changer)):
               
                if i=='1':
                    bit[count]+=1
       
          return max(bit)

                
        

       
        