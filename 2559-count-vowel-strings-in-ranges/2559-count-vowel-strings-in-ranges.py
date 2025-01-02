class Solution:
    def vowel_count(self,word):
        e={"a","e","i","o","u"}
        if len(word)==1 and word in e:
            return 1
        elif word[0] in e and word[-1] in e:
            return 1
        else:
            return 0

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res=[]
        temp=0
        for i in words:
             temp+=self.vowel_count(i)
             res.append(temp)
   
        final=[]
        for i in queries:
            temp=res[i[1]]
            if i[0]!=0:
                temp-=res[i[0]-1]
            final.append(temp)
        return final
        