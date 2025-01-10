class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        res=[]

        
        
        
        
        freq=[0]*26 
        temp=[0]*26     
        for word in words2:
           for i in word:
                temp[ord(i)-ord('a')]+=1
           for m in range(26):
               freq[m]=max(freq[m],temp[m])
           temp=[0]*26
        for i in words1:
            maxi=[0]*26
            check=True
            for j in i:
                maxi[ord(j)-ord('a')]+=1
            for u in range(26):
                if maxi[u] < freq[u]:
                    check=False
            if check:
                res.append(i)
            

         
                

            

        
      
  
       
              
                
            
                     
           
           
                 

               
        return res

            
