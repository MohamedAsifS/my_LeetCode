class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        res=[]

        hash={}
        tracker={}

        for pos,col in queries:
            if pos in hash:
                old=hash[pos]
                tracker[old]-=1
                if tracker[old]==0:
                    del tracker[old]
            hash[pos]=col
            tracker[col]=tracker.get(col,0)+1

            res.append(len(tracker))
        return res

            


            
           
                
                   
             

            
          
           
          
       
        