from itertools import permutations

 
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        f=set()
        res=0

        for i in range(1,len(tiles)+1):
            pre=permutations(tiles,i)
            for i in pre:
                f.add(i)
      

       
            
        return len(f)



        
        