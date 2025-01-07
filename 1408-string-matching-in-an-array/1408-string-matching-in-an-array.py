class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        words=sorted(words)
        for i in range(len(words)):
            for j in range(len(words)-1,i,-1):
                if words[i] in words[j]:
                    res.append(words[i])
        return res






        