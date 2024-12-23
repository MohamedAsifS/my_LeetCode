class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        colinr=[]
    

        res=0

        for i in range(len(grid)):
            temp=[]
            for j in range(len(grid[i])):
                temp.append(grid[j][i])
            colinr.append(temp)
            
        hash1={}
        hash2={}

        for i in grid:
            val=tuple(i)
            if val not in hash1:
                hash1[val]=1
            else:
                hash1[val]+=1
        for i in colinr:
            val=tuple(i)
            if val not in hash2:
                hash2[val]=1
            else:
                hash2[val]+=1
        
       
        for i in grid:
            if hash2.get(tuple(i),0)!=0:
                 res+=hash2[tuple(i)]
        return res
        
       

        