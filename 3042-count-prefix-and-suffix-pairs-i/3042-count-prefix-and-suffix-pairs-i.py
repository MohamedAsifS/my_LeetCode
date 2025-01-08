class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[j][0:len(words[i])]==words[i] and words[j][len(words[j])-len(words[i]):len(words[j])]==words[i]:
                    res+=1
        return res


      

        