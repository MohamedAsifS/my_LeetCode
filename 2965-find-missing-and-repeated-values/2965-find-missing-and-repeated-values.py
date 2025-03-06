class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hash={}

        for i in range(1,(len(grid[0])**2)+1):
              hash[i]=False
        res=[0]*2
        for i in grid:
            for j in i:
                if j in hash and hash[j]==False:
                    hash[j]=True
                else:
                    
                    res[0]=j
       
        for i in hash.keys():
            
            if hash[i]==False:

                res[1]=i
                break
        return res

        

        