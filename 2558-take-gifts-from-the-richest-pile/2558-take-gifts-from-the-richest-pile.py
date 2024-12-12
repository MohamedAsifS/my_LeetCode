import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
         
        
      
         for i in range(k):
             heapq._heapify_max(gifts)
             gifts[0]=math.sqrt(gifts[0])
         return int(sum(gifts))

        
       

       
          
        