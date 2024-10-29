class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        temp=""
        for i in words:
            temp+=i
        const={}

        for i in temp:
            if i not in const:
                const[i]=1
            else:
                const[i]+=1
        get=len(words)
       

        for i in const:
            if (const[i]%get)!=0:
                 return False
        return True
        