class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        res=[]

        temp=[]
        for i in words2:
         
          
                
               
                for j in i:
                    temp.append(j)

        
      
            
        for i in words1:
            check=True
            for j in temp:
                if j not in i:
                    check=False
            if check:
                res.append(i)

               
        return res

            
