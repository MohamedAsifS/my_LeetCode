class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        temp=set()
        i=0
        j=0
        res=0
       
        while j<len(s):
          
           
            if s[j] not in temp:
                temp.add(s[j])
                j+=1
            else:
                temp=set()
                i+=1
                j=i

            if len(temp)==3:
               
                temp=set()
                res+=1
                i+=1
                j=i
            
        return res
            
        