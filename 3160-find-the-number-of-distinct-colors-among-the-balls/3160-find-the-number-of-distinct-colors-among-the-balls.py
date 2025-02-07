class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        res=[]

        hash={}
        tracker={}

        for i in queries:
            if i[0] not in hash and i[1] not in tracker:
                hash[i[0]]=i[1]
                tracker[i[1]]=i[0]
            elif i[0] in hash :
                del tracker[hash[i[0]]]
                tracker[i[1]]=i[0]
                hash[i[0]]=i[1]
           
                
                   
             

            
          
           
          
            res.append(len(tracker))
        return res
        