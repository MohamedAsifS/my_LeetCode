class Solution:

       

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res=[]
        temp=0
        e={"a","e","i","o","u"}
        for i in words:
           
            if len(i)==1 and i in e:
                temp+=1
            elif i[0] in e and i[-1] in e:
                temp+=1
           
           
            res.append(temp)
   
        final=[]
        for i in queries:
            temp=res[i[1]]
            if i[0]!=0:
                temp-=res[i[0]-1]
            final.append(temp)
        return final
        